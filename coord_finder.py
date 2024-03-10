import cv2
import numpy as np
import keyboard as kb

x = 400
y = 250

while True:
    img = cv2.imread("inverted.jpg")
    if kb.is_pressed("w"):
        y = y - 2
        print("(",x,",",y,")")
    if kb.is_pressed("s"):
        y = y + 2
        print("(",x,",",y,")")
    if kb.is_pressed("a"):
        x = x - 2
        print("(",x,",",y,")")
    if kb.is_pressed("d"):
        x = x + 2
        print("(",x,",",y,")")
    if kb.is_pressed("q"):
        break
    cv2.ellipse(img, (x,y), (10,10), 0, 0, 360, (0,0,255), 2)
    cv2.ellipse(img, (x,y), (2,2), 0, 0, 360, (0,0,255), -1)
    cv2.imshow("hehe", img)
    cv2.waitKey(100)
cv2.destroyAllWindows()