from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:
sides = int(input)
for shapes in range (sides):
    t.pencolor("blue")
    t.pendown()
    t.forward(100)
    t.right(90)


#angle = 360/sides

#pencolor("azure")
#pendown()
#speed("10")

#for shapes in range (sides)
#goto(<50>, <100>)
#goto(<100>, <0>)
#goto(<100>, <0>)



# Close window on click.
exitonclick()
