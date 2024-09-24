import re
from modules.domain.recipes.ingredient import Ingredient
from modules.domain.recipes.recipe import Recipe
from modules.repository.measurment_unit_repository import MeasurementUnitRepository
from modules.repository.nomenclature_group_repository import NomenclatureGroupRepository
from modules.repository.nomenclature_repository import NomenclatureRepository
from modules.service.data_loader.abstract_loader import AbstractDataLoader


class RecipeLoader(AbstractDataLoader):

    @staticmethod
    def load_from_json_file(file_path: str) -> Recipe:
        with open(file_path) as f:
            md_content = f.read()
            title_match = re.search(r'# (.+)', md_content)
            recipe_name = title_match.group(1) if title_match else "Без названия"
            portions_match = re.search(r'#### `(\d+) порций`', md_content)
            portions_count = int(portions_match.group(1)) if portions_match else 1
            recipe = Recipe(name=recipe_name, portions_count=portions_count)
            for line in md_content.split('\n'):
                if '|' in line and 'ингредиенты' not in line.lower() and 'граммовка' not in line.lower() and '-|' not in line:
                    current_row = line.lstrip().split('|')[1:][:-1]
                    current_row = [i.strip() for i in current_row]
                    count_data = current_row[1].split(' ')
                    ingredient_name = current_row[0]
                    amount = float(count_data[0])
                    measure = count_data[1]
                    measurement_unit = MeasurementUnitRepository.create_new_measurement_unit(measure, None, 1)
                    ing_category = NomenclatureGroupRepository.create_new_group("ингредиент")
                    nomenclature = NomenclatureRepository.create_nomenclature(ingredient_name, ing_category,
                                                                              measurement_unit)
                    if nomenclature and measurement_unit:
                        ingredient = Ingredient(nomenclature=nomenclature, measurement_unit=measurement_unit,
                                                amount=amount)
                        recipe.add_ingredient(ingredient)
                if "время приготовления:" in line.lower():
                    cooking_time_data = line.lower().split('время приготовления:')[1].strip().replace('`', '').split(
                        ' ')
                    time = cooking_time_data[0]
                    recipe.cooking_time_mins = int(time)

            step_pattern = r'\d+\.\s(.*?)\n'
            steps = re.findall(step_pattern, md_content, re.DOTALL)
            for i in steps:
                recipe.add_step(i)
            return recipe
