import unittest
from src.modules.factory.repository_factory.repository_factory import RepositoryFactory
from src.modules.service.init_service.start_service import StartService


class TestDumpingSystem(unittest.TestCase):

    def test_dumps_processing(self):
        ss = StartService()
        ss.create()
        repos = list(RepositoryFactory().repositories.values())
        for repo in repos:
            begin_data = list(repo.get_all().values())
            repo.dump()
            repo.clear()
            assert not len(list(repo.get_all().values()))
            if len(begin_data):
                repo.load_dump()
                new_data = list(repo.get_all().values())
                assert len(begin_data) == len(new_data)
