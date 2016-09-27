import turtle

turtle.speed('fastest')
for i in range(36):
    turtle.rt(10)
    for j in range(36):
       turtle.rt(10)
       turtle.fd(20)
turtle.exitonclick()