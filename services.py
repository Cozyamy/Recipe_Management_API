from models import Recipe, Ingredient, NutritionalInfo
import config

def create_recipe(recipe: Recipe):
    database = config.load_database()
    recipe_dict = recipe.dict()
    recipe_dict["id"] = len(database["recipes"]) + 1
    database["recipes"].append(recipe_dict)
    config.save_database(database)
    return recipe

def read_recipe(recipe_id: int):
    database = config.load_database()
    for recipe in database["recipes"]:
        if recipe["id"] == recipe_id:
            return recipe
    return None

def update_recipe(recipe_id: int, recipe: Recipe):
    database = config.load_database()
    for idx, rec in enumerate(database["recipes"]):
        if rec["id"] == recipe_id:
            database["recipes"][idx] = recipe.dict()
            config.save_database(database)
            return True
    return False

def delete_recipe(recipe_id: int):
    database = config.load_database()
    for idx, rec in enumerate(database["recipes"]):
        if rec["id"] == recipe_id:
            del database["recipes"][idx]
            config.save_database(database)
            return True
    return False

def create_ingredient(ingredient: Ingredient):
    database = config.load_database()
    ingredient_dict = ingredient.dict()
    ingredient_dict["id"] = len(database["ingredients"]) + 1
    database["ingredients"].append(ingredient_dict)
    config.save_database(database)
    return ingredient

def read_ingredient(ingredient_id: int):
    database = config.load_database()
    for ingredient in database["ingredients"]:
        if ingredient["id"] == ingredient_id:
            return ingredient
    return None

def update_ingredient(ingredient_id: int, ingredient: Ingredient):
    database = config.load_database()
    for idx, ing in enumerate(database["ingredients"]):
        if ing["id"] == ingredient_id:
            database["ingredients"][idx] = ingredient.dict()
            config.save_database(database)
            return True
    return False

def delete_ingredient(ingredient_id: int):
    database = config.load_database()
    for idx, ing in enumerate(database["ingredients"]):
        if ing["id"] == ingredient_id:
            del database["ingredients"][idx]
            config.save_database(database)
            return True
    return False

def create_nutritional_info(nutritional_info: NutritionalInfo):
    database = config.load_database()
    nutritional_info_dict = nutritional_info.dict()
    nutritional_info_id = len(database["nutritional_info"]) + 1
    database["nutritional_info"][nutritional_info_id] = nutritional_info_dict
    config.save_database(database)
    return nutritional_info

def read_nutritional_info(recipe_id: int):
    database = config.load_database()
    return database["nutritional_info"].get(recipe_id)

def update_nutritional_info(recipe_id: int, nutritional_info: NutritionalInfo):
    database = config.load_database()
    if recipe_id in database["nutritional_info"]:
        database["nutritional_info"][recipe_id] = nutritional_info.dict()
        config.save_database(database)
        return True
    return False

def delete_nutritional_info(recipe_id: int):
    database = config.load_database()
    if recipe_id in database["nutritional_info"]:
        del database["nutritional_info"][recipe_id]
        config.save_database(database)
        return True
    return False

# Search and filter operations for recipes
def search_recipes_by_title(title: str):
    database = config.load_database()
    recipes = []
    for recipe in database["recipes"]:
        if title.lower() in recipe["title"].lower():
            recipes.append(recipe)
    return recipes

def filter_recipes_by_ingredient(ingredient: str):
    database = config.load_database()
    recipes = []
    for recipe in database["recipes"]:
        for ing in recipe["ingredients"]:
            if ingredient.lower() in ing["name"].lower():
                recipes.append(recipe)
                break
    return recipes

def filter_recipes_by_nutritional_info(min_calories: int = None, max_calories: int = None,
                                       min_fat: int = None, max_fat: int = None,
                                       min_protein: int = None, max_protein: int = None,
                                       min_carbs: int = None, max_carbs: int = None):
    database = config.load_database()
    recipes = []
    for recipe in database["recipes"]:
        if min_calories is not None and recipe["nutritional_info"]["calories"] < min_calories:
            continue
        if max_calories is not None and recipe["nutritional_info"]["calories"] > max_calories:
            continue
        if min_fat is not None and recipe["nutritional_info"]["fat"] < min_fat:
            continue
        if max_fat is not None and recipe["nutritional_info"]["fat"] > max_fat:
            continue
        if min_protein is not None and recipe["nutritional_info"]["protein"] < min_protein:
            continue
        if max_protein is not None and recipe["nutritional_info"]["protein"] > max_protein:
            continue
        if min_carbs is not None and recipe["nutritional_info"]["carbs"] < min_carbs:
            continue
        if max_carbs is not None and recipe["nutritional_info"]["carbs"] > max_carbs:
            continue
        recipes.append(recipe)
    return recipes

def filter_recipes_by_dietary_preferences(vegetarian: bool = False, gluten_free: bool = False):
    database = config.load_database()
    recipes = []
    for recipe in database["recipes"]:
        if vegetarian and not is_vegetarian(recipe):
            continue
        if gluten_free and not is_gluten_free(recipe):
            continue
        recipes.append(recipe)
    return recipes

# Helper functions for dietary preferences
def is_vegetarian(recipe):
    for ingredient in recipe["ingredients"]:
        if "meat" in ingredient["name"].lower():
            return False
    return True

def is_gluten_free(recipe):
    for ingredient in recipe["ingredients"]:
        if "gluten" in ingredient["name"].lower():
            return False
    return True