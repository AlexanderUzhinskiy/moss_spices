# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials
import requests
from requests import exceptions
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFile
from io import StringIO
import io  # Note: io.BytesIO is StringIO.StringIO on Python2.
from datetime import datetime
from os import mkdir, path, listdir
from os.path import join
import pandas as pd
from collections import defaultdict

ImageFile.LOAD_TRUNCATED_IMAGES = True  

subscription_key = "76003022336e40e58c6b33f57506396c"
page_size = 120

db_standard_dir = "moss-standard"
labels = sorted(listdir(db_standard_dir))
keywords = dict([( label,  open("{}/{}/{}".format(db_standard_dir,label, "keywords")).read().rstrip().split("\n")) \
                 for label in labels ])

# when attemping to download images from the web both the Python
# programming language and the requests library have a number of
# exceptions that can be thrown so let's build a list of them now
# so we can filter on them
EXCEPTIONS = set([IOError, FileNotFoundError,
	exceptions.RequestException, exceptions.HTTPError,
	exceptions.ConnectionError, exceptions.Timeout])
    
    
client = ImageSearchAPI(CognitiveServicesCredentials(subscription_key))

timenow = datetime.now().strftime("%Y%m%d-%H%M%S")
for label in labels :
    output_dir = label + "_" + timenow
    index = 1

    try:
        # Create target Directory
        mkdir(output_dir)
        print("Directory " , output_dir ,  " Created ") 
    except FileExistsError:
        print("Directory " , output_dir ,  " already exists")
            
    current_offset = 0
    while current_offset >= 0:
        query_exact = map( lambda word: '"{}"'.format(word) , keywords[label])
        query_exact_or = " | ".join( query_exact )
        image_results = client.images.search(query= query_exact_or, count = 120, offset = current_offset )
        current_count = len(image_results.value)
        print("Total number of images returned: {} ({}-{})".format(current_count, current_offset, current_offset + current_count))

        if current_count == page_size :
            current_offset += page_size
        else:
            current_offset = -1
            
        for query_img in image_results.value:	
            url = query_img.content_url
            try:
                r = requests.get(url, timeout = 10 )
                if r.status_code == 200:
                    img = Image.open(io.BytesIO(r.content)).convert('RGB')
                    img.save(path.join( output_dir , 'img_{:04}.jpg'.format(index)))
                    index = index + 1
            except requests.exceptions.Timeout:
                print("Timeout occurred ({}): {}".format( label , url ))
            except requests.exceptions.SSLError:
                print("SSL Error ({}): {}".format( label , url ))
            except IOError :
                print("IO Error ({}): {}".format( label , url ))

#fig=plt.figure(figsize=(8, 8))
#columns = 4
#rows = 5
#for i in range(1, columns*rows +1):
#    img = np.random.randint(10, size=(h,w))
#    fig.add_subplot(rows, columns, i)
#    plt.imshow(img)
#plt.show()    