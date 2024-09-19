import json
from modules.domain.measures.measurment_unit_model import MeasurementUnit
from modules.validation.data_validator import DataValidator


class MeasurementUnitRepository:
    __units = {}

    @staticmethod
    def get_unit_by_name(name: str) -> MeasurementUnit:
        DataValidator.validate_field_type(name, str)
        if name in MeasurementUnitRepository.__units:
            return MeasurementUnitRepository.__units.get(name)  # More efficient lookup
        return None

    @staticmethod
    def create_new_measurement_unit(name: str, connected_unit: MeasurementUnit = None, converted: float = 1.0):
        if name not in MeasurementUnitRepository.__units:
            DataValidator.validate_field_type(connected_unit, MeasurementUnit, True)
            new_unit = MeasurementUnit(name=name, unit=converted, base_measure_unit=connected_unit)
            MeasurementUnitRepository.__units[name] = new_unit
            if connected_unit and connected_unit.name not in MeasurementUnitRepository.__units:
                MeasurementUnitRepository.__units[connected_unit.name] = connected_unit
        return MeasurementUnitRepository.__units[name]

    @staticmethod
    def create_related_unit_by_name(name: str, related_unit_name: str, converted: float):
        if name not in MeasurementUnitRepository.__units:
            related_unit = MeasurementUnitRepository.get_unit_by_name(related_unit_name)
            if related_unit:
                MeasurementUnitRepository.create_new_measurement_unit(name, related_unit, converted)

    @staticmethod
    def clear_repository():
        MeasurementUnitRepository.__units.clear()  # Clear dictionary

    @staticmethod
    def load_units_from_json(json_file: str):
        try:
            with open(json_file, 'r') as f:
                json_data = json.load(f)["units"]
                for unit_data in json_data.values():
                    unit_name = unit_data["name"]
                    MeasurementUnitRepository.create_new_measurement_unit(name=unit_name)

                for unit_data in json_data.values():
                    related_unit_name = unit_data["related_unit"]
                    if related_unit_name != "NONE":
                        current_unit = MeasurementUnitRepository.get_unit_by_name(unit_data["name"])
                        current_unit.base_measure_unit = MeasurementUnitRepository.get_unit_by_name(related_unit_name)
                        current_unit.unit = unit_data["conversion_factor"]

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading JSON file: {e}")

    @staticmethod
    def get_all():
        return MeasurementUnitRepository.__units

    @staticmethod
    def clear():
        MeasurementUnitRepository.__units = {}

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(MeasurementUnitRepository, cls).__new__(cls)
        return cls.instance
