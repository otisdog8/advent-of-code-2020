import os
import random

fole = open("Fuck_You.png", "rb")
data = fole.read()
path = input("Enter your folder path:  ")
os.mkdir(os.getcwd() + "/" + path)


def generate_name():
    name = "Fuck_You"
    parts = random.randint(2, 10)
    for i in range(parts):
        game = random.randint(0, 2)
        if game == 0:
            name += "_-_"
        elif game == 1:
            name += "_Copy_" + str(random.randint(1, 1024)) + " "
        elif game == 2:
            name += " (" + str(random.randint(1, 1024)) + ")_"
    name += ".png"
    return name


for i in range(1024):
    fele = open(path + generate_name(), "wb")
    fele.write(data)
