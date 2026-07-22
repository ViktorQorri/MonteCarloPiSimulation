#Imports
import random as rd
import matplotlib.pyplot as plt

#Variables
cycles = 1000 #set this number for the precision
inside = 0
estimation = 0
xpoints = []
ypoints = []
pointcolors = []

#Functions
def calcInside(x,y):
    global cycles
    global inside
    if pow(x,2) + pow(y,2) <= 1:
        return True
    else:
        return False

def calcPi():
    global inside
    global cycles
    global estimation
    estimation = 4 * (inside / cycles)


#Main
for cycle in range(cycles):
    x = rd.random()
    y = rd.random()
    xpoints.append(x)
    ypoints.append(y)
    if calcInside(x,y):
        inside += 1
        pointcolors.append("green")
    else:
        pointcolors.append("red")

calcPi()
print(estimation)
plt.scatter(xpoints,ypoints,c=pointcolors)
plt.show()