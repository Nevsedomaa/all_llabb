people_1 = input("")
people_2 = input("")
if people_1 == people_2:
    print("Пароль принят")
else:
    print("Пароль не принят")

def p2():
    place = int(input(""))
    if place in range (1, 36):
        if place % 2 == 0:
            print("Верхнее место в купе")
        else:
            print("Место нижнее в купе")
    if place in range (37,54):
        if place % 2 == 0:
            print("Боковое верхнее")
        else:
            print("Боковое нижнее")
    if place in range (55, 1000):
        print("Ошибка")
def p3():
    year = int(input(""))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Год високосный")
    else:
        print("Год не високосный")

def p4():
    color_1 = input("Введите цвет (синий, красный, жёлтый) ")
    color_2 = input("Введите цвет (синий, красный, жёлтый) ")
    if color_1 == "красный" and color_2 == "синий" or color_1 == "синий" and color_2 == "красный":
        print("фиолетовый")
    elif color_1 == "красный" and color_2 == "жёлтый" or color_1 == "жёлтый" and color_2 == "красный" :
        print("оранжевый")
    elif color_1 == "синий" and color_2 == "жёлтый" or color_1 == "жёлтый" and color_ == "красный":
        print("зелёный")
    elif color_1 or color_2 != "красный" or "синий" or "жёлтый":
        print("Неправильный цвет")


p2(),p3(),p4()