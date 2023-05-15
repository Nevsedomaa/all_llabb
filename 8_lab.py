from PIL import Image, ImageDraw, ImageFont
from termcolor import colored

image = Image.open("test.jpeg")
area = (0, 0, 500, 500)
cropped_img = image.crop(area)
cropped_img.save("cropped_img.jpg")

def d2():
    card_dict = {
        "др": "birthday.jpg",
        "нг": "new_year.jpg",
        "8м": "8.jpg",
        "23ф": "23.jpg"

    }

    holiday = input("Введите название праздника: ")
    if holiday not in card_dict:
        print("Открытка не найдена")
    else:
        card_file = card_dict[holiday]
        card_image = Image.open(card_file)
        card_image.show()
d2()

def d3():
    name = input("Введите имя получателя: ")
    image = Image.open("1.jpg")

    text_area = (50, 50, 450, 450)

    draw = ImageDraw.Draw(image)
    text = f"{name}, поздравляю!"

    font_size = 60
    font_type = "arial_bold.ttf"
    font = ImageFont.truetype(font_type, font_size,)
    draw.text((125, 10), text, font=font, fill=(255, 0, 0))
    image.show()
    image.save("pick.png")
d3()

