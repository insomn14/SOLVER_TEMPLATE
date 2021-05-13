from PIL import Image
from numpy import *

one_img = Image.open(r'encrypted_one.png')
two_img = Image.open(r'encrypted_two.png')

one = array(one_img)
two = array(two_img)

#print(img)

a, b, c = one.shape
#print(img.shape)

for x in range(0, a):
    for y in range(0, b):
        pixel1 = one[x, y]
        pixel2 = two[x, y]
        if pixel1.any():
            for i in range(0,3):
                pixel1[i] = pixel1[i] ^ pixel2[i]
            one[x][y] = pixel1

get = Image.fromarray(one)
get.save('out.png')
