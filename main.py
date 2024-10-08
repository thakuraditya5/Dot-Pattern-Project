import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.hideturtle()
# List of dark colors
dark_colors = [
    (139, 0, 0),    # Dark Red
    (0, 100, 0),    # Dark Green
    (0, 0, 139),    # Dark Blue
    (75, 0, 130),   # Dark Purple
    (205, 92, 0),   # Dark Orange
    (0, 139, 139),  # Dark Cyan
    (139, 0, 139)   # Dark Magenta
]

tim.speed("fastest")

# Outer loop for rows
for row in range(10):
    n = 0  # Reset n for each row
    # Move to the starting position of the row
    tim.penup()
    tim.goto(-300, 200-row * 50)  # Adjust the y-coordinate for each row
    tim.pendown()

    while n <= 500:
        tim.penup()
        tim.forward(50)  # Move forward
        tim.pendown()  # Put the pen down to start drawing
        tim.dot(20,random.choice(dark_colors))  # Set a random fill color
        tim.penup()
        n += 50  # Increment the counter

screen = t.Screen()
screen.exitonclick()
