import os
import random

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

CAR_FOLDER_PATH = '../Images/car'
NON_CAR_FOLDER_PATH = '../Images/not_car'


class ImageGenarator:
    def __init__(self):
        self.car_photos = ImageGenarator.img_gen(CAR_FOLDER_PATH)
        self.not_car_photos = ImageGenarator.img_gen(NON_CAR_FOLDER_PATH)

    @staticmethod
    def img_gen(path):
        for file in os.listdir(path):
            file_in_folder = os.path.join(path, file)
            yield mpimg.imread(file_in_folder)

    def get_image(self):
        is_car = random.random() > .5
        if is_car:
            return next(self.car_photos), is_car
        else:
            return next(self.not_car_photos), is_car


gen = ImageGenarator()


def show_img():
    img, isCar = gen.get_image()
    plt.imshow(img)
    plt.show()

show_img()
show_img()
show_img()
show_img()
show_img()
show_img()
show_img()
show_img()