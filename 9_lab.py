import os
from PIL import Image
import csv
print("9.1 and 9.2")
datadir = "D:\mashichev\pick"
processdir = os.path.join(datadir , "Обработано")

ListFiles = os.listdir(datadir)

if os.path.isdir(processdir) == False:
    os.mkdir(processdir)
count = 0
for  file in ListFiles:
    filename = os.path.join(datadir, file)

    if os.path.isfile(filename) and file.endswith('.png') or file.endswith('.jpg'):
        with Image.open(filename) as img:
            img.load()
            rotated_img = img.rotate(45)
            rotated_img.save(os.path.join(processdir, file))
            count +=1
print("Изображений обработано: ", count)
def d2():
    print("9.3")
    file_path ="D:\mashichev\qwer.csv"
    with open(file_path) as f:
        total_cost = 0
        print('Нужно купить: ')
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            product = row[0]
            quantity = int(row[1])
            prise = int(row[2])
            cost = quantity * prise
            total_cost += cost
            print(f'{product} - {quantity} шт за {prise} руб')
    print(f'Итоговая стоимость: {total_cost} руб')
d2()