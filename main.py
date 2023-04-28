import cv2 as cv
import sys

def getPixelGreyScale(pixel) : 
    return (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) / 3

if len(sys.argv) < 2 : 
    print("missing an image\n")
    exit(1)


#grayscale string
str = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'."
#read image
img = cv.imread(sys.argv[1])
rows, cols, channels = img.shape
#creating new image array according to image size
newImage = [[0] * cols] * rows

f = open("image.txt", "x")
for i in range(rows) :
    for j in range(cols) :
        
        #getting image greyscale value
        pixelGreyscale = int(getPixelGreyScale(img[i, j]))
        #setting pixel ascii value according to greyscale

        newImage[i][j] = (str[max(0, len(str) - 1 - int(max(0, ((pixelGreyscale/255) * len(str)) - 1)))])
        f.write(newImage[i][j] +" ")
    f.write("\n")
f.close()


