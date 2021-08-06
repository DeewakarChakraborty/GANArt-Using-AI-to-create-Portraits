
#Importing essential libraries
import os
from PIL import Image
import numpy as np



from_path = '/content/drive/MyDrive/Kaggle/Portrait/Data' #gdrive path where the scrapped images are saved
to_path = '/content/drive/MyDrive/Kaggle/Portrait/Images' #gdrive path where prepared images will be stored

size = 512 #I will be using 512*512 resolution to train the model


# loop through the images and resizing them
path, dirs, files = next(os.walk(from_path))
for file in sorted(files):
  print(file)
  try:
   image = Image.open(path + "/" + file)
   if image.mode == "RGB":
     image_resized = image.resize((size,size), resample=Image.BILINEAR)
     image_resized.save(to_path + "/" + file)
  except:
    print('Thumb.db')