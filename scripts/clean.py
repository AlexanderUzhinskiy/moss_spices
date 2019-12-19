import hashlib
import imageio
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import os
os.getcwd()
def file_hash(filepath):
    with open(filepath, 'rb' ) as f:
        return md5(f.read()).hexdigest()
    
duplicates = []
hash_keys = dict()
for index, filename in enumerate(os.listdir('.')):
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
        if filehash not in hash_keys:
            hash_keys[filehash] = filename
        else: 
            duplicates.append((filename, hash_keys[filehash]))
            os.remove( filename )
            
            
# https://medium.com/@urvisoni/removing-duplicate-images-through-python-23c5fdc7479e
