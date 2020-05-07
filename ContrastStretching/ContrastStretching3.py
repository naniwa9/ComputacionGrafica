import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('new_copy.png')
#print(img)
height = np.size(img, 0)
width = np.size(img, 1)
limit = height*width*10/100

#print(height*width,limit)

#histr = cv2.calcHist([img],[0],None,[256],[0,256])
color = ('b','g','r')
maxC=0
minC=255
for i, c in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color = c)
    plt.xlim([0,256])
#print(histr[0][0],histr[1][0])
count=0
quantity=0
a=0
b1=255
c=0
d=0
print('nim',height, width)
#for i in histr:
#    print(i[0])
for i in histr:
    #print('quan',quantity)
    if (quantity>=limit):
        c=count
        count=0
        quantity=0
        break;
    count=count+1
    quantity=quantity+i[0]
reversed_histr = histr[::-1]
for i in reversed_histr:
    if (quantity>=limit):
        d=255-count
        count=0
        quantity=0
        break;
    count=count+1
    quantity=quantity+i[0]
#    if (i[0]!=0):
#        d=255-count
#        count=0
#        break;
#    count=count+1
print(a,b1,c,d)
#temp=0
for i in range (width-1):
    for j in range (height-1):
        b,g,r=img[i,j]
        temp1=img[i,j]
        temp=(temp1[0]-c)*((b1-a)/(d-c))+a
        if (temp>255):
            temp=255
        if (temp<0):
            temp=0
        #print('temp',temp)
        img[i][j]=temp
plt.plot(histr)
cv2.imshow('image',img)
plt.show()
