import os
os.chdir("D:\\Users\\Geovanni\\Downloads\\food-101.tar\\food-101\\food")

#windows:get all files ending with jpg and save in a text file
os.system("(for %i in (*.jpg) do @echo file '%i') > mylist.txt")

#take each image name in file and stitch all into a video, each image last .5 second
os.system("ffmpeg -f concat -r 2 -i mylist.txt -vcodec mpeg4 -b 900k -y movie.mp4")
