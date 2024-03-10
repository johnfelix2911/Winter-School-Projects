import cv2
import numpy as np
import random
import math

def randomPointGenerator(width, height):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    return (x,y)

def nearestNodeFinder(point):
    dist = []
    for node in nodes:
        d = ((node.locx - point[0]) ** 2 + (node.locy - point[1]) ** 2)
        dist.append(d)
    return nodes[np.argmin(dist)]

def samplePointGenerator(pt1, pt2):
    theta = math.atan2(pt2[1] - pt1.locy, pt2[0] - pt1.locx)
    x = int(pt1.locx + step_size * math.cos(theta))
    y = int(pt1.locy + step_size * math.sin(theta))
    return (x,y)

def collisionChecker(pt1, pt2):
    line = np.linspace((pt1.locx, pt1.locy), pt2, num=10, dtype=int)
    for i in line:
        if np.any(image[i[1]][i[0]])==0:
            return 0
    return 1

def find_path(iterations):
    for j in range(iterations):  
        random_pt = randomPointGenerator(width, height)
        nearest = nearestNodeFinder(random_pt)
        sample_pt = samplePointGenerator(nearest, random_pt)
        if collisionChecker(nearest, sample_pt):
            sample_point = TreeNode(sample_pt[0], sample_pt[1])
            nearest.add_child(sample_point)
            nodes.append(sample_point)
            if np.linalg.norm(np.array(sample_pt) - np.array((goal.locx, goal.locy))) < step_size:
                sample_point.add_child(goal)
                retrace(goal)
                waypoint.insert(0, (start.locx, start.locy))   
                for i in range(len(waypoint)-1 ):
                    cv2.line(last, (int(waypoint[i][0]), int(waypoint[i][1])), (int(waypoint[i + 1][0]), int(waypoint[i + 1][1])), (0,0,255), 3)
                    cv2.imshow('RRT', last)
                    cv2.waitKey(100)
                return nodes
            cv2.line(img, (nearest.locx, nearest.locy), sample_pt, (0,0,255), 1)
            cv2.circle(img, sample_pt, 2, (255,0,0), -1)
            cv2.imshow("RRT", img)
            cv2.waitKey(100)
    return None
    
def retrace(goal):
    if goal.locx == start.locx:
        return
    waypoint.insert(0,(goal.locx, goal.locy))
    retrace(goal.parent)

image = cv2.imread("inverted.jpg")
img = cv2.imread("inverted.jpg")
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
last = cv2.imread("inverted.jpg")

start = (118,144)
goal = (314,174)
step_size = 15
iterations = 10000
cv2.circle(img, start, 5, (0, 0, 255), -1)
cv2.circle(img, goal, step_size, (255, 0, 0), 3)

class TreeNode:
    def __init__(self, locx, locy):
        self.locx = locx
        self.locy = locy
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

start = TreeNode(start[0], start[1])
goal = TreeNode(goal[0], goal[1])
height = image.shape[0]
width = image.shape[1]
nodes = [start]
waypoint = []

path = find_path(iterations)
if not path:
    print("Fail")
else:
    print("Success")
cv2.imshow("RRT Final Path", last)
cv2.waitKey(0)
cv2.destroyAllWindows()