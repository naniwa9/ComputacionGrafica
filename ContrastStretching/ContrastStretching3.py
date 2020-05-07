import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('new_copy.png')
height = np.size(img, 0)
width = np.size(img, 1)
limit = height*width*10/100

#creamos el histograma
color = ('b','g','r')
maxC=0
minC=255
for i, c in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color = c)
    plt.xlim([0,256])

#variables
count=0
quantity=0
a=0
b1=255
c=0
d=0

#buscamos la mayor y menor escala de la imagen en el histograma,
#usando los limites y apoyandonos en la variable "quantity"
#buscamos el valor de "c"
for i in histr:
    if (quantity>=limit):
        c=count
        count=0
        quantity=0
        break;
    count=count+1
    quantity=quantity+i[0]

#invertimos el histograma para buscar el mayor valor, "d"
reversed_histr = histr[::-1]
for i in reversed_histr:
    if (quantity>=limit):
        d=255-count
        count=0
        quantity=0
        break;
    count=count+1
    quantity=quantity+i[0]

print(a,b1,c,d)

#Alteramos la imagen usando la formula con los limites.
#usamos las condiciones para no pasarnos exceder los limites de la escala de grises
for i in range (width-1):
    for j in range (height-1):
        b,g,r=img[i,j]
        temp1=img[i,j]
        temp=(temp1[0]-c)*((b1-a)/(d-c))+a
        if (temp>255):
            temp=255
        if (temp<0):
            temp=0
        img[i][j]=temp
plt.plot(histr)
cv2.imshow('image',img)
plt.show()
