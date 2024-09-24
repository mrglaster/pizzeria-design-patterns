from modules.domain.base.abstract_reference import AbstractReference
from modules.domain.nomenclature.nomenclature_model import Nomenclature
from modules.domain.recipes.ingredient import Ingredient
from modules.domain.recipes.recipe_step import RecipeStep
from modules.validation.data_validator import DataValidator


class Recipe(AbstractReference):
    def __init__(self, name: str, portions_count: int = 1, cooking_time_mins: int = None):
        super().__init__(name)
        self.__name = name
        self.__ingredients = []
        self.__portions_count = portions_count
        self.__cooking_time_mins = cooking_time_mins
        self.__steps = []
        self.__step_count = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        DataValidator.validate_field_type(value, str)
        self.__name = value

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value: list):
        DataValidator.validate_field_type(value, list)
        self.__ingredients = value

    @property
    def portions_count(self):
        return self.__portions_count

    @portions_count.setter
    def portions_count(self, value: int):
        DataValidator.validate_field_type(value, int)
        self.__portions_count = value

    @property
    def cooking_time_mins(self):
        return self.__cooking_time_mins

    @cooking_time_mins.setter
    def cooking_time_mins(self, value: int):
        DataValidator.validate_field_type(value, int)
        self.__cooking_time_mins = value

    @property
    def steps(self):
        return self.__steps

    @steps.setter
    def steps(self, value: list):
        DataValidator.validate_field_type(value, list)
        DataValidator.validate_list_not_empty(value)
        self.__steps = value
        self.__step_count = len(value)

    @property
    def step_count(self):
        return self.__step_count

    def add_ingredient(self, ingredient: Ingredient):
        DataValidator.validate_field_type(ingredient, Ingredient)
        if ingredient not in self.__ingredients:
            self.__ingredients.append(ingredient)

    def add_step(self, description: str):
        DataValidator.validate_field_type(description, str)
        new_step = RecipeStep(step_id=self.__step_count + 1, description=description)
        if new_step not in self.__steps:
            self.__steps.append(new_step)
            self.__step_count += 1

    def __eq__(self, other):
        try:
            assert isinstance(other, Recipe)
            assert self.__name == other.name
            assert self.__ingredients == other.ingredients
            assert self.__portions_count == other.portions_count
            assert self.__cooking_time_mins == other.cooking_time_mins
        except:
            return False

    def __ne__(self, other):
        return not self == other
