import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('contr2.jpg')

height = np.size(img, 0)
width = np.size(img, 1)

print(img)

#creamos el histograma
color = ('b','g','r')
maxC=0
minC=255
for i, c in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color = c)
    plt.xlim([0,256])

count=0
a=0
b=255
c=0
d=0

for i in histr:
    if (i[0]!=0):
        c=count
        count=0
        break;
    count=count+1
reversed_histr = histr[::-1]
for i in reversed_histr:
    if (i[0]!=0):
        d=255-count
        count=0
        break;
    count=count+1
print(a,b,c,d)
# show the plotting graph of an image
for i in range (width-1):
    for j in range (height-1):
        b,g,r=img[i,j]
        img[i][j]=(img[i][j]-c)*((b-a)/(d-c))+a
plt.plot(histr)
cv2.imshow('image',img)
plt.show()

#crear un outliner
img2 = cv2.imread('contr2.jpg',0)
for i in range (15):
    for j in range (15):
        img2[i][j]=0
cv2.imwrite('new_copy.png',img2)
