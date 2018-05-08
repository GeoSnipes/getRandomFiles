"""Note, this was built taking into account the base input folder only contains other folders """
"""Take a subset of files within a sub directory"""
import os
from random import randint
from shutil import copy2, move
import folder_paths

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


base = folder_paths.getplacePATH1 #hardcoded here, use sys.argv or your own implementation to be more dynamic
for folder in os.listdir(base+"\\images"):
    getFiles(base, base+"\\images\\"+folder,folder)