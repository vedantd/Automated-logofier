# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 12:10:40 2017

@author: Vedant Dalvi
"""

from os import listdir
import PIL.Image
import PIL.ImageEnhance
y=100



dirListing = listdir(r"C:/Users/vedan/Desktop")  #enter directory/folder of the photos you want to add logo to.

editFiles = []                                   #creates list which will fill up with all images from specified directory above.

for item in dirListing:                          #loops through directory and fills list with .JPG (specify according to user) .   
    if (".jpg") in item:
        editFiles.append(item)
print (editFiles)
print (len(editFiles))

for i in range (0, len(editFiles)):              #performs  action on the photos in list
    # images
    
    base_path = editFiles[i]                    #pass image files in list to variable base_path
    
    watermark_path ='ieee.png'                  #sepecify the path of the ieee logo here. 
    
    watermark_path2 = 'vitlogo.png'             #specify the path of the vit logo here.
    base = PIL.Image.open(base_path)            
    width, height= base.size
    watermark = PIL.Image.open(watermark_path)  #opens watermark and pass to watermark variable
    wat1width, wat1height= watermark.size
    
    watermark2 = PIL.Image.open(watermark_path2)  #opens second watermark and pass to watermark2 variable
    wat2width, wat2height= watermark2.size

                                                   # optional lightness of watermark from 0.0 to 1.0
    brightness = 0.5
    watermark = PIL.ImageEnhance.Brightness(watermark).enhance(brightness)
    watermark2 = PIL.ImageEnhance.Brightness(watermark2).enhance(brightness)

    # apply the watermark
    
    some_xy_offset = (int(width/192), int(height/54))                      # x and y cood of ieee logo
    some_xy2_offset = (int(width-width/4)-15, 10)  #x and y cood of vit logo

    
    watermark=watermark.resize((int(width/9.66), int(height/7)))  #resizes logo image to maintain aspect ratio wrt main image(using  pixel ratios).
    watermark2=watermark2.resize((int(width/4),int(height/9.81)))
    
    # the mask uses the transparency of the watermark (if it exists)
    
    base.paste(watermark, some_xy_offset, mask=watermark)        #applies the logo 
    base.paste(watermark2, some_xy2_offset, mask=watermark2)     #applies the logo 
    
    base.save('ycpics/ImageWithLogo'+ str(y)+ '.JPG')                    #name+ someNumber of saved image
    #base.show()                                                   #display each image
    y=y+1

base.show()