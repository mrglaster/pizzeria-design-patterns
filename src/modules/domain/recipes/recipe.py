from src.modules.domain.base.abstract_reference import AbstractReference
from src.modules.domain.recipes.ingredient import Ingredient
from src.modules.domain.recipes.recipe_step import RecipeStep
from src.modules.validation.data_validator import DataValidator


class Recipe(AbstractReference):
    def __init__(self, name: str):
        super().__init__(name)
        self.__step_count = 0
        self.__ingredients = []
        self.__recipe_steps = []

    @classmethod
    def create(cls, name: str = "DEFAULT_RECIPE_NAME", portions_count: int = 1, cooking_time_mins: int = 0):
        instance = cls(name)
        instance.name = name
        instance.portions_count = portions_count
        instance.cooking_time_mins = cooking_time_mins
        return instance

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
        DataValidator.validate_field_type(value, int, nullable=True)
        self.__cooking_time_mins = value

    @property
    def recipe_steps(self):
        return self.__recipe_steps

    @recipe_steps.setter
    def recipe_steps(self, value: list):
        DataValidator.validate_field_type(value, list)
        DataValidator.validate_list_not_empty(value)
        self.__recipe_steps = value
        self.__step_count = len(value)

    @property
    def step_count(self):
        return self.__step_count

    @step_count.setter
    def step_count(self, value: int):
        DataValidator.validate_field_type(value, int)
        assert value > 0
        self.__step_count = value

    def add_ingredient(self, ingredient: Ingredient):
        DataValidator.validate_field_type(ingredient, Ingredient)
        if ingredient not in self.__ingredients:
            self.__ingredients.append(ingredient)

    def add_step(self, description: str):
        DataValidator.validate_field_type(description, str)
        new_step = RecipeStep.create(step_id=self.__step_count + 1, description=description)
        if new_step not in self.__recipe_steps:
            self.__recipe_steps.append(new_step)
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
