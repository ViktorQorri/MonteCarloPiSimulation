# Monte carlo PI aproximation
By Viktor Qorri

## My goals for this project:
- AI-less project, no debug, thinking or coding by AI
- Learning about monte carlo simulations
- Aproximating PI with n amount of simulations
- Learning data visualisation libraries

## How will it work
### How can we calculate PI
Lets first talk about the area of a circle, the formula for the calculation is "A=π*r^(2)". We can rewrite this to "π=A/r^(2)"

### How are we calculating PI in the simulation
We will aproximate PI with the formula "π=A/r^(2)" that we just got. To solve this we need "A" and "r". We will use a quarter circle with a radius of 1 so "r=1".

Now our formula has turned into "π=A/1^(2)" which we can turn in to "π=A/1" and into "π=A (for r=1)".

Now we need to get "A", as said before we will use a quarter circle with radius 1. We will fire random points between 0 and 1 and calculating if the point falls into the circle. We can check if a point falls inside of the circle with the formula "X^(2)+Y^(2)<=1" as this formula is the bound of a circle with "r=1"

We will use the "random" library to generate the 2 coordinates between 0 and 1. calculate if it falls within the circle and calculate the total amount of points within the circle with the formula "Inside/Total". As we are using a quarter circle we will need to multiply this number by 4 to get the full number which will be aproximaly PI

After the calculation we will plot the points with the "mathplotlib" library.

## Learning/Feature Log
### 21-jul-2026
- README.md and a small description of the project in the file.