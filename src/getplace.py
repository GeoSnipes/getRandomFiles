"""Note, this was built taking into account the base input folder only contains other folders """
import os
from random import randint
from shutil import copy2, move

def getFiles(base, source, folder):
    count = 0
    dest = base + "\\imagestest\\" + folder
    files = os.listdir(source)
    if not os.path.exists(dest):
        os.makedirs(dest)
    #takes 3 files from each folder
    while count < 3:
        randomNum = randint(0, len(files)-1)
        move(source + "\\" + files[randomNum], dest)    #or copy2 to copy
        count+=1


base = "D:\\Users\\Geovanni\\Downloads\\food-101.tar\\food-101" #hardcoded here, use sys.argv or your own implementation to be more dynamic
for folder in os.listdir(base+"\\images"):
    getFiles(base, base+"\\images\\"+folder,folder)