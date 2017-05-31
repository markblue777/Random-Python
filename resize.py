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
import time

class ResizeImage():

    def __init__(self, width, height):
        self.Image = None
        self.Running = False
        self.Width = width
        self.Height = height
        self.Size = [self.Width, self.Height]
        self.ScanningThread = None

    def Run(self, dir):
        self.ScanningThread = threading.Thread(target=self.ScanDir, args=[dir])
        self.ScanningThread.daemon = True
        self.ScanningThread.start()

        while True:
            pass

    def ScanDir(self, dir):
        while True:
            for infile in glob.glob(dir + "/*.jpg"):
                file, ext = os.path.splitext(infile)
                if not file.__contains__("thumbnail"):
                    self.Resize(infile, file, ext)

            # sleep the thread so it scans the folder every second
            time.sleep(1)
            print('Scanning Folder')

    def Resize(self, infile, file, ext):
        im = Image.open(infile)
        im.thumbnail(self.Size)
        im.save(file + ".thumbnail" + ext, "JPEG")

def main():
    res = ResizeImage(200, 100)
    res.Run('C:\\Temp\Pics')

if __name__ == '__main__':
    main()


