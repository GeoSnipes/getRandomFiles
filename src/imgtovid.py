"""Take so images and stitch them together into a vid"""
import os
import folder_paths

os.chdir(folder_paths.imgtovidPATH1)

#windows:get all files ending with jpg and save in a text file
os.system("(for %i in (*.jpg) do @echo file '%i') > mylist.txt")

#take each image name in file and stitch all into a video, each image last .5 second
#os.system("ffmpeg -f concat -r 2 -i mylist.txt -vcodec mpeg4 -b 900k -y movie.mp4")
os.system(
    "ffmpeg -f concat -i mylist.txt -c:v libx264 -preset veryslow -crf 0 output.mkv"
)
