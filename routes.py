from fastapi import APIRouter, HTTPException, Query
from models import Recipe, Ingredient, NutritionalInfo
from services import create_recipe, read_recipe, update_recipe, delete_recipe, \
                     create_ingredient, read_ingredient, update_ingredient, delete_ingredient, \
                     create_nutritional_info, read_nutritional_info, update_nutritional_info, delete_nutritional_info, \
                     search_recipes_by_title, filter_recipes_by_ingredient, filter_recipes_by_nutritional_info, \
                     filter_recipes_by_dietary_preferences

router = APIRouter()

# Recipe Endpoints
@router.post("/recipes/")
async def create_new_recipe(recipe: Recipe):
    if recipe.nutritional_info:
        nutritional_info = create_nutritional_info(recipe.nutritional_info)
        recipe.nutritional_info_id = nutritional_info.id
    for ingredient in recipe.ingredients:
        create_ingredient(ingredient)
    return create_recipe(recipe)

@router.get("/recipes/{recipe_id}")
async def get_recipe(recipe_id: int):
    recipe = read_recipe(recipe_id)
    if recipe:
        return recipe
    else:
        raise HTTPException(status_code=404, detail="Recipe not found")

@router.put("/recipes/{recipe_id}")
async def update_existing_recipe(recipe_id: int, recipe: Recipe):
    # Update nutritional info if provided
    if recipe.nutritional_info:
        update_nutritional_info(recipe.nutritional_info_id, recipe.nutritional_info)
    # Update ingredients if provided
    for ingredient in recipe.ingredients:
        update_ingredient(ingredient.id, ingredient)
    return update_recipe(recipe_id, recipe)

@router.delete("/recipes/{recipe_id}")
async def delete_existing_recipe(recipe_id: int):
    # Delete nutritional info if exists
    nutritional_info = read_nutritional_info(recipe_id)
    if nutritional_info:
        delete_nutritional_info(recipe_id)
    return delete_recipe(recipe_id)

# Ingredient Endpoints
@router.post("/ingredients/")
async def create_new_ingredient(ingredient: Ingredient):
    return create_ingredient(ingredient)

@router.get("/ingredients/{ingredient_id}")
async def get_ingredient(ingredient_id: int):
    ingredient = read_ingredient(ingredient_id)
    if ingredient:
        return ingredient
    else:
        raise HTTPException(status_code=404, detail="Ingredient not found")

@router.put("/ingredients/{ingredient_id}")
async def update_existing_ingredient(ingredient_id: int, ingredient: Ingredient):
    if update_ingredient(ingredient_id, ingredient):
        return {"message": "Ingredient updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Ingredient not found")

@router.delete("/ingredients/{ingredient_id}")
async def delete_existing_ingredient(ingredient_id: int):
    if delete_ingredient(ingredient_id):
        return {"message": "Ingredient deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    

# Search and Filtering Endpoints
@router.get("/recipes/search/")
async def search_recipes_by_title(title: str):
    recipes = search_recipes_by_title(title)
    if recipes:
        return recipes
    else:
        raise HTTPException(status_code=404, detail="No recipes found")

@router.get("/recipes/filter/")
async def filter_recipes_by_ingredients(ingredient: str = Query(None)):
    recipes = filter_recipes_by_ingredient(ingredient)
    if recipes:
        return recipes
    else:
        raise HTTPException(status_code=404, detail="No recipes found")

@router.get("/recipes/filter/nutritional/")
async def filter_recipes_by_nutritional_info(
    min_calories: int = Query(None, gt=0),
    max_calories: int = Query(None, gt=0),
    min_fat: int = Query(None, ge=0),
    max_fat: int = Query(None, ge=0),
    min_protein: int = Query(None, ge=0),
    max_protein: int = Query(None, ge=0),
    min_carbs: int = Query(None, ge=0),
    max_carbs: int = Query(None, ge=0)
):
    recipes = filter_recipes_by_nutritional_info(
        min_calories=min_calories,
        max_calories=max_calories,
        min_fat=min_fat,
        max_fat=max_fat,
        min_protein=min_protein,
        max_protein=max_protein,
        min_carbs=min_carbs,
        max_carbs=max_carbs
    )
    if recipes:
        return recipes
    else:
        raise HTTPException(status_code=404, detail="No recipes found")