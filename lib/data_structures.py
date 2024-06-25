spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = []
    for food in spicy_foods:
        food_names.append(food["name"])
    return food_names
        
def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods: 
        if (food['heat_level'] > 5):
            spiciest_foods.append(food)
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods: 
        heat_level = food['heat_level']
        food_name = food['name']
        food_cuisine = food['cuisine']
        emoji_items = "🌶" * heat_level
        print(f"{food_name} ({food_cuisine}) | Heat Level: {emoji_items}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods: 
        if cuisine == food["cuisine"]:
            return food
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods: 
        heat_level = food['heat_level']
        food_name = food['name']
        food_cuisine = food['cuisine']
        emoji_items = "🌶" * heat_level
        if (food['heat_level'] > 5):
            print(f"{food_name} ({food_cuisine}) | Heat Level: {emoji_items}")
    pass

def get_average_heat_level(spicy_foods):
    heat_values = []
    for food in spicy_foods:
        heat_values.append(food['heat_level'])
        heat_sum = sum(heat_values)
    return (heat_sum / len(spicy_foods))
    pass

def create_spicy_food(spicy_foods, spicy_food):
        spicy_foods.append(spicy_food)
        return spicy_foods