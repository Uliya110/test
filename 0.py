cook_book = {}

with open('recipes.txt', encoding='utf-8') as f:

    while True:
        dish_name = f.readline()
        if not dish_name:
            break  # файл закончился

        dish_name = dish_name.strip()
        if not dish_name:
            continue  # пропускаем пустые строки

        ingredients_count = int(f.readline().strip())
        ingredients = []

        for _ in range(ingredients_count):
            line = f.readline().strip()
            ingredient_name, quantity, measure = line.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })

        cook_book[dish_name] = ingredients

print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish not in cook_book:
            print(f'Блюда "{dish}" нет в cook_book')
            continue

        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']

            if name not in shop_list:
                shop_list[name] = {
                    'measure': measure,
                    'quantity': quantity
                }
            else:
                shop_list[name]['quantity'] += quantity

    return shop_list
dishes_input = input('Введите список блюд через запятую:\n')
person_count = int(input('Введите количество персон:\n'))
dishes = [d.strip() for d in dishes_input.split(',')]
result = get_shop_list_by_dishes(dishes, person_count)
print(result)
print('status')
print('duble change')
print('Новая попытка')





