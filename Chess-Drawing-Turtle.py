import turtle
screen = turtle.Screen()
screen.bgcolor("red")
caretta = turtle.Turtle()
caretta.shape('turtle')
caretta.speed(10)
caretta.pensize(3)

def drawBox():
    for i in range(4):
        caretta.forward(40)
        caretta.right(90)

def oddBlock(y):
    for i in range(0,320,40):
        if i == 0 or i == 80 or i == 160 or i == 240:
            caretta.goto(i,y)
            caretta.begin_fill()
            caretta.color("white")
            drawBox()
            caretta.end_fill()
        else :
            caretta.goto(i,y)
            caretta.begin_fill()
            caretta.color("black")
            drawBox()
            caretta.end_fill()

def evenBlock(y):
    for i in range(0,320,40):
        if i == 0 or i == 80 or i == 160 or i == 240:
            caretta.goto(i,y)
            caretta.begin_fill()
            caretta.color("black")
            drawBox()
            caretta.end_fill()
        else :
            caretta.goto(i,y)
            caretta.begin_fill()
            caretta.color("white")
            drawBox()
            caretta.end_fill()

for y in range(0,320,40):
    if y == 0 or y == 80 or y == 160 or y == 240 or y == 320:
        caretta.penup()
        oddBlock(y)
        caretta.pendown()
    else:
        caretta.penup()
        evenBlock(y)
        caretta.pendown()

screen.exitonclick()