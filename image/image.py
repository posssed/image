from PIL import Image
from PIL import ImageFilter

with Image.open("life.jpg") as original:
    print("Розмір зображення: ", original.size)
    print("Формат зображення: ", original.format)
    print("Колірний тип: ", original.mode)

    # black_white = original.convert("L")
    # black_white.save("black_white.jpg")

    # blurimg = original.filter(ImageFilter.BLUR)
    # blurimg.save("blur.jpg")

    # rotateimg = original.transpose(Image.ROTATE_270)
    # rotateimg.save("rotated.jpg")

    # mirrorimg = original.transpose(Image.FLIP_LEFT_RIGHT)
    # mirrorimg.save("mirror.jpg")

    box = (250, 100, 600, 400)
    crop = original.crop(box)
    crop.save("cropped.jpg")

    crop.show()
