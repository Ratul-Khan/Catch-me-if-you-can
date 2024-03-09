# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 14:18:13 2023

@author: asus
"""

import turtle


	
	
screen = turtle.Screen()

screen.title("")

screen.bgcolor('lightblue')



screen.bgpic("proj.gif")

# x = screen.numinput("Enter distance:",100)

screen.title("Level 1")

x = 7

# x = np.array([7,15,23],np.int32)

dist = x+1

player = turtle.Turtle()

player.color('blue')

player.shape('turtle')

# print(player.size())

ai = player.clone()

ai.color('red')

player.penup()

player.goto(-350, 300)

ai.penup()

ai.goto(350, 300)

true = 1


x+=1

stepsize = 700/x

line = turtle.Turtle()

line = turtle.Turtle()

line.penup()

line.goto(-350,280)

# base = turtle.Turtle()

# base.penup()

# base.goto(350, 280)

# line.pendown()

xx = 20

mm = int(x+1)

str = "abc"

win = 0    

for i in range(mm):
    line.pendown()
    line.forward(xx)
    line.penup()
    line.forward(stepsize-xx)

