# author: mackowacko

import turtle

n = 200
length = 4
angle = 180 - 180 * (n-2) / n
numbers = range(0, n)

Jose = turtle.Turtle()

for number in numbers:
	Jose.color("magenta")
	Jose.forward(length)
	Jose.left(angle)

