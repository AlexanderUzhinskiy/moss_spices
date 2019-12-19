##import numpy as np
##from skimage import io, color
##from skimage.transform import resize
##
##rgb = io.imread("E:/Progams-Engineering/Python/PythonOpenCvmine/mine/JINR - Machine Learning/2/search-bing-api/dataset/Abietinella_abietina/crop")
### show original image
##img = Image.fromarray(rgb, 'RGB')
##img.show()
##
##rgb = resize(rgb, (256, 256))
### show resized image
##img = Image.fromarray(rgb, 'RGB')
##img.show()

##
##from PIL import Image
##import os, sys
##
##path = ('E:/Progams-Engineering/Python/PythonOpenCvmine/mine/JINR - Machine Learning/2/search-bing-api/dataset/Abietinella_abietina/crop')
##dirs = os.listdir( path )
##
##def resize():
##    for item in dirs:
##        if os.path.isfile(path+item):
##            im = Image.open(path+item)
##            f, e = os.path.splitext(path+item)
##            imResize = im.resize((256,256), Image.ANTIALIAS)
##            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)
##
##resize()


import os
from PIL import Image
resize_method = Image.ANTIALIAS
    #Image.NEAREST)  # use nearest neighbour
    #Image.BILINEAR) # linear interpolation in a 2x2 environment
    #Image.BICUBIC) # cubic spline interpolation in a 4x4 environment
    #Image.ANTIALIAS) # best down-sizing filter


max_height= 256
max_width= 256
extensions= ['JPG']

path= os.path.abspath(".")

def adjusted_size(width,height):
    if width>max_width or height>max_height:
        if width>height:
            return max_width, int (max_width * height/ width)
        else:
            return int (max_height*width/height), max_height
    else:
        return width,height

	
if __name__ == "__main__":
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path,f)):
            f_text, f_ext= os.path.splitext(f)
            f_ext= f_ext[1:].upper()
            if f_ext in extensions:
                image = Image.open(os.path.join(path,f))
                width, height= image.size
                print (f, image.size)
                image = image.resize(adjusted_size(width, height))
                if image.size==(256,256):
                    print("Ok")
                if image.size!=(256,256):
                    print("Nooooooo, Please adjust me")
                image.save(os.path.join(path,f))
