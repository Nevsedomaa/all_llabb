import re
from functools import reduce
def PostNews(*args):
    init, news = args


    newsRang = int(news[0])


    MaxNewsRang = init['rang']


    if newsRang > MaxNewsRang:

        init.update({'rang': newsRang})

        init['posts'].append(news[1])

    return init


filename = "D:/1/news.txt"
with open(filename, 'r') as file:

    lines = file.read()


    listNews = []
    pattern = re.compile(r'([\d]+)\s*(.*)', re.M)
    listNews = pattern.findall(lines)

    res = reduce(PostNews, listNews, dict({'posts': [], 'rang': 0}))
    [print(value) for value in res['posts']]

