#Imports
import random as rd

#Variables
cycles = 10000000 #set this number for the precision
inside = 0
estimation = 0

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
    calcInside(x,y)

calcPi()
print(estimation)