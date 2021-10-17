import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def image_open(Image_Address): 
  ImageAddress = Image_Address
  ImageItself = Image.open(ImageAddress)
  ImageNumpyFormat = np.asarray(ImageItself)
  plt.imshow(ImageNumpyFormat)
  plt.draw()
  plt.pause(5) # pause how many seconds
  plt.close()
  return 0
  