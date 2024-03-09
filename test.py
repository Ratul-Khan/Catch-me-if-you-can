# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 19:17:15 2022

@author: Asus
"""

import turtle

def take_zero(a,b,c,d,distance):
    lst =[]
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.append(d)
    lst = sorted(lst)
    #print(lst)
    a = lst[0]
    b = lst[1]
    c = lst[2]
    d = lst[3]
    
    if a[0] == distance or b[0] == distance or c[0] == distance or d[0] == distance :
        if a[0] == distance:
            a=(a[0],True)
            return a
        
        elif b[0] == distance:
            b=(b[0],True) 
            return b
        
        elif c[0] == distance:
            c=(c[0],True)
            return c
        
        elif d[0] == distance:
            d=(d[0],True)
            return d
        
        
    else:
        if a[1]:
            return a
        
        elif b[1]:
            return b
        
        elif c[1]:
            return c
        
        elif d[1]:
            return d
        
        return a
    
    
def avoid_zero(a,b,c,d,distance):
    
    lst =[]
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.append(d)
    lst = sorted(lst)
    a = lst[0]
    b = lst[1]
    c = lst[2]
    d = lst[3]
    
    #print(lst)
    if (a[0] > distance or b[0] > distance or c[0] > distance or d[0] > distance):
        if a[0] > distance:
            return a
        elif b[0] > distance :
            return b
        elif c[0] > distance :
            return c
        elif d[0] > distance :
            return d
        
    else:
        if a[1]==False:
            return a
        elif b[1]==False :
            return b
        elif c[1]==False :
            return c
        elif d[1]==False:
            return d
    return a

def minimax (policeTurn, step_flag , distance):
    step = step_flag[0]
    flag = step_flag[1]
    distance -= step
	# base case : targetDepth reached
    if distance <= 0:
        return step_flag
    two = 2
    three = 3
    four = 4
    five =5
    if policeTurn : 
        #print("Before Police" , step, distance)
        #flag = False
        step_flag = take_zero(minimax(False, (two, flag) ,distance),	
                         minimax(False, (three, flag) ,distance),
                     	minimax(False, (four, flag),distance),
                     	minimax(False, (five, flag) ,distance),distance)
        
        #print("After Police" , step_flag, distance)
        return step_flag

    else:
        #print("Before Theif" , step, distance)
        #flag= False
        step_flag = avoid_zero(minimax(True, (two, flag) ,distance),	
                         minimax(True, (three, flag) ,distance),
                     	minimax(True, (four, flag),distance),
                     	minimax(True, (five, flag) ,distance),distance)
		#step = avoid_zero(minimax(True, 2,distance), minimax(True, 3 ,distance),minimax(True,4,distance),minimax(True, 5,distance),distance)
        #print("After Theif" , step_flag, distance)
        return step_flag

screen = turtle.Screen()

screen.bgcolor('lightblue')

x = screen.numinput("Enter distance:",100)

dist = x+1

player = turtle.Turtle()

player.color('blue')

player.shape('turtle')

# print(player.size())

ai = player.clone()

ai.color('red')

player.penup()

player.goto(-350, 100)

ai.penup()

ai.goto(350, 100)

true = 1

# x = screen.numinput("Enter distance:",100)

x+=1

stepsize = 700/x

line = turtle.Turtle()

line.penup()

line.goto(-350,80)

base = turtle.Turtle()

base.penup()

base.goto(350, 80)

# line.pendown()

xx = 20

mm = int(x+1)

for i in range(mm):
    line.pendown()
    line.forward(xx)
    line.penup()
    line.forward(stepsize-xx)
    
while(dist>0):
    steps = screen.numinput("Enter steps:",100)
    
    player.forward(stepsize*steps)
    if(player.pos()==ai.pos()):
        screen.title("Player lost the game!")
        break
    if(player.pos()>ai.pos()):
        screen.title("Player won the game!")
        break
    
    # steps_ai = screen.numinput("Enter steps:",100)
    
    tem = minimax (True, (steps,False) , dist)
    
    steps_ai = tem[0]
    
    
    
    ai.backward(steps_ai*stepsize )
    if(player.pos()==ai.pos()):
        screen.title("Player lost the game!")
        break
    if(player.pos()>ai.pos()):
        screen.title("Player won the game!")
        break
    
    dist-=steps
    
    dist-=steps_ai
    
    
    
        
# while true == 1:

#     steps = screen.numinput("Enter steps:",100)
    
#     player.forward(stepsize*steps)
#     if(player.pos()==ai.pos()):
#         screen.title("Player lost the game!")
#         break
#     if(player.pos()>ai.pos()):
#         screen.title("Player won the game!")
#         break
    
#     # from minimax:
#     # steps_ai = minimax()
    
#     steps_ai = screen.numinput("Enter steps:",100)
    
#     ai.backward(steps_ai*stepsize )
#     if(player.pos()==ai.pos()):
#         screen.title("Player lost the game!")
#         break
#     if(player.pos()>ai.pos()):
#         screen.title("Player won the game!")
#         break
    
    

turtle.done()