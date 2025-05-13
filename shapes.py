import turtle

def square(len):
    for i in range(4):
        turtle.forward(len)
        turtle.right(90)

def triangle(len):
    for i in range(3):
        turtle.forward(len)
        turtle.left(120)

def house(len):
    turtle.speed(0)
    turtle.color("blue")
    square(100)
    triangle(100)

def main():
    turtle.speed(0)
    turtle.color("blue")
    house(100)
    turtle.penup()
    turtle.forward(150)
    turtle.pendown()
    turtle.color("red")
    house(50)

main()
turtle.Screen().exitonclick()