import turtle
degrees = input('Enter degrees ')
length = input('Enter length ')

while True:
    turtle.left(int(degrees))
    turtle.forward(int(length))

turtle.done()