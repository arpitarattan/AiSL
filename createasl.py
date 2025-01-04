import os 
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

path = 'C:/Users/lenovo/Downloads/AiSL/asl_dataset'

images = []
labels = []

dataset = os.listdir(path)

for folder in dataset:
    subpath = os.path.join(path, folder)
    imgs = os.listdir(subpath)


    # Iterate through images in each letter
    for img in imgs:
        img_path = os.path.join(subpath, img)
        images.append(Image.open(img_path))
        labels.append(folder)
        break

fig, ax = plt.subplots(6,6)
fig.set_size_inches(15,15)

for i in range(6):
  for j in range(6):
    ax[i,j].imshow(images[(i*6)+j], cmap='gray')
    ax[i,j].title.set_text(labels[(i*6) + j])
    ax[i,j].axis('off')

plt.show()