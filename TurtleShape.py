import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(1)  # Set the drawing speed

# Draw the heart shape
pen.begin_fill()
pen.color("red")
pen.left(140)
pen.forward(100)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.left(120)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.forward(224)
pen.end_fill()

# Hide the turtle
pen.hideturtle()

# Keep the window open until it's closed by the user
turtle.done()
