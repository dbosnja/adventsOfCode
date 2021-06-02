#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/21#part2


def get_food(file_path):
    """read the input file

    :param file_path: file path to input file --> str
    :rtype: dict
    """
    food_map = {}
    with open(file_path) as f:
        for line in f:
            food = line.strip()
            if "contains" not in food:
                food_map[line.split(" ")] = ()
            else:
                ingredient_list, allergen_list = food.split("(contains")
                ingredient_list = ingredient_list.strip().split(" ")
                allergen_list = allergen_list.strip(" )").split(", ")
                food_map[tuple(ingredient_list)] = tuple(allergen_list)
    return food_map


def get_unique_mapper(ingredient_allergent):
    """

    :param ingredient_allergent: represents system of linear equations --> dict
    :rtype: dict
    """
    unique_mapper = {}
    while True:
        if not ingredient_allergent: break
        for key in list(ingredient_allergent.keys()):
            if len(key) == 1:
                unique_mapper[key[0]] = ingredient_allergent[key]
                del ingredient_allergent[key]
                ingredient_allergent = update_mapper(key[0], ingredient_allergent)
            continue
    return unique_mapper


def update_mapper(ingredient, ingredient_allergent):
    """iterate over mapper once and delete all occurrences of ingredient

    :param ingredient: str
    :param ingredient_allergent: dict
    :rtype: dict
    """
    for key in list(ingredient_allergent.keys()):
        if ingredient in key:
            temp_key = [it for it in
            ' '.join(key).replace(ingredient, "").split(" ") if it.strip()]
            new_key = tuple(temp_key)
            ingredient_allergent[new_key] = ingredient_allergent[key]
            del ingredient_allergent[key]
    return ingredient_allergent


def get_number(unique_mapper, food_map):
    """extract all ingredients which don't contain any allergen
       and count them all

    :param unique_mapper: dict
    :param food_map: dict
    :rtype: int
    """
    all_of_them = []
    for key in food_map:
        temp_ingred = list(key)
        for unique_key in unique_mapper.keys():
            if unique_key not in temp_ingred: continue
            temp_ingred.remove(unique_key)
        all_of_them.extend(temp_ingred)
    return len(all_of_them)


def main():
    file_path = "input.txt"
    food_map = get_food(file_path)
    # data loaded
    all_allergens = set()
    ingredient_allergent = {}
    for allergens in food_map.values():
        for allergen in allergens:
            all_allergens.add(allergen)
    for allergen in all_allergens:
        potential_ingr = set()
        for ingr, allrg in food_map.items():
            if allergen not in allrg: continue
            if not potential_ingr:
                potential_ingr = set(ingr)
            else:
                # there was already a hit, intersect it
                potential_ingr = potential_ingr.intersection(set(ingr))
        ingredient_allergent[tuple(potential_ingr)] = allergen
    unique_mapper = get_unique_mapper(ingredient_allergent)
    return ','.join(sorted(unique_mapper, key=unique_mapper.get))

if __name__ == "__main__":
    print(main())
