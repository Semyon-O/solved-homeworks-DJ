from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'carbonara': {
        'ветчина, г': 500,
        'сыр, г': 100,
        'яйцо, шт': 1,
        'макароны, г': 200,
        'сливки, г': 100
    }
}


def show_recipe_dish(request, dish):
    template = 'calculator/index.html'
    recipe_dish = DATA.get(dish, None)

    if recipe_dish is None:
        return render(request, template, context={'recipe': None})

    amount = request.GET.get('servings', 1)

    result = {}

    for recipe, product in enumerate(recipe_dish):
        result[product] = recipe_dish[product] * float(amount)

    context = {
        'recipe': result
    }

    return render(request, template, context=context)

