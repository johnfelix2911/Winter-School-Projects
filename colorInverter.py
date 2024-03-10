import cv2
import numpy as np

img = cv2.imread("dilated_image2.jpg", 0)
_ , img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

y = 0
for i in img:
    x = 0
    for j in i:
        if (j==255):
            img[y][x] = 0
        else:
            img[y][x] = 255
        x = x + 1
    y = y + 1

cv2.imshow("hh", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("inverted.jpg", img)