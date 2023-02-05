import math
import turtle

print("please enter the length of the two legs in a right triangle:")
a = float(input("leg #1: "))
b = float(input("leg #2: "))
c = math.sqrt(a**2 + b**2)

alpha_in_radiance = math.atan(a / b)
alpha = math.degrees(alpha_in_radiance)
beta = 90 - alpha

turtle.forward(a)
turtle.left(90)
turtle.forward(b)
turtle.left(180 - alpha)
turtle.forward(c)
turtle.left(180 - beta)
turtle.hideturtle()
turtle.done()
