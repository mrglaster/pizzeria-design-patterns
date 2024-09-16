import os
import unittest

from modules.domain.measures.measurment_unit_model import MeasurementUnit
from modules.domain.nomenclature.nomenclature_group_model import NomenclatureGroup
from modules.domain.nomenclature.nomenclature_model import Nomenclature
from modules.domain.organization.organization_model import Organization
from modules.exception.bad_argument_exception import BadArgumentException
from modules.managers.settings_manager import SettingsManager


class TestUtils(unittest.TestCase):
    def test_nomenclature_diff_uid(self):
        assert NomenclatureGroup("aaaa") != NomenclatureGroup("aaaa")

    def test_nomenclature_group_model_getters(self):
        group_name = "group"
        group = NomenclatureGroup(group_name)
        assert group.name == group_name

    def test_measurements_scales(self):
        unit_name = "г"
        assert MeasurementUnit(unit_name, unit=1.) == MeasurementUnit(unit_name, unit=1000.)

    def test_measurement_unit_setters(self):
        unit_name = "g"
        unit = 1
        g = MeasurementUnit("1", 666)
        g.unit = unit
        g.name = unit_name
        assert g.unit == unit
        assert g.name == unit_name

    def test_measurement_base_unit_model(self):
        base_unit_name = "г"
        unit_name = "к"
        big_unit_name = "т"

        g_unit = MeasurementUnit(base_unit_name, 1)
        kg_unit = MeasurementUnit(unit_name, 1000, g_unit)
        t_unit = MeasurementUnit(big_unit_name, 1000, kg_unit)

        kg_base_unit = kg_unit.base_measure_unit
        t_base_unit = t_unit.base_measure_unit
        assert kg_base_unit == g_unit
        assert t_base_unit == kg_unit

    def test_measurement_unit_exceptions(self):
        wrong_unit_name = 42
        unit = 1
        with self.assertRaises(BadArgumentException):
            MeasurementUnit(wrong_unit_name, unit)

    def test_nomenclature_model(self):
        g_unit = MeasurementUnit("грамм", 1)
        kg_unit = MeasurementUnit("килограмм", 1000, g_unit)
        ingridients = NomenclatureGroup("Ингридиенты")
        equipments = NomenclatureGroup("Оборудование")

        sausage = Nomenclature("Колбаса", ingridients, kg_unit, "a"*100)
        cooker = Nomenclature("Плита", equipments, kg_unit, "b"*100)

        assert sausage.nomenclature_group == ingridients
        assert sausage.measurement_unit == kg_unit
        assert cooker.nomenclature_group == equipments
        assert cooker.measurement_unit == kg_unit

    def test_organization_model_converting(self):
        settings_manager = SettingsManager()
        file_path = os.path.join(os.getcwd(), "configuration", "settings.json")
        file_path = file_path.replace("test/", "")
        settings_manager.read_settings(file_path)
        settings = settings_manager.settings
        print(settings)
        org = Organization(settings)
        assert org.name == settings.organization_name
        assert org.inn == settings.inn
        assert org.bank_account == settings.bank_account
        assert org.bik == settings.bik
        assert org.property_type == settings.property_type
