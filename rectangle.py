import turtle


def octagon(len):
    for i in range(8):
        turtle.forward(len)
        turtle.right(45)

    for t in range(2):
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)


turtle.Screen().exitonclick()