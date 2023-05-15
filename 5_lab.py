import random

random_numbers = [random.randint(1, 10) for i in range(5)]
print('случайно сгенерированный список - ' + str(random_numbers))

r_n = int(input('Введите случайное число - '))

if r_n in random_numbers:
    print('Поздравляю, вы угадали число: ' + str(r_n))
else:
    print('Нет такого числа, правильные числа - ' + str(random_numbers))
def d1():
    days = ('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Суб', 'Вс')
    days_off = int(input('Сколько выходных ты хочешь?'))
    print('твои выходные:',*days[len(days)-days_off:])
    print('твои рабочие дни:', *days[:len(days)-days_off] )
def d2_1():
    k = 0
    list = [2, 7, 12, 22, 26, 17, 7]
    for i in list:
        if list.count(i) > 1 and i != k:
            print("Найдено повторяющиеся число: ", i)
            k = i


def d2():
    group1 = ["Машичев", "Дюбарев", "Аленик", "Ковалев", "Сайкал", "Дубовец", "Абадовский ", "Шапран", "Нуримов",
              "Фаттахов "]
    group2 = ["Рузвельт ", "Черчель", "Сталин", "Ленин", "Попов", "Иванов", "Ельцин ", "Балабанов", "Яковлев",
              "Гаврилов"]
    team = tuple(group1[:5] + group2[:5])
    print("Группа 1:", group1)
    print("Группа 2:", group2)
    print("Команда:", team)
    print("Длина кортежа:", len(team))
    sorted_team = sorted(team)
    print("Команда (отсортирована по алфавиту):", sorted_team)
    ivanov_count = team.count("Иванов")
    if ivanov_count > 0:
        print("Фамилия Иванов входит в команду. Встречается:", ivanov_count, "раз(а)")
    else:
        print("Фамилия Иванов не входит в команду")



d1(),d2_1(),d2()