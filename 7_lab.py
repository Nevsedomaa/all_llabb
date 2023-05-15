
from PIL import Image, ImageFilter
import os

image = Image.open('image.jpg')
image.show()

print("Размер изображения:", image.size)
print("Формат изображения:", image.format)
print("Цветовая модель:", image.mode)
def d1():
    image = Image.open('image.jpg')
    image.show()

    new_size = (image.width // 3, image.height // 3)
    image.thumbnail(new_size)
    image.show()
    image.save('image_3x.jpg')


    mirror_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    mirror_image.show()
    mirror_image.save('image_mirror.jpg')

    rotate_image = image.rotate(180)
    rotate_image.show()
    rotate_image.save('image_rotate.jpg')
d1()
def d2():

    os.mkdir('output')

    for i in range(1, 6):
        filename = f'{i}.jpg'
        input_img = Image.open(filename)

        output_img = input_img.filter(ImageFilter.CONTOUR)

        new_filename = f'output/{i}_contour.jpg'
        output_img.save(new_filename)
d2()
def d3():
    background = Image.open("background.jpg")
    foreground = Image.open("foreground.png")
    background.show()

    background.paste(foreground, (100, 100), foreground)
    background.show()
    background.save("result.png")
d3()