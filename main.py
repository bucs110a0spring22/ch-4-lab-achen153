import turtle
import math

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for h


def setupWindow(wn=None):
  wn.setworldcoordinates(-360, -1, 360, 1) 

def setupAxis(dart=None, x_start=0, y_start=0, x_end=0, y_end=0):
  dart.up()
  dart.goto(x_start,y_start)
  dart.down()
  dart.goto(x_end, y_end)
  dart.up

def drawSineCurve(dart):
    dart.up()
    for i in range(-360,361):
      y = math.sin(math.radians(i))
      dart.goto(i,y)
      dart.down()
  
def drawCosineCurve(turt):
  turt.up()
  turt.color("blue")
  turt.goto(-360,1)
  turt.down()
  for i in range(-360,361):
    y = math.cos(math.radians(i))
    turt.goto(i,y)

def drawTangentCurve(dart):
  dart.up()
  dart.color("red")
  dart.goto(-360,-1)
  dart.down()
  for i in range(-360,361):
    y = math.tan(math.radians(i))
    dart.goto(i,y)

def drawSineCurveChangeColor(dart):
  SineCurveColor = str(input("Enter 'purple' if you'd like the sine curve to be red or 'green' if you want it to be green"))
  dart.color(SineCurveColor)
  drawSineCurve(dart)

def drawCircle(dart, x_origin=0, y_origin=0, radius=0):
  dart.up()
  dart.goto(x_origin, y_origin-radius)
  dart.down()
  dart.circle(radius, steps=360)

def ifCircleLeftRight(turt):
  if turt.distance(0,0) > 1:
    return "Your circle is on right side"
  if turt.distance(0,0) <=1:
    return "Your circle is on left side"


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
    setupAxis(dart, -360, 0, 360, 0)
    setupAxis(dart, 0, -1, 0, 1)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    drawSineCurveChangeColor(dart)
    wn.setworldcoordinates(-10, -10, 10, 10)
    wn.clear()
    setupAxis(dart, 0, -10, 0, 10)
    setupAxis(dart, -10, 0, 10, 0)
    drawCircle(dart, 3, 3, radius=3)
    print(ifCircleLeftRight(dart))
    wn.exitonclick()
main()
