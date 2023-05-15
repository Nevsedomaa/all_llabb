def d3(number):
    try:
        if int(number) % 3 == 0:
            a = int(number)//3
            print("Делится,","ваш ответ -",a)
        else:
            print("Не делится")
    except:
        print("Вы ввели что-то не то")

d3(input("Введите число, которое нужно делить  на 3: "))

def d4(number):
    try:
        a = 100/int(number)
    except ValueError:
        print("Вы ввели не число")
    except ZeroDivisionError:
        print("На 0 делить нельзя")
    else:
        print(100 / int(number))

d4(input("Введите делитель для 100: "))
def d5(date):
    try:
        if int(date.split(".")[0]) > 12 or int(date.split(".")[1]) > 12 or int(date.split(".")[1]) < 1 or int(date.split(".")[0]) < 1:
            return "Вы неправильно ввели дату или месяц"
        else:
            if int(date.split(".")[0]) * int(date.split(".")[1]) == int(date.split(".")[2][2:]):
                return True
            else:
                return False
    except:
        return "Вы ввели дату неправильно "
print(d5(input("Введите дату: ")))

def d6(num):
    try:
        sum1 = 0
        sum2 = 0
        for i in num[:int(len(num) / 2)]:
            sum1 += int(i)
        for j in num[int(len(num) / 2):]:
            sum2 += int(j)
        if sum1 == sum2:
            print("У вас счастливый билетик")
        else:
            print("У вас несчастливый билетик")
    except:
        print("Вы ввели что-то не то")

d6(input("Введите номер билетика: "))