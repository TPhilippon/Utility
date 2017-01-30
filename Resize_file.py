#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 22:24:26 2017

@author: terencephilippon
"""

from PIL import Image
import os

path = "/Users/terencephilippon/Desktop/Dossier_MM_files/ToCrop/PACA2010_Sante/"
outpath = "/Users/terencephilippon/Desktop/Dossier_MM_files/Out/PACA2010_Sante/"
top = 260
left = 125
w = 800
h = 600

for myfile in os.listdir(path):
    
    if myfile[0:1] != '.':
        print myfile
        file_name = myfile
        myfile = Image.open(path+myfile)
    #    w, h = myfile.size
        cropped = myfile.crop((left, top, w-left, h+top))
#       cropped.show()
        cropped.save(outpath+'crop'+str(file_name), "PNG")
    
#w, h = yourImage.size
#yourImage.crop((0, 30, w, h-30)).save(...)