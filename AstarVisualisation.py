import cv2
import numpy as np

def gridMaker(img):
    for i in range(49):
        cv2.line(img, ((i+1)*10, 0), ((i+1)*10, 499), (255,255,255), 1)
        cv2.line(img, (0, (i+1)*10), (499, (i+1)*10), (255,255,255), 1)
    cv2.rectangle(img, (0,0), (499, 10), (255,255,255), -1)
    cv2.rectangle(img, (0,490), (499, 499), (255,255,255), -1)
    cv2.rectangle(img, (0,0), (10, 499), (255,255,255), -1)
    cv2.rectangle(img, (490, 0), (499, 499), (255,255,255), -1)

    cv2.rectangle(img, (0, 40), (70, 50), (255,255,255), -1)
    cv2.rectangle(img, (110, 0), (120, 90), (255,255,255), -1)
    cv2.rectangle(img, (350, 40), (400, 100), (255,255,255), -1)
    cv2.rectangle(img, (300,300), (450,450), (255,255,255), -1)
    cv2.rectangle(img, (0,150), (350,160), (255,255,255), -1)
    cv2.rectangle(img, (100, 150), (110, 390), (255,255,255), -1)
    cv2.rectangle(img, (220, 499), (230, 250), (255,255,255), -1)

    cv2.imshow("The GRID", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def findNeighbours(node):
    l = []
    neighbours = []
    if ((node[0]+10, node[1]) in graph):
        l.append((node[0]+10, node[1]))
        highlight((node[0]+10, node[1]), blue)
    if ((node[0]-10, node[1]) in graph):
        l.append((node[0]-10, node[1]))
        highlight((node[0]-10, node[1]), blue)
    if ((node[0], node[1]+10) in graph):
        l.append((node[0], node[1]+10))
        highlight((node[0], node[1]+10), blue)
    if ((node[0], node[1]-10) in graph):
        l.append((node[0], node[1]-10))
        highlight((node[0], node[1]-10), blue)
    for i in l:
        if i not in vis:
            neighbours.append(i)
    return neighbours

def highlight(pt, color):
    cv2.rectangle(img, (pt[0]-5, pt[1]-5), (pt[0]+5, pt[1]+5), color, -1)

def retracePath(node):
    highlight(node, green)
    cv2.imshow("the GRID", img)
    cv2.waitKey(100)
    if (node==start):
        return
    else:
        retracePath(parentTracker[node])

def Astar(img, graph, grid, node, start, goal, map, vis):
    neighbours = findNeighbours(node)
    for i in neighbours:
        if i not in parentTracker.keys():
            parentTracker[i] = node
    vis.append(node)
    if (node==goal):
        retracePath(goal)
        return
    highlight(node, red)
    for i in neighbours:
        g_score = map[node][0] + round(((i[0] - node[0])**2 + (i[1] - node[1])**2)**0.5)
        h_score = abs(goal[0] - i[0]) + abs(goal[1] - i[1])
        if i not in map.keys():
            map[i] = [g_score, h_score]
        else:
            if (map[i][0]+map[i][1] > g_score+h_score):
                map[i][0] = g_score
                map[i][1] = h_score
    potential_nodes = []
    min = 10000
    for i in map.keys():
        if i not in vis:
            if (map[i][0]+map[i][1])<min:
                min = map[i][0]+map[i][1]
                potential_nodes = [i]
            elif (map[i][0]+map[i][1])==min:
                potential_nodes.append(i)
    new_node = node
    if len(potential_nodes)==1:
        new_node = potential_nodes[0]
    else:
        min = 10000
        for i in potential_nodes:
            if map[i][1]<min:
                min = map[i][1]
                new_node = i
    for i in vis:
        highlight(i, red)
    cv2.imshow("The GRID", img)
    cv2.waitKey(100)
    Astar(img, graph, grid, new_node, start, goal, map, vis)

img = np.full((500,500,3), 0, dtype = np.uint8)
gridMaker(img)
grid = []
graph = []
map = {}
vis = []
parentTracker = {}
blue = (255,0,0)
green = (0,255,0)
red = (0,0,255)
for i in range(49):
    for j in range(49):
        grid.append(((i*10 + 5, j*10 + 5)))
        if (img[j*10 + 5][i*10 + 5][0] == 0):
            graph.append(((i*10 + 5, j*10 + 5)))
start = (15,15)
goal = (185, 405)
map[start] = [0,0]
highlight(start, red)
highlight(goal, green)
cv2.imshow("The GRID", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
Astar(img, graph, grid, start, start, goal, map, vis)
cv2.destroyAllWindows()
