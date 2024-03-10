import cv2
import numpy as np

def isBlue(l):
    if l[0]>100 and l[1]<100 and l[2]<100:
        return 1
    else:
        return 0
    
img = cv2.imread("final_proj_img.jpg")
map = np.full((500,800,3), (255,255,255), dtype = np.uint8)
lis = []
l = []
img = cv2.resize(img,(800,500))

lis.append([img[0][0][0], img[0][0][1], img[0][0][2]])

y = 0
for i in img:
    x=0
    for j in i:
        if (isBlue(j)):
            map[y][x][1] = 0
            map[y][x][2] = 0
            map[y][x][0] = 255
            cv2.imshow("map", map)
            cv2.waitKey(100)
        x = x + 1
    y = y + 1
cv2.destroyAllWindows()

cv2.imwrite("map_final.jpg", map)