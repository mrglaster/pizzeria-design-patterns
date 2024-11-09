from src.modules.domain.base.abstract_reference import AbstractReference
from src.modules.domain.enum.filter_types import FilterType
from src.modules.factory.repository_factory.repository_factory import RepositoryFactory
from src.modules.prototype.domain_prototype import DomainPrototype


class PostProcessor:

    @staticmethod
    def get_formatted_name(object):
        class_name = object.__class__.__name__
        formatted_name = object.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower()
        return formatted_name

    @staticmethod
    def delete(object_to_delete):
        formatted_name = PostProcessor.get_formatted_name(object_to_delete)
        repository = RepositoryFactory().get_by_name(formatted_name)()
        repository.delete(object_to_delete)

    @staticmethod
    def create(object_to_create):
        formatted_name = PostProcessor.get_formatted_name(object_to_create)
        repository = RepositoryFactory().get_by_name(formatted_name)()
        repository.add(object_to_create)

    @staticmethod
    def update(old_object, new_object):
        formatted_name = PostProcessor.get_formatted_name(old_object)
        repos = list(RepositoryFactory().repositories.keys())
        for repo in repos:
            if repo == formatted_name:
                continue
            proto = DomainPrototype().create_from_repository(repo)
            using = proto.filter_by(field_name=formatted_name, value=old_object,
                                    filter_type=FilterType.EQUALS).all()
            repo_obj = RepositoryFactory().get_by_name(repo)()
            for i in using:
                current = i
                prev = i
                PostProcessor.recursive_update(current, old_object, new_object)
                repo_obj.update(prev, current)
        source_repository = RepositoryFactory().get_by_name(formatted_name)()
        source_repository.update(old_object, new_object)

    @staticmethod
    def recursive_update(obj, old_object, new_object):
        for property_name in obj.get_properties():
            value = getattr(obj, property_name, None)
            if isinstance(value, AbstractReference):
                if value == old_object:
                    setattr(obj, property_name, new_object)
                else:
                    PostProcessor().recursive_update(value, old_object, new_object)
            elif value == old_object:
                setattr(obj, property_name, new_object)