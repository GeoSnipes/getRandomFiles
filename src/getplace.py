"""Note, this was built taking into account the base input folder only contains other folders """
import os
from random import randint
from shutil import copy2

def getFiles(directory):
    count = 0
    files = os.listdir(directory)
    while count < 3:
        randomNum = randint(0, len(files)-1)
        copy2(directory + "\\" + files[randomNum],"D:\\Users\\Geovanni\\Downloads\\food-101.tar\\food-101\\food")
        count+=1


path = "D:\\Users\\Geovanni\\Downloads\\food-101.tar\\food-101\\images" #hardcoded here, use sys.argv or your own implementation to be more dynamic
for folder in os.listdir(path):
    getFiles(path+"\\"+folder)