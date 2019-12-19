import os
from PIL import Image

extensions= ['JPG']
path= os.path.abspath(".")
if __name__ == "__main__":
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path,f)):
            f_text, f_ext= os.path.splitext(f)
            f_ext= f_ext[1:].upper()
            if f_ext in extensions:
                image = Image.open(os.path.join(path,f))
                width, height= image.size
                print (f, image.size)
                if image.size==(256,256):
                    print("Ok")
                if image.size!=(256,256):
                    print("Nooooooo, Please adjust me")
    
