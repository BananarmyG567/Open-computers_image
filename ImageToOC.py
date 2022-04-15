import cv2
import numpy as np


print("Max res 160 50, for none squished images do width: 100 and height: 50")

while True:
    try:
        width = int(input("Width: "))
        if width < 5:
            print("invalid input, please input number between 5-160")
        elif width > 160:
            print("invalid input, please input number between 5-160")
        else:
            break
    except:
        print("invalid input, please input number between 5-160")

while True:
    try:
        height = int(input("height: "))
        if height < 5:
            print("invalid input, please input number between 5-50")
        elif height > 50:
            print("invalid input, please input number between 5-50")
        else:
            break
    except:
        print("invalid input, please input number between 5-50")


print("Image file path (image has to be png)")

while True:
    try:
        imagepath = str(input("path: "))
        if imagepath[-4:] != ".png":
            print("invalid input file type, pleas use png")
        else:
            break
    except:
        print("invalid input, please input image path")


list = []

image = cv2.imread(imagepath)
(h, w, _) = image.shape
#cv2.imshow('Original', image)
#cv2.waitKey(0)

(cX, cY) = (w // width, h // height)
cX1 = cX
cY1 = cY

list.append([width,height])

for v1 in range(height):

    cX1 = cX

    for v2 in range(width):

        pixel = image[cY1-cY:cY1, cX1-cX:cX1]
        #cv2.imshow("Pixel", pixel)
        Averageperrow = np.average(pixel, axis=0)
        Average = np.average(Averageperrow, axis=0)
        rgb = [round(Average[2]),round(Average[1]),round(Average[0])]
        list.append(rgb)

        cX1 = cX1 + cX
    cY1 = cY1 + cY

list = str(list)
list = list.replace("[", "{")
list = list.replace("]", "}")
list = list.replace(" ", "")

F = open(imagepath.replace(".png",".OcI"),"w")
F.write(list)
F.close()