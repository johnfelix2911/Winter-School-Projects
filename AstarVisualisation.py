import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

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

def minPos(lis):
    min = lis[0]
    pos = 0
    for i in range(len(lis)):
        if lis[i]<min:
            pos = i
    return pos


def AStar(node,goal):
    vis.append(node)
    img[node[1]][node[0]][0] = 0
    img[node[1]][node[0]][1] = 0
    img[node[1]][node[0]][2] = 255
    cv2.imshow("hehe", img)
    cv2.waitKey(100)
    l_point = []
    l_dist = []
    for n in graph[node]:
        if n not in vis:
            d = math.pow(n[0]-goal[0],2) + math.pow(n[1]-goal[1],2)
            l_dist.append(d)
            l_point.append(n)
    next_node_pos = minPos(l_dist)
    next_node = l_point[next_node_pos]
    if next_node!=goal:
        AStar(next_node,goal)
    else:
        cv2.ellipse(img, goal, (10,10), 0, 0, 360, (0,0,255), 2)
        cv2.imshow("hehe", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

AStar((296,293), (498,490))