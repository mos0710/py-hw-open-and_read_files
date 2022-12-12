recipes = []
with open('recipes.txt', 'rt', encoding='utf-8') as file:
    menu = {}
    for line in file:
        dish_name = line[:-1]
        counter = file.readline().strip()
        list_of_ingredient = []
        for i in range(int(counter)):
            dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
            ingredient = file.readline().strip().split(' | ')
            for item in ingredient:
                dish_items['ingredient_name'] = ingredient[0]
                dish_items['quantity'] = ingredient[1]
                dish_items['measure'] = ingredient[2]
            list_of_ingredient.append(dish_items)
            cook_book = {dish_name: list_of_ingredient}
            menu.update(cook_book)
        file.readline()

def get_shop_list_by_dishes(dishes, persons=int):
    print('Ознакомьтесь с нашим меню :')
    print(menu)
    print()
    shopping_list = {}
    try:
        for dish in dishes:
            for item in (menu[dish]):
                items_list = dict([(item['ingredient_name'],
                                    {'measure': item['measure'], 'quantity': int(item['quantity']) * persons})])
                if shopping_list.get(item['ingredient_name']):
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                    int(items_list[item['ingredient_name']]['quantity']))
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item

                else:
                    shopping_list.update(items_list)

        print(f"Для приготовления блюд на {persons} человек  нам необходимо купить:")
        print(shopping_list)
    except KeyError:
        print("Вы ошиблись в названии блюда, проверьте ввод")

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)



