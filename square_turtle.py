import turtle

print("please enter the length of each side:")
side_len = int(input())

for i in range((4)):
  turtle.forward(side_len)
  turtle.left(90)

turtle.hideturtle()
turtle.done()
