import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("map_final.jpg")

x_coords = []
y_coords = []

y = 0
for i in img:
    x = 0
    for j in i:
        if j[1]<100 and j[2]<100:
            x_coords.append(x)
            y_coords.append(-y)
            #print(x," and ",y)
        x = x + 1
    y = y + 1

plt.plot(x_coords, y_coords, marker = 'o', markersize = 1, linestyle = '')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Graphy")
plt.grid(True)

plt.show()