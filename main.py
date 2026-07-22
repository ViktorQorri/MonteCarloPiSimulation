#Imports
import random as rd
import matplotlib.pyplot as plt

#Variables
cycles = 10 #set this number for the precision
inside = 0
estimation = 0
xpoints = []
ypoints = []

#Functions
def calcInside(x,y):
    global cycles
    global inside
    if pow(x,2) + pow(y,2) <= 1:
        inside += 1
    else:
        return

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
    calcInside(x,y)

plt.plot(xpoints,ypoints,'.')
plt.show()
calcPi()
print(estimation)