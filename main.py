#Imports
import random as rd
import matplotlib.pyplot as plt

#Variables
cycles = 10000000 #set this number for the precision
plotcycles = 10000 #max 10.000 is recomended, gets calculated automaticaly if cycles < 10.000
inside = 0
estimation = 0
xpoints = []
ypoints = []
pointcolors = []

if cycles < plotcycles:
    plotcycles = cycles

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
for cycle in range(plotcycles):
    x = rd.random()
    y = rd.random()
    xpoints.append(x)
    ypoints.append(y)
    if calcInside(x,y):
        inside += 1
        pointcolors.append("green")
    else:
        pointcolors.append("red")

for cycle in range(cycles - plotcycles):
    x = rd.random()
    y = rd.random()
    if calcInside(x,y):
        inside += 1

calcPi()
print(estimation)
plt.gca().set_aspect('equal') #Plot aspect ratio set to "equal" (1:1 aspect)
plt.scatter(xpoints,ypoints,c=pointcolors)
plt.text(0, 1.1, f"PI aproximation: {estimation}")
plt.show()