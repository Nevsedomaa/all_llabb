
N = int(input())
words = []
for i in range(N):
    words.append(input())
lg_st=" ".join(words)
print(lg_st)
def p1():
    word = str(input())
    words = " "
    while word != "stop":
        words += word + " "
        word = str(input())

    print(words)
def p2():
    while(word := str(input())) !="stop":
        if "ф" in word:
            print("Ого! Это редкое слово...")
        else:
            print("Эх, это не очень редкое слово...")

def p3():
    from random import randint
    h = 0
    pr_o = 0
    while h < 3:
        a = randint(1,100)
        b = randint(1,100)
        res = int(input(str(a) + '+' + str(b) + '='))
        if res != a+b:
            print("Ответ не верный")
            h+=1
        else:
            print("Правильно")
            pr_o+=1
    if h == 3:
        print("Игра окончена,правильных ответов-", pr_o)
p1(), p2(), p3()