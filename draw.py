# author: mackowacko

import turtle

n = 5
length = 100
angle = 180 - 180 * (n-2) / n
#numbers = range(0, n)
colors = ["red", "yellow", "orange", "magenta", "blue"]

Jose = turtle.Turtle()

for color in colors:
	Jose.color(color)
	Jose.forward(length)
	Jose.left(angle)

