'''
# Created by Mark Davies
# 
# Email: mark@mandppcs.co.uk 
# 
# Licensed under the MIT License.
# 
# Version 0.1
'''
import PIL
from PIL import Image
import threading
import glob
import os

class ResizeImage():

    def __init__(self, width, height):
        self.Image = None
        self.Running = False
        self.Width = width
        self.Height = height
        self.Size = [self.Width, self.Height]

    def Run(self, dir):
        for infile in glob.glob(dir + "/*.jpg"):
            file, ext = os.path.splitext(infile)
            if not file.__contains__("thumbnail"):
                self.Resize(infile, file, ext)

    # run in thread every x seconds to look in a specific folder
    def Resize(self, infile, file, ext):
        im = Image.open(infile)
        im.thumbnail(self.Size)
        im.save(file + ".thumbnail" + ext, "JPEG")

def main():
    res = ResizeImage(200, 100)
    res.Run('C:\\Temp\Pics')

if __name__ == '__main__':
    main()


