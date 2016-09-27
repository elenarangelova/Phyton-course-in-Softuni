import turtle
side=40
goto_size=40
for j in range(8):
    for i in range(8):
        if j % 2 == 1 and i % 2==0:
            turtle.begin_fill()
        elif j % 2 == 0 and i % 2 ==1:
            turtle.begin_fill()
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.end_fill()
        turtle.forward(side)
    turtle.penup()
    turtle.goto(0,goto_size)
    turtle.pendown()

    goto_size += 40
turtle.exitonclick()