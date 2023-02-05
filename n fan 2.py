import turtle
def turtle_square(side_len):
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
print('please enter the number of squares: ')
n = int(input())
# draw fan of n squares 100*100
for count in range(n):
    turtle_square(100)
    turtle.left(360/n)
turtle.hideturtle()
turtle.done()