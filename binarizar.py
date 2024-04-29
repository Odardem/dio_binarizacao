from PIL import Image
from time import sleep
import numpy as np
#L = R * 299/1000 + G * 587/1000 + B * 114/1000

def convert_to_grey(image):
    image = np.asarray(image)
    r,g,b = image[:,:,0],image[:,:,1],image[:,:,2]
    cinza = r * 0.2125 + g * 0.7154 + b * 0.0721
    img = Image.fromarray(cinza.astype(np.uint8))
    return img

def convert_grey_to_binary(image, threshold=128):
    image = np.asarray(image)
    binary = np.where(image >= threshold, 255,0)
    img = Image.fromarray(binary.astype(np.uint8))
    return img

img = Image.open(r'./img/lena.png')
cinza = convert_to_grey(img)
cinza.show()

binario = convert_grey_to_binary(cinza)
binario.show()





