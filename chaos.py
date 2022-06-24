#!/usr/bin/env python3
import turtle
from numpy import *
import random

window = turtle.Screen()
window.bgcolor("black")
window.title("chaos")
window.tracer(0)

g = -0.1
r = 200
balls = []
colors = ["orange","blue","green","pink","white"]
start = [[0.0002,0],[0.0001,0]]

circle = turtle.Turtle()
circle.color("green")
circle.penup()
circle.goto(0,-r)
circle.pendown()
circle.hideturtle()
circle.circle(r)

for _ in range(2):
	balls.append(turtle.Turtle())

for ball in balls:
	ball.shape("circle")
	ball.shapesize(0.5,0.5,1)
	ball.pensize(0.1)
	#ball.color(random.choice(colors))
	ball.speed(0)
	ball.penup()
v0 = [0,0]
v1 = [0,0]
balls[0].goto(start[0])
balls[1].goto(start[1])

balls[0].color("red")
balls[1].color("blue")

balls[0].pendown()
balls[1].pendown()

while True:
	window.update()
	v0[1] += g
	v1[1] += g

	R0 = [balls[0].xcor(),balls[0].ycor()]
	R1 = [balls[1].xcor(),balls[1].ycor()]
	
	if (balls[0].xcor()**2 + balls[0].ycor()**2 >= r**2):
		d = dot(v0,R0)/linalg.norm(R0)
		R0 = [2*d*a/linalg.norm(R0) for a in R0]
		v0 = [v0[i] - R0[i] for i in range(2)]
		v0[1] += g
	
	if (balls[1].xcor()**2 + balls[1].ycor()**2 >= r**2):
		d = dot(v1,R1)/linalg.norm(R1)
		R1 = [2*d*a/linalg.norm(R1) for a in R1]
		v1 = [v1[i] - R1[i] for i in range(2)]
		v1[1] += g

	balls[1].sety(balls[1].ycor() + v1[1])
	balls[1].setx(balls[1].xcor() + v1[0])
	balls[0].sety(balls[0].ycor() + v0[1])
	balls[0].setx(balls[0].xcor() + v0[0])
	
window.mainloop()