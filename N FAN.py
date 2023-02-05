import turtle

print('please enter the number of squares: ')
n = int(input())
# draw fan of n squares 100*100
for count in range(n):
    # draw a square
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.left(360/n)
turtle.hideturtle()
turtle.done()