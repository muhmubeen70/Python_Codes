import turtle             # allows us to use the turtles library
wn = turtle.Screen()      # creates a graphics window
wn.bgcolor("black")
alex = turtle.Turtle()    # create a turtle named alex
alex.color("White")
alex.pensize(5)
for _ in range(5):
    alex.forward(150)         # tell alex to move forward by 150 units
    alex.left(90)             # turn by 90 degrees
    alex.forward(75)          # complete the second side of a rectangle
    alex.left(90)             # turn by 90 degrees
    alex.forward(150)          # complete the second side of a rectangle
    alex.left(90)             # turn by 90 degrees
    alex.forward(75)          # complete the second side of a rectangle



wn.exitonclick()