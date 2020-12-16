from random import choice
from os import listdir


def randomFile(dir = "lemurPhotos"):
    return dir + "/" + choice(listdir(dir))

print(randomFile())
