print('1 задание')
countries = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                 "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                 "Северная Македония": "Скопье", "Сербия": "Белград"}
print("Страны - столицы : ")
for country, capital in countries.items():
    print(country, ":", capital)
country = input("Введите название страны: ")

if country in countries:
    print("Столица", country, ":", countries[country])
else:
    print("Страна", country, "не найдена")
print("Отсортированный список страна + столица : ")
for country, capital in sorted(countries.items()):
    print(country, ":", capital)
def d1_1():
    print("Нормальное решение 2 задания : ")
    letters_values = {
        "А": 1,
        "Б": 3,
        "В": 1,
        "Г": 3,
        "Д": 2,
        "Е": 1,
        "Ё": 3,
        "Ж": 5,
        "З": 5,
        "И": 1,
        "Й": 4,
        "К": 2,
        "Л": 2,
        "М": 2,
        "Н": 1,
        "О": 1,
        "П": 2,
        "Р": 1,
        "С": 1,
        "Т": 1,
        "У": 2,
        "Ф": 10,
        "Х": 5,
        "Ц": 5,
        "Ч": 5,
        "Ш": 8,
        "Щ": 10,
        "Ъ": 10,
        "Ы": 4,
        "Ь": 3,
        "Э": 8,
        "Ю": 8,
        "Я": 3
    }

    word = input("Введите слово: ").upper()
    point = 0
    for letter in word:
        point += letters_values[letter]

    print("Стоимость слова", word, ":", point, "очков")


def d2():
    print("2 задание")
    word = input("Введите слово: ").upper()

    points = 0
    for letter in word:
        if letter in "АВЕИНОРСТ":
            points += 1
        elif letter in "ДКЛМПУ":
            points += 2
        elif letter in "БГЁЬЯ":
            points += 3
        elif letter in "ЙЫ":
            points += 4
        elif letter in "ЖЗХЦЧ":
            points += 5
        elif letter in "ШЭЮ":
            points += 8
        elif letter in "ФЩЪ":
            points += 10

    print(f"Строимость слова {word}: {points}"," очков")
def d3():
    print("доп зад")

    languages = set()
    chinese_speakers = []
    students = {'Илья': {'Англиский', 'Китайский', 'Русский'},
                'Вадим': {'Англиский', 'Французкий'},
                'Глеб': {'Китайский', 'Японский'},
                'Валерий': {'Китайский', 'Русский'},
                'Сергей': {'Немецкий', 'Русский', 'Китайский'}}

    for student, lang in students.items():
        languages.update(lang)
        if 'Китайский' in lang:
            chinese_speakers.append(student)

    sorted_languages = sorted(list(languages))

    print(sorted_languages)
    print(chinese_speakers)
d2(), d1_1(), d3()