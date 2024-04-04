from pydantic import BaseModel, Field
from typing import List, Annotated

class NutritionalInfo(BaseModel):
    calories: Annotated[float, Field(gt=0)]
    fat: Annotated[float, Field(ge=0)]
    protein: Annotated[float, Field(ge=0)]
    carbs: Annotated[float, Field(ge=0)]

class Ingredient(BaseModel):
    name: str
    quantity: Annotated[float, Field(gt=0)]
    unit: str

class Recipe(BaseModel):
    id: int
    title: str
    description: str
    instructions: str
    ingredients: List[Ingredient]
    nutritional_info: NutritionalInfo