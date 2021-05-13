from numpy import *
from PIL import Image

def brute(p, k):
    val = []
    for c in range(0,256):
        if (c * k % 251) == p:
            val.append(c)
    if len(val) > 1:
        print(val)
    return val[0]

enc_flag = Image.open(r'enc.png')
img = array(enc_flag)

#print(img)

key = [41, 37, 23]

a, b, c = img.shape
#print(img.shape)  # (200, 500, 4)

for x in range(0, a):
    for y in range(0, b):
        pixel = img[x, y]
        #print(pixel) # [ 92 121   9 255]
        for i in range(0,3):
            #print(f'Pixel : {pixel[i]}\t Key : {key[i]}\t Res : %d' % (pixel[i] * key[i] % 251))
            pixel[i] = brute(pixel[i], key[i])
        img[x][y] = pixel

dec = Image.fromarray(img)
dec.save('dec.png')
