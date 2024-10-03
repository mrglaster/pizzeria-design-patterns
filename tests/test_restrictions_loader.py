import unittest

from src.modules.configuration.length_restricions_configuration import LengthRestrictionsLoader
from src.modules.exception.conf_file_not_found import ConfigurationFileNotFound


class TestRestrictionsLoader(unittest.TestCase):
    def test_restrictions_loader(self):
        data = LengthRestrictionsLoader.get_restrictions()
        assert data is not None
        assert len(data.keys()) == 9

    def test_load_restrictions_invalid_path(self):
        with self.assertRaises(ConfigurationFileNotFound):
            data = LengthRestrictionsLoader.get_restrictions("azaza.json")

