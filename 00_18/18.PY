#!/usr/bin/env python
__author__ = "Sreenivas Bhattiprolu"
__license__ = "Feel free to copy, I appreciate if you acknowledge Python for Microscopists"

# https://www.youtube.com/watch?v=uDNqNv2N-pY&t=

#prints current directory 
import os
print(os.getcwd()) 
#check if it exist 
import os
print(os.path.exists("..\\images\\test_image.jpg"))


#Actual program -->show image,#Reading images
from PIL import Image
img = Image.open(r"..\images\test_image.jpg") #used raw string,r" is important so, instead of /i(esc chr), /t "test_image.jpg" becomes "test mage.jpg lol
print(type(img))
img.show() 
 
# prints format of image 
print(img.format) 
  
# prints mode of image RGB or CMYK
print(img.mode) 

print(img.size)  #prints the size of image (width, height)


#####################################################################
# Resize images
from PIL import Image
img = Image.open(r"..\images\test_image.jpg")
resize00_img = img.resize((200, 300))
resize00_img.save(r"..\images\test_image_resize.jpg")  #squished image

print(resize00_img.size)

# resize() method resizes images to exact value whether it makes sense or not.
#aspect ratio is not maintained so images are squished.
#if you want to keep the aspect ration then use thumbnail() method
from PIL import Image
img = Image.open(r"..\images\test_image.jpg")
img.thumbnail((200, 200))
img.save(r"..\images\test_imagethumbnail_new.jpg")

print(img.size)

img.thumbnail((1200, 1200))  #doesn't blow up the image, only reduces the size if original is larger.
img.save(r"..\images\test_image00thumbnail.jpg")  

large_img = img.resize((1200, 1300))
large_img.save(r"..\images\test_image01thumbnail.jpg")  #enlarged image. 
print(large_img.size)

#Cropping images
from PIL import Image 
img = Image.open(r"..\images\test_image.jpg")
cropped_img = img.crop((0, 0, 300, 300))  #crops from (0,0) to (300,300)
cropped_img.save(r"..\images\test_imagecropped.jpg")

# We can paste image on another image
#this involves copying original image and pasting a second image on it
from PIL import Image 
img1 = Image.open(r"..\images\test_image.jpg")
print(img1.size)
img2 = Image.open(r"..\images\monkey.jpg")
print(img2.size)
img2.thumbnail((200, 200))  #Resize in case the image is very large. 
img2.show()
img1.show()

img1_copy = img1.copy()   #Create a copy of the large image
img1_copy.paste(img2, (0, 0))  #Paset the smaller imager image at specified location 
img1_copy.save(r"python_for_microscopists\images\test_imagepasted_image.jpg")
img1_copy.show()

# Rotating images
from PIL import Image 
img = Image.open(r"python_for_microscopists\images\test_image.jpg")

img_90_rot = img.rotate(90)
img_90_rot.save(r"python_for_microscopists\images\rotated90.jpg")  #keeps original aspect ratio and dimensions
img_45_rot.show()

img_45_rot = img.rotate(45)
img_45_rot.save(r"python_for_microscopists\images\rotated45.jpg")  #keeps original aspect ratio and dimensions
img_45_rot.show()

img_45_rot = img.rotate(45, expand=True)  #Dimensions are expanded to fir the entire image
img_45_rot.save(r"python_for_microscopists\images\rotated45.jpg")  


#Flipping or transposing images

from PIL import Image 
img = Image.open(r"python_for_microscopists\images\monkey.jpg")  #easy to see that the image is flipped
img_flipLR = img.transpose(Image.FLIP_LEFT_RIGHT)
img_flipLR.save(r"python_for_microscopists\images\monkeyflipped.jpg")
img_flipLR.show()

img_flipTB = img.transpose(Image.FLIP_TOP_BOTTOM)
img_flipTB.save(r"python_for_microscopists\images\monkeyflippedTB.jpg")
img_flipTB.show()

# Color transforms, convert images between L (greyscale), RGB and CMYK
from PIL import Image 
img = Image.open(r"python_for_microscopists\images\test_image.jpg")

grey_img = img.convert('L')  #L is for grey scale
grey_img.save(r"python_for_microscopists\images\testgrey_img.jpg")
grey_img.show()

# Many other tasks can be performed. Here is full documentation.
# https://pillow.readthedocs.io/en/stable/reference/Image.html


#Here is a way to automate image processing for multiple images.

from PIL import Image 
import glob

path = "python_for_microscopists\images\test_images\aeroplane/*.*"
for file in glob.glob(path):
    print(file)     #just stop here to see all file names printed
    a= Image.open(file)  #now, we can read each file since we have the full path
    
    rotated45 = a.rotate(45, expand=True)
    rotated45.save(file+"_rotated45.png", "PNG")   













