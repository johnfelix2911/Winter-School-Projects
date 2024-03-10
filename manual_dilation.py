import cv2
import numpy as np

img = cv2.imread("map_final.jpg", 0)
_, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, img1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

for k in range(6):
    y = 0
    print("Iteration ",k," going on")
    for i in img:
        x = 0
        for j in i:
            if x<799 and y<499:
                if (img[y+1][x]==0 or img[y][x+1]==0):
                    img[y][x] = 0
            x = x + 1
        y = y + 1

if (np.all(img==img1)):
    print("Same")
else:
    print("Diff")

cv2.imshow("dilated", img)
cv2.imshow("Original", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("dilated_image2.jpg", img)