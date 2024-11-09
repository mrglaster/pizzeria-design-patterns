from src.modules.domain.base.abstract_reference import AbstractReference


class Address(AbstractReference):
    __country = ""
    __region = ""
    __city = ""
    __street = ""
    __building_number = ""

    @classmethod
    def create(cls, country: str = "", region: str= "", city: str= "", street: str= "", building_number: str= ""):
        instance = cls()
        instance.__country = country
        instance.__region = region
        instance.__city = city
        instance.__street = street
        instance.__building_number = building_number
        return instance

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, value: str):
        self.__country = value

    @property
    def region(self) -> str:
        return self.__region

    @region.setter
    def region(self, value: str):
        self.__region = value

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, value: str):
        self.__city = value

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, value: str):
        self.__street = value

    @property
    def building_number(self) -> str:
        return self.__building_number

    @building_number.setter
    def building_number(self, value: str):
        self.__building_number = value

    def __eq__(self, other):
        if not isinstance(other, Address):
            return False
        return (self.__country == other.__country and
                self.__region == other.__region and
                self.__city == other.__city and
                self.__street == other.__street and
                self.__building_number == other.__building_number)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.__country, self.__region, self.__city, self.__street, self.__building_number))


