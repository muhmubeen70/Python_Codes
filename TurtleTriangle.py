import turtle
wn = turtle.Screen()

elan = turtle.Turtle()
elan.pensize(3)
elan.speed(10)
distance = 50
for _ in range(35):
    elan.forward(distance)
    elan.right(120)
    distance = distance + 10

wn.exitonclick()
