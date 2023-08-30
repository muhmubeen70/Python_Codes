import turtle
import math
wn = turtle.Screen()
bob = turtle.Turtle()
bob.right(90)
bob.forward(50)
bob.left(90)
bob.forward(100)

# Add your code below!
bob.left(90)
bob.forward(50)
bob.left(90)
bob.forward(100)

#for Triangle
dist=math.sqrt(100*100/2)
bob.right(135)
#bob.forward(72)
bob.forward(dist)
bob.right(90)
#bob.forward(72)
bob.forward(dist)

wn.exitonclick()