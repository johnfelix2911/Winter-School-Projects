import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("map_final.jpg")

x_coords = []
y_coords = []

#collecting x an y coordinates
y = 0
for i in img:
    x = 0
    for j in i:
        if j[1]<100 and j[2]<100:
            x_coords.append(x)
            y_coords.append(y)
        x = x + 1
    y = y + 1
    
graph = {}
length = len(x_coords)

#making the graph
for i in range(length):
    graph[(x_coords[i],y_coords[i])] = []
    if img[y_coords[i]][x_coords[i]+1][1]<100 and img[y_coords[i]][x_coords[i]+1][2]<100:
        graph[(x_coords[i],y_coords[i])].append((x_coords[i]+1,y_coords[i]))
    if img[y_coords[i]][x_coords[i]-1][1]<100 and img[y_coords[i]][x_coords[i]-1][2]<100:
        graph[(x_coords[i],y_coords[i])].append((x_coords[i]-1,y_coords[i]))
    if img[y_coords[i]+1][x_coords[i]][1]<100 and img[y_coords[i]+1][x_coords[i]][2]<100:
        graph[(x_coords[i],y_coords[i])].append((x_coords[i],y_coords[i]+1))
    if img[y_coords[i]-1][x_coords[i]][1]<100 and img[y_coords[i]-1][x_coords[i]][2]<100:
        graph[(x_coords[i],y_coords[i])].append((x_coords[i],y_coords[i]-1))
    
print(graph)

vis=[]
q=[]

#applying bfs
def bfs(node):
    q.append(node)
    vis.append(node)
    img[node[1]][node[0]][0] = 0
    img[node[1]][node[0]][1] = 0
    img[node[1]][node[0]][2] = 255
    while True:
        m=q.pop(0)
        for n in graph[m]:
            if n not in vis:
                vis.append(n)
                img[n[1]][n[0]][0] = 0
                img[n[1]][n[0]][1] = 0
                img[n[1]][n[0]][2] = 255
                cv2.imshow("hehe", img)
                cv2.waitKey(100)
                q.append(n)
cv2.destroyAllWindows()

bfs((296,293))