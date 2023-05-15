import json
print(10.1 and 10.2)
with open('file.json',) as f:
    data = json.load(f)
    products = data['products']

    name = input("Введите название продукта:")
    price = int(input("Введите цену продукта:"))
    weight = int(input("Введите вес продукта:"))
    available = input("Доступен ли продукт?? (true/false):")

    new_prod = {
        'name': name,
        'price': price,
        'weight': weight,
        'available': available
    }

products.append (new_prod)

with open('file.json','w') as fw:
    json.dump(data,fw, ensure_ascii=False)

print("Информация о продуктах:")
print()
for prod in products:
    print(f"Название: {prod['name']}")
    print(f"Цена: {prod['price']}")
    print(f"Вес: {prod['weight']}")
    if prod['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()
def d1():
    en_ru_dict = {}
    with open('en-ru.txt') as f:
        for line in f:
            en_word, ru_words = line.strip().split(' - ')
            en_ru_dict[en_word] = ru_words.split(', ')

    ru_en_dict = {}
    for en_word, ru_words in en_ru_dict.items():
        for ru_word in ru_words:
            if ru_word in ru_en_dict:
                ru_en_dict[ru_word].append(en_word)
            else:
                ru_en_dict[ru_word] = [en_word]

    with open('ru-en.txt', 'w') as f:
        for ru_word in sorted(ru_en_dict):
            en_words = ', '.join(sorted(ru_en_dict[ru_word]))
            f.write(f"{ru_word} - {en_words}\n")
d1()