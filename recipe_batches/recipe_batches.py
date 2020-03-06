#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    arr = []
    for ingredient in recipe:
        if ingredient not in ingredients or ingredients[ingredient] < recipe[ingredient]:
            return 0
        # If enough, divide and appen to list
        else:
            check_amount = ingredients[ingredient] // recipe[ingredient]
            arr.append(check_amount)
    return min(arr)

    # recipe_batches(
    #   recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    # ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    # )


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
