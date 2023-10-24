from PIL import Image

im = Image.open("Images/some_picture.jpg")
print(im.format, im.size, im.mode)  # Выводит параметры изображения
im.rotate(45).show()  # Поворачивает изображение на 45 градусов и показывает его
