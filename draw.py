# author: mackowacko 

colors = ["red", "yellow", "blue", "magenta"]
angle = 90
numbers = range (5, 200, 2)

Jose = turtle.Turtle()

for color in colors:
	for number in numbers:
		Jose.forward(number)
		Jose.left(angle)
	