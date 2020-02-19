#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  current_min = float("inf")
  for key in recipe:
    if key in ingredients:
      if (ingredients[f"{key}"]//recipe[f"{key}"]) < current_min:
        current_min = (ingredients[f"{key}"]//recipe[f"{key}"])
    else:
      return 0
  return current_min

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))