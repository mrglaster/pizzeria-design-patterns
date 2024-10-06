import os
import unittest
from src.modules.domain.measures.measurment_unit_model import MeasurementUnit
from src.modules.domain.nomenclature.nomenclature_group_model import NomenclatureGroup
from src.modules.domain.nomenclature.nomenclature_model import Nomenclature
from src.modules.domain.organization.organization_model import Organization
from src.modules.exception.bad_argument_exception import BadArgumentException
from src.modules.service.managers.settings_manager import SettingsManager


class TestModels(unittest.TestCase):
    def test_nomenclature_diff_uid(self):
        assert NomenclatureGroup("aaaa") != NomenclatureGroup("aaaa")

    def test_nomenclature_group_model_getters(self):
        group_name = "group"
        group = NomenclatureGroup(group_name)
        assert group.name == group_name

    def test_measurements_scales(self):
        unit_name = "г"
        assert MeasurementUnit.create(unit_name, unit=1.) == MeasurementUnit.create(unit_name, unit=1000.)

    def test_measurement_unit_setters(self):
        unit_name = "g"
        unit = 1
        g = MeasurementUnit.create("1", 666)
        g.unit = unit
        g.name = unit_name
        assert g.unit == unit
        assert g.name == unit_name

    def test_measurement_base_unit_model(self):
        base_unit_name = "г"
        unit_name = "к"
        big_unit_name = "т"

        g_unit = MeasurementUnit.create(base_unit_name, 1)
        kg_unit = MeasurementUnit.create(unit_name, 1000, g_unit)
        t_unit = MeasurementUnit.create(big_unit_name, 1000, kg_unit)

        kg_base_unit = kg_unit.base_measure_unit
        t_base_unit = t_unit.base_measure_unit
        assert kg_base_unit == g_unit
        assert t_base_unit == kg_unit

    def test_measurement_unit_exceptions(self):
        wrong_unit_name = 42
        unit = 1
        with self.assertRaises(BadArgumentException):
            MeasurementUnit.create(wrong_unit_name, unit)

    def test_nomenclature_model(self):
        g_unit = MeasurementUnit.create("грамм", 1)
        kg_unit = MeasurementUnit.create("килограмм", 1000, g_unit)
        ingredients = NomenclatureGroup.create("Ингридиенты")
        equipments = NomenclatureGroup.create("Оборудование")

        sausage = Nomenclature.create("Колбаса", ingredients, kg_unit, "a" * 100)
        cooker = Nomenclature.create("Плита", equipments, kg_unit, "b"*100)

        assert sausage.nomenclature_group == ingredients
        assert sausage.measurement_unit == kg_unit
        assert cooker.nomenclature_group == equipments
        assert cooker.measurement_unit == kg_unit

    def test_organization_model_converting(self):
        settings_manager = SettingsManager()
        file_path = os.path.join(os.getcwd(), "configuration", "settings.json")
        file_path = file_path.replace("tests/", "")
        settings_manager.read_settings(file_path)
        settings = settings_manager.settings
        org = Organization.create(settings)
        assert org.name == settings.organization_name
        assert org.inn == settings.inn
        assert org.bank_account == settings.bank_account
        assert org.bik == settings.bik
        assert org.property_type == settings.property_type
