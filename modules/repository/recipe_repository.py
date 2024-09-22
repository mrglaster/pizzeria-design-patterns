from modules.repository.data_repository import AbstractRepository
from modules.service.data_loader.recipe_loader import RecipeLoader
from modules.validation.data_validator import DataValidator


class RecipeRepository(AbstractRepository):
    __recipes = {}

    @staticmethod
    def find_recipe_by_name(name: str):
        DataValidator.validate_field_type(name, str, False)
        if name in RecipeRepository.__recipes.keys():
            return RecipeRepository.__recipes[name]
        return None

    @staticmethod
    def load_recipe_from_file(file_path):
        recipe = RecipeLoader.load_from_json_file(file_path)
        if recipe.name not in RecipeRepository.__recipes.keys():
            RecipeRepository.__recipes[recipe.name] = recipe
        return recipe

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(RecipeRepository, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_all():
        return RecipeRepository.__recipes

    @staticmethod
    def clear():
        RecipeRepository.__recipes = {}