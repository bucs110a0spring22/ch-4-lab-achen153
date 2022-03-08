import turtle
import math

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for h


def setupWindow(wn=None):
  wn.setworldcoordinates(-360, -1, 360, 1) 

def setupAxis(dart=None):
  dart.up()
  dart.goto(0,1)
  dart.down()
  dart.goto(0,-1)
  dart.up()
  dart.goto(-360,0)
  dart.down()
  dart.goto(360,0)

def drawSineCurve(dart):
    for i in range(-360,360):
      y = math.sin(math.radians(i))
      dart.goto(i,y)
      
def drawCosineCurve(dart):
  dart.up()
  dart.color("blue")
  dart.goto(-360,1)
  dart.down()
  for i in range(-360,360):
    y = math.cos(math.radians(i))
    dart.goto(i,y)

def drawTangentCurve(dart):
  dart.up()
  dart.color("red")
  dart.goto(-360,-1)
  dart.down()
  for i in range(-360,360):
    y = math.tan(math.radians(i))
    dart.goto(i,y)
    dart.up()

##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(-10)
    dart = turtle.Turtle()
    dart.speed(0)
    #example(dart)
    drawSineCurve(dart)
    
    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    setupAxis(dart)
    wn.exitonclick()
main()
