# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 11:52:55 2022

@author: Asus
"""

import turtle
from turtle import Screen, Turtle
import math

def close():
    exit()

def take_zero(a,b,distance):
    lst =[]
    lst.append(a)
    lst.append(b)
    lst = sorted(lst)
    #print(lst)
    a = lst[0]
    b = lst[1]
    
    if a[0] == distance or b[0] == distance :
        if a[0] == distance:
            a=(a[0],True)
            return a
        
        elif b[0] == distance:
            b=(b[0],True) 
            return b
        
        
        
    else:
        if a[1]:
            return a
        
        elif b[1]:
            return b
        
     
        return a
    
    
def avoid_zero(a,b,distance):
    
    lst =[]
    lst.append(a)
    lst.append(b)
    lst = sorted(lst)
    a = lst[0]
    b = lst[1]
    
    #print(lst)
    if (a[0] > distance or b[0] > distance):
        if a[0] > distance:
            return a
        elif b[0] > distance :
            return b
        
    else:
        if a[1]==False:
            return a
        elif b[1]==False :
            return b
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
    
    if policeTurn : 
        #print("Before Police" , step, distance)
        #flag = False
        step_flag = take_zero(minimax(False, (two, flag) ,distance),	
                         minimax(False, (three, flag) ,distance),distance)
        
        #print("After Police" , step_flag, distance)
        return step_flag

    else:
        #print("Before Theif" , step, distance)
        #flag= False
        step_flag = avoid_zero(minimax(True, (two, flag) ,distance),	
                         minimax(True, (three, flag) ,distance),distance)
		#step = avoid_zero(minimax(True, 2,distance), minimax(True, 3 ,distance),minimax(True,4,distance),minimax(True, 5,distance),distance)
        #print("After Theif" , step_flag, distance)
        return step_flag

def set_difficulty():
    
    screen = Screen()

    screen.title("Catch me if you can")

    screen.bgcolor('lightblue')



    screen.bgpic("proj.gif")

    difficulty = screen.textinput("Difficulty","Easy/Medium/Hard?")
    screen.clearscreen()
    return difficulty

def easy():
    screen = Screen()

    screen.title("Easy:Level 1")

    screen.bgcolor('lightblue')



    screen.bgpic("proj.gif")

    
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
    
    line.penup()
    
    line.goto(-350,280)
    
    xx = 20
    
    mm = int(x+1)
    
    str = "abc"
    
    win = 0    
    
    for i in range(mm):
        line.pendown()
        line.forward(xx)
        line.penup()
        line.forward(stepsize-xx)
        
    # for i in range(3):
    #     dist = x[i]+1
        
        
    while(dist>0):
        steps = screen.numinput("Steps:","Enter valid steps(2/3)")
        
        if steps != 2 and steps != 3:
            continue
        
        player.forward(stepsize*steps)
        
        dist-=steps 
        
        if(dist == 0):
            # screen.title("Player lost the game!")
            str = "Player lost the game!"
            win=0
            break
        
        if(dist<0):
            # screen.title("Player won the game!")
            str = "Player won the game!"
            win=1
            break
        
        tem = minimax (True, (steps,False) , dist+steps)
        
        steps_ai = tem[0]
        
        dist-=steps_ai
        
        ai.backward(steps_ai*stepsize )
        
        if(dist == 0):
            # screen.title("Player lost the game!")
            str = "Player lost the game!"
            win=0
            break
        
        if(dist<0):
            # screen.title("Player won the game!")
            str = "Player won the game!"
            win=1
            break
    
        
        
        
    
    if win != 0:
    
        ex = screen.textinput(str,"Continue to level 2(yes/no)?")
    
    if win == 0:
       return win
    
    if ex[0] == 'y':
        
    
        screen.title("Easy:Level 2")
        
        x = 14
        
        dist = x+1
        
        player.penup()
        
        player.goto(-350, 100)
        
        ai.penup()
        
        ai.goto(350, 100)
        
        true = 1
        
        x+=1
    
        stepsize = 700/x
    
        line = turtle.Turtle()
    
        line.penup()
    
        line.goto(-350,80)
        
        xx = 20
    
        mm = int(x+1)
    
        str = "abc"
    
        win = 0    
    
        for i in range(mm):
            line.pendown()
            line.forward(xx)
            line.penup()
            line.forward(stepsize-xx)
            
        while(dist>0):
            steps = screen.numinput("Steps:","Enter valid steps(2/3)")
            
            if steps != 2 and steps != 3:
                continue
            
            player.forward(stepsize*steps)
            
            dist-=steps 
            
            if(dist == 0):
                # screen.title("Player lost the game!")
                str = "Player lost the game!"
                win=0
                break
            
            if(dist<0):
                # screen.title("Player won the game!")
                str = "Player won the game!"
                win=1
                break
            
            # player.forward(stepsize*steps)
            # if(player.pos()==ai.pos()):
            #     screen.title("Player lost the game!")
            #     break
            # if(player.pos()>ai.pos()):
            #     screen.title("Player won the game!")
            #     break
            
            # steps_ai = screen.numinput("Enter steps:",100)
            
            # tem = minimax (True, (steps,False) , dist)
            
            # steps_ai = tem[0]
            
            tem = minimax (True, (steps,False) , dist+steps)
            
            steps_ai = tem[0]
            
            dist-=steps_ai
            
            ai.backward(steps_ai*stepsize )
            
            if(dist == 0):
                # screen.title("Player lost the game!")
                str = "Player lost the game!"
                win=0
                break
            
            if(dist<0):
                # screen.title("Player won the game!")
                str = "Player won the game!"
                win=1
                break
            
    if(ex[0]=='n'):
        return win
        
    if win != 0:
    
        ex = screen.textinput(str,"Continue to level 3(yes/no)?")
    
    if win == 0:
       return win
    
    if ex[0] == 'y':
        
    
        screen.title("Easy:Level 3")
        
        x = 21
        
        dist = x+1
        
        player.penup()
        
        player.goto(-350, -230)
        
        ai.penup()
        
        ai.goto(350, -230)
        
        true = 1
        
        x+=1
    
        stepsize = 700/x
    
        line = turtle.Turtle()
    
        line.penup()
    
        line.goto(-350,-240)
        
        xx = 20
    
        mm = int(x+1)
    
        str = "abc"
    
        win = 0    
    
        for i in range(mm):
            line.pendown()
            line.forward(xx)
            line.penup()
            line.forward(stepsize-xx)
            
        while(dist>0):
            steps = screen.numinput("Steps:","Enter valid steps(2/3)")
            
            if steps != 2 and steps != 3:
                continue
            
            player.forward(stepsize*steps)
            
            dist-=steps 
            
            if(dist == 0):
                # screen.title("Player lost the game!")
                str = "Player lost the game!"
                win=0
                break
            
            if(dist<0):
                # screen.title("Player won the game!")
                str = "Player won the game!"
                win=1
                break
            
            
            tem = minimax (True, (steps,False) , dist+steps)
            
            steps_ai = tem[0]
            
            dist-=steps_ai
            
            ai.backward(steps_ai*stepsize )
            
            if(dist == 0):
                # screen.title("Player lost the game!")
                str = "Player lost the game!"
                win=0
                break
            
            if(dist<0):
                # screen.title("Player won the game!")
                str = "Player won the game!"
                win=1
                break
    if(ex[0]=='n'):
        return win 
    screen.clearscreen()
    return win
   
    
def medium():
    GRID_SIZE = 600
    screen = Screen()
    screen.title("Medium:Level 1")
    screen.bgcolor('lightblue')
    screen.bgpic("proj.gif")
    sub_divisions = 7
    #print(sub_divisions)
    
    cell_size = GRID_SIZE / float(sub_divisions)  # force float for Python 2
    
    win = 0
    
    player = Turtle()
    
    player.color('blue')
    
    player.shape('turtle')
    
    # print(player.size())
    
    ai = player.clone()
    
    ai.color('red')
    
    player.penup()
    
    player.goto(-280, 270)
    
    ai.penup()
    
    ai.goto(280, -270)
    
    
    turtle = Turtle()
    turtle.penup()
    turtle.goto(-GRID_SIZE/2, GRID_SIZE/2)
    turtle.pendown()
    turtle.speed(1000)
    
    angle = 90
    
    for _ in range(4):
        turtle.forward(GRID_SIZE)
        turtle.right(angle)
    
    for _ in range(2):
        for _ in range(1, sub_divisions):
            turtle.forward(cell_size)
            turtle.right(angle)
            turtle.forward(GRID_SIZE)
            turtle.left(angle)
    
            angle = -angle
    
        turtle.forward(cell_size)
        turtle.right(angle)
        
    
    dist_x = sub_divisions-1
    dist_y = sub_divisions-1
    stepsize = cell_size
    prev_player_x = -280
    prev_player_y = 270
    prev_ai_x = 280
    prev_ai_y = -270
    while(dist_x>0 or dist_y >0):
        steps_x = screen.numinput("X_Steps:","Enter valid steps(2/3)")
        steps_y = screen.numinput("Y_Steps:","Enter valid steps(2/3)")
        #steps = steps_x+steps_y
        if (steps_x != 2 and steps_x != 3) or (steps_y != 2 and steps_y != 3):
            continue
        
        player.goto(prev_player_x+stepsize*steps_x,prev_player_y-stepsize*steps_y)
        prev_player_x = prev_player_x+stepsize*steps_x
        prev_player_y = prev_player_y-stepsize*steps_y
        dist_x-=steps_x
        dist_y-=steps_y
       # dist = math.sqrt(dist_x**2+dist_y**2)
        
        if(dist_x == 0 and  dist_y==0):
            # screen.title("Player lost the game!")
            str = "Player lost the game!"
            win=0
            break
        
        if(dist_x<0 or dist_y<0):
            # screen.title("Player won the game!")
            str = "Player won the game!"
            win=1
            break
        
        tem_x = minimax (True, (steps_x,False) , dist_x+steps_x)
        
        steps_x_ai = tem_x[0]
        
        dist_x-=steps_x_ai
        
        tem_y = minimax (True, (steps_y,False) , dist_y-steps_y)
        
        steps_y_ai = tem_y[0]
        
        dist_y-=steps_y_ai
        #print(steps_x_ai,steps_y_ai)
        
        ai.goto(prev_ai_x-stepsize*steps_x_ai,prev_ai_y+stepsize*steps_y_ai)
        prev_ai_x = prev_ai_x-stepsize*steps_x_ai
        prev_ai_y = prev_ai_y+stepsize*steps_y_ai
        
        print(dist_x,dist_y)
        if(dist_x == 0 and dist_y ==0):
            str = "Player lost the game!"
            win=0
            break
        
        if(dist_x<0 or dist_y<0):
            str = "Player won the game!"
            win=1
            break
    if win != 0:
    
        ex = screen.textinput(str,"Continue to level 2(yes/no)?")
    
    if win == 0:
        return win
        
    if ex[0]=='y' :
         screen.clearscreen()
         GRID_SIZE = 600
         screen = Screen()
         screen.title("Medium:Level 2")
         screen.bgcolor('lightblue')
         screen.bgpic("proj.gif")
         sub_divisions = 14
         #print(sub_divisions)
         
         cell_size = GRID_SIZE / float(sub_divisions)  # force float for Python 2
         
         
        
         
         player = Turtle()
         
         player.color('blue')
         
         player.shape('turtle')
         
         # print(player.size())
         
         ai = player.clone()
         
         ai.color('red')
         
         player.penup()
         
         player.goto(-280, 270)
         
         ai.penup()
         
         ai.goto(280, -270)
         
         
         turtle = Turtle()
         turtle.penup()
         turtle.goto(-GRID_SIZE/2, GRID_SIZE/2)
         turtle.pendown()
         turtle.speed(1000)
         
         angle = 90
         
         for _ in range(4):
             turtle.forward(GRID_SIZE)
             turtle.right(angle)
         
         for _ in range(2):
             for _ in range(1, sub_divisions):
                 turtle.forward(cell_size)
                 turtle.right(angle)
                 turtle.forward(GRID_SIZE)
                 turtle.left(angle)
         
                 angle = -angle
         
             turtle.forward(cell_size)
             turtle.right(angle)
             
         
         dist_x = sub_divisions-1
         dist_y = sub_divisions-1
         stepsize = cell_size
         prev_player_x = -280
         prev_player_y = 270
         prev_ai_x = 280
         prev_ai_y = -270
         while(dist_x>0 or dist_y >0):
             steps_x = screen.numinput("X_Steps:","Enter valid steps(2/3)")
             steps_y = screen.numinput("Y_Steps:","Enter valid steps(2/3)")
             #steps = steps_x+steps_y
             if (steps_x != 2 and steps_x != 3) or (steps_y != 2 and steps_y != 3):
                 continue
             
             player.goto(prev_player_x+stepsize*steps_x,prev_player_y-stepsize*steps_y)
             prev_player_x = prev_player_x+stepsize*steps_x
             prev_player_y = prev_player_y-stepsize*steps_y
             dist_x-=steps_x
             dist_y-=steps_y
            # dist = math.sqrt(dist_x**2+dist_y**2)
             
             if(dist_x == 0 and  dist_y==0):
                 # screen.title("Player lost the game!")
                 str = "Player lost the game!"
                 win=0
                 break
             
             if(dist_x<0 or dist_y<0):
                 # screen.title("Player won the game!")
                 str = "Player won the game!"
                 win=1
                 break
             
             tem_x = minimax (True, (steps_x,False) , dist_x+steps_x)
             
             steps_x_ai = tem_x[0]
             
             dist_x-=steps_x_ai
             
             tem_y = minimax (True, (steps_y,False) , dist_y-steps_y)
             
             steps_y_ai = tem_y[0]
             
             dist_y-=steps_y_ai
             #print(steps_x_ai,steps_y_ai)
             
             ai.goto(prev_ai_x-stepsize*steps_x_ai,prev_ai_y+stepsize*steps_y_ai)
             prev_ai_x = prev_ai_x-stepsize*steps_x_ai
             prev_ai_y = prev_ai_y+stepsize*steps_y_ai
             
             print(dist_x,dist_y)
             if(dist_x == 0 and dist_y ==0):
                 str = "Player lost the game!"
                 win=0
                 break
             
             if(dist_x<0 or dist_y<0):
                 str = "Player won the game!"
                 win=1
                 break
    
    if(ex[0]=='n'):
        return win
    if win != 0:
    
        ex = screen.textinput(str,"Continue to level 3(yes/no)?")
    
    if win == 0:
        return win
        
    if ex[0]=='y' :
         print("Medium:Level 3")
         screen.clearscreen()
         GRID_SIZE = 600
         screen = Screen()
         screen.title("Medium:Level 3")
         screen.bgcolor('lightblue')
         screen.bgpic("proj.gif")
         sub_divisions = 18
         #print(sub_divisions)
         
         cell_size = GRID_SIZE / float(sub_divisions)  # force float for Python 2
         
         
        
         
         player = Turtle()
         
         player.color('blue')
         
         player.shape('turtle')
         player.shapesize(0.6, 0.6, 1)
         
         ai = player.clone()
         
         ai.color('red')
         
         player.penup()
         
         player.goto(-280, 270)
         
         ai.penup()
         
         ai.goto(280, -270)
         
         
         turtle = Turtle()
         turtle.penup()
         turtle.goto(-GRID_SIZE/2, GRID_SIZE/2)
         turtle.pendown()
         turtle.speed(1000)
         
         angle = 90
         
         for _ in range(4):
             turtle.forward(GRID_SIZE)
             turtle.right(angle)
         
         for _ in range(2):
             for _ in range(1, sub_divisions):
                 turtle.forward(cell_size)
                 turtle.right(angle)
                 turtle.forward(GRID_SIZE)
                 turtle.left(angle)
         
                 angle = -angle
         
             turtle.forward(cell_size)
             turtle.right(angle)
             
         
         dist_x = sub_divisions-1
         dist_y = sub_divisions-1
         stepsize = cell_size
         prev_player_x = -280
         prev_player_y = 270
         prev_ai_x = 280
         prev_ai_y = -270
         while(dist_x>0 or dist_y >0):
             steps_x = screen.numinput("X_Steps:","Enter valid steps(2/3)")
             steps_y = screen.numinput("Y_Steps:","Enter valid steps(2/3)")
             #steps = steps_x+steps_y
             if (steps_x != 2 and steps_x != 3) or (steps_y != 2 and steps_y != 3):
                 continue
             
             player.goto(prev_player_x+stepsize*steps_x,prev_player_y-stepsize*steps_y)
             prev_player_x = prev_player_x+stepsize*steps_x
             prev_player_y = prev_player_y-stepsize*steps_y
             dist_x-=steps_x
             dist_y-=steps_y
            # dist = math.sqrt(dist_x**2+dist_y**2)
             
             if(dist_x == 0 and  dist_y==0):
                 # screen.title("Player lost the game!")
                 str = "Player lost the game!"
                 win=0
                 break
             
             if(dist_x<0 or dist_y<0):
                 # screen.title("Player won the game!")
                 str = "Player won the game!"
                 win=1
                 break
             
             tem_x = minimax (True, (steps_x,False) , dist_x+steps_x)
             
             steps_x_ai = tem_x[0]
             
             dist_x-=steps_x_ai
             
             tem_y = minimax (True, (steps_y,False) , dist_y-steps_y)
             
             steps_y_ai = tem_y[0]
             
             dist_y-=steps_y_ai
             #print(steps_x_ai,steps_y_ai)
             
             ai.goto(prev_ai_x-stepsize*steps_x_ai,prev_ai_y+stepsize*steps_y_ai)
             prev_ai_x = prev_ai_x-stepsize*steps_x_ai
             prev_ai_y = prev_ai_y+stepsize*steps_y_ai
             
             print(dist_x,dist_y)
             if(dist_x == 0 and dist_y ==0):
                 str = "Player lost the game!"
                 win=0
                 break
             
             if(dist_x<0 or dist_y<0):
                 str = "Player won the game!"
                 win=1
                 break
    if(ex[0]=='n'):
       return win
    screen.clearscreen()
    return win
        

def hard():
    GRID_SIZE = 600
    screen = Screen()
    screen.title("Medium")
    screen.bgcolor('lightblue')
    screen.bgpic("proj.gif")
    sub_divisions = 7
    #print(sub_divisions)
    win = 0
    
    cell_size = GRID_SIZE / float(sub_divisions)  # force float for Python 2
    
    
   
    
    player = Turtle()
    
    player.color('blue')
    
    player.shape('turtle')
    
    # print(player.size())
    
    ai = player.clone()
    
    ai.color('red')
    
    player.penup()
    
    player.goto(-280, 270)
    
    ai.penup()
    
    ai.goto(280, -270)
    
    
    turtle = Turtle()
    turtle.penup()
    turtle.goto(-GRID_SIZE/2, GRID_SIZE/2)
    turtle.pendown()
    turtle.speed(1000)
    
    angle = 90
    
    for _ in range(4):
        turtle.forward(GRID_SIZE)
        turtle.right(angle)
    
    for _ in range(2):
        for _ in range(1, sub_divisions):
            turtle.forward(cell_size)
            turtle.right(angle)
            turtle.forward(GRID_SIZE)
            turtle.left(angle)
    
            angle = -angle
    
        turtle.forward(cell_size)
        turtle.right(angle)
        
    
    dist_x = sub_divisions-1
    dist_y = sub_divisions-1
    stepsize = cell_size
    prev_player_x = -280
    prev_player_y = 270
    prev_ai_x = 280
    prev_ai_y = -270
    while(dist_x>0 or dist_y >0):
        steps_x = screen.numinput("X_Steps:","Enter valid steps(2/3)")
        steps_y = screen.numinput("Y_Steps:","Enter valid steps(2/3)")
        #steps = steps_x+steps_y
        if (steps_x != 2 and steps_x != 3) or (steps_y != 2 and steps_y != 3):
            continue
        
        
        player.goto(prev_player_x+stepsize*steps_x,prev_player_y-stepsize*steps_y)
        prev_player_x = prev_player_x+stepsize*steps_x
        prev_player_y = prev_player_y-stepsize*steps_y
        dist_x-=steps_x
        dist_y-=steps_y
        dist = math.sqrt(dist_x**2+dist_y**2)
        
        if(dist_x == 0 and  dist_y==0):
            # screen.title("Player lost the game!")
            str = "Player lost the game!"
            win=0
            break
        
        if(dist_x<0 and dist_y<0):
            # screen.title("Player won the game!")
            str = "Player won the game!"
            win=1
            break
        
        tem_x = minimax (True, (steps_x,False) , dist_x+steps_x)
        
        steps_x_ai = tem_x[0]
        
        dist_x-=steps_x_ai
        
        tem_y = minimax (True, (steps_y,False) , dist_y-steps_y)
        
        steps_y_ai = tem_y[0]
        
        dist_y-=steps_y_ai
        #print(steps_x_ai,steps_y_ai)
        
        ai.goto(prev_ai_x-stepsize*steps_x_ai,prev_ai_y+stepsize*steps_y_ai)
        prev_ai_x = prev_ai_x-stepsize*steps_x_ai
        prev_ai_y = prev_ai_y+stepsize*steps_y_ai
        
        print(dist_x,dist_y)
        if(dist_x == 0 and dist_y ==0):
            screen.title("Player lost the game!")
            str = "Player lost the game!"
            win=0
            break
        
        if(dist_x<0 and dist_y<0):
            screen.title("Player won the game!")
            str = "Player won the game!"
            win=1
            break
    if win != 0:
    
        ex = screen.textinput(str,"Continue to level 2(yes/no)?")
    
    if win == 0:
        return win
        
    if ex[0]=='y' :
         screen.clearscreen()
         GRID_SIZE = 600
         screen = Screen()
         screen.title("Medium:Level 2")
         screen.bgcolor('lightblue')
         screen.bgpic("proj.gif")
         sub_divisions = 14
         #print(sub_divisions)
         
         cell_size = GRID_SIZE / float(sub_divisions)  # force float for Python 2
         
         
        
         
         player = Turtle()
         
         player.color('blue')
         
         player.shape('turtle')
         
         # print(player.size())
         
         ai = player.clone()
         
         ai.color('red')
         
         player.penup()
         
         player.goto(-280, 270)
         
         ai.penup()
         
         ai.goto(280, -270)
         
         
         turtle = Turtle()
         turtle.penup()
         turtle.goto(-GRID_SIZE/2, GRID_SIZE/2)
         turtle.pendown()
         turtle.speed(1000)
         
         angle = 90
         
         for _ in range(4):
             turtle.forward(GRID_SIZE)
             turtle.right(angle)
         
         for _ in range(2):
             for _ in range(1, sub_divisions):
                 turtle.forward(cell_size)
                 turtle.right(angle)
                 turtle.forward(GRID_SIZE)
                 turtle.left(angle)
         
                 angle = -angle
         
             turtle.forward(cell_size)
             turtle.right(angle)
             
         
         dist_x = sub_divisions-1
         dist_y = sub_divisions-1
         stepsize = cell_size
         prev_player_x = -280
         prev_player_y = 270
         prev_ai_x = 280
         prev_ai_y = -270
         while(dist_x>0 or dist_y >0):
             steps_x = screen.numinput("X_Steps:","Enter valid steps(2/3)")
             steps_y = screen.numinput("Y_Steps:","Enter valid steps(2/3)")
             #steps = steps_x+steps_y
             if (steps_x != 2 and steps_x != 3) or (steps_y != 2 and steps_y != 3):
                 continue
             player.goto(prev_player_x+stepsize*steps_x,prev_player_y-stepsize*steps_y)
             prev_player_x = prev_player_x+stepsize*steps_x
             prev_player_y = prev_player_y-stepsize*steps_y
             dist_x-=steps_x
             dist_y-=steps_y
            # dist = math.sqrt(dist_x**2+dist_y**2)
             
             if(dist_x == 0 and  dist_y==0):
                 # screen.title("Player lost the game!")
                 str = "Player lost the game!"
                 win=0
                 break
             
             if(dist_x<0 or dist_y<0):
                 # screen.title("Player won the game!")
                 str = "Player won the game!"
                 win=1
                 break
             
             tem_x = minimax (True, (steps_x,False) , dist_x+steps_x)
             
             steps_x_ai = tem_x[0]
             
             dist_x-=steps_x_ai
             
             tem_y = minimax (True, (steps_y,False) , dist_y-steps_y)
             
             steps_y_ai = tem_y[0]
             
             dist_y-=steps_y_ai
             #print(steps_x_ai,steps_y_ai)
             
             ai.goto(prev_ai_x-stepsize*steps_x_ai,prev_ai_y+stepsize*steps_y_ai)
             prev_ai_x = prev_ai_x-stepsize*steps_x_ai
             prev_ai_y = prev_ai_y+stepsize*steps_y_ai
             
             print(dist_x,dist_y)
             if(dist_x == 0 and dist_y ==0):
                 str = "Player lost the game!"
                 win=0
                 break
             
             if(dist_x<0 and dist_y<0):
                 str = "Player won the game!"
                 win=1
                 break
    
    if(ex[0]=='n'):
        return win
    if win != 0:
    
        ex = screen.textinput(str,"Continue to level 3(yes/no)?")
    
    if win == 0:
        return win
        
    if ex[0]=='y' :
         print("Medium:Level 3")
         screen.clearscreen()
         GRID_SIZE = 600
         screen = Screen()
         screen.title("Medium:Level 3")
         screen.bgcolor('lightblue')
         screen.bgpic("proj.gif")
         sub_divisions = 18
         #print(sub_divisions)
         
         cell_size = GRID_SIZE / float(sub_divisions)  # force float for Python 2
         
         
        
         
         player = Turtle()
         
         player.color('blue')
         
         player.shape('turtle')
         player.shapesize(0.6, 0.6, 1)
         
         ai = player.clone()
         
         ai.color('red')
         
         player.penup()
         
         player.goto(-280, 270)
         
         ai.penup()
         
         ai.goto(280, -270)
         
         
         turtle = Turtle()
         turtle.penup()
         turtle.goto(-GRID_SIZE/2, GRID_SIZE/2)
         turtle.pendown()
         turtle.speed(1000)
         
         angle = 90
         
         for _ in range(4):
             turtle.forward(GRID_SIZE)
             turtle.right(angle)
         
         for _ in range(2):
             for _ in range(1, sub_divisions):
                 turtle.forward(cell_size)
                 turtle.right(angle)
                 turtle.forward(GRID_SIZE)
                 turtle.left(angle)
         
                 angle = -angle
         
             turtle.forward(cell_size)
             turtle.right(angle)
             
         
         dist_x = sub_divisions-1
         dist_y = sub_divisions-1
         stepsize = cell_size
         prev_player_x = -280
         prev_player_y = 270
         prev_ai_x = 280
         prev_ai_y = -270
         while(dist_x>0 or dist_y >0):
             steps_x = screen.numinput("X_Steps:","Enter valid steps(2/3)")
             steps_y = screen.numinput("Y_Steps:","Enter valid steps(2/3)")
             #steps = steps_x+steps_y
             if (steps_x != 2 and steps_x != 3) or (steps_y != 2 and steps_y != 3):
                 continue
             
             player.goto(prev_player_x+stepsize*steps_x,prev_player_y-stepsize*steps_y)
             prev_player_x = prev_player_x+stepsize*steps_x
             prev_player_y = prev_player_y-stepsize*steps_y
             dist_x-=steps_x
             dist_y-=steps_y
            # dist = math.sqrt(dist_x**2+dist_y**2)
             
             if(dist_x == 0 and  dist_y==0):
                 # screen.title("Player lost the game!")
                 str = "Player lost the game!"
                 win=0
                 break
             
             if(dist_x<0 and dist_y<0):
                 # screen.title("Player won the game!")
                 str = "Player won the game!"
                 win=1
                 break
             
             tem_x = minimax (True, (steps_x,False) , dist_x+steps_x)
             
             steps_x_ai = tem_x[0]
             
             dist_x-=steps_x_ai
             
             tem_y = minimax (True, (steps_y,False) , dist_y-steps_y)
             
             steps_y_ai = tem_y[0]
             
             dist_y-=steps_y_ai
             #print(steps_x_ai,steps_y_ai)
             
             ai.goto(prev_ai_x-stepsize*steps_x_ai,prev_ai_y+stepsize*steps_y_ai)
             prev_ai_x = prev_ai_x-stepsize*steps_x_ai
             prev_ai_y = prev_ai_y+stepsize*steps_y_ai
             
             print(dist_x,dist_y)
             if(dist_x == 0 and dist_y ==0):
                 str = "Player lost the game!"
                 win=0
                 break
             
             if(dist_x<0 or dist_y<0):
                 str = "Player won the game!"
                 win=1
                 break
    if(ex[0]=='n'):
       return win
    screen.clearscreen()
    return win
        
def main():
    screen = Screen()
    
    screen.title("Catch me if You can")
    
    screen.bgcolor('lightblue')
    
    
    
    screen.bgpic("proj.gif")
    
    screen.clearscreen()
    difficulty = set_difficulty()
    
    
    # x = screen.numinput("Enter distance:",100)
    if difficulty == 'e' or difficulty == 'E':
        win = easy()
    
    elif  difficulty == 'm' or difficulty == 'M':
        win =  medium()
       
    elif difficulty == 'h'or difficulty == 'H':
        win = hard()
    
    loop(win)
    


def loop(win):
    print(win)
    screen = Screen()
    
    screen.title("Catch me if You can")
    
    screen.bgcolor('lightblue')
    
    screen.bgpic("proj.gif")
       
    if(win != 0):
        ex = screen.textinput("You won the game","want to continue(yes/no)?")
        if(ex[0]=='y'):
            main()
        else:
            screen.bye()
    if win == 0:
        ex = screen.textinput("You lost the game","want to play again(yes/no)?")
        if(ex[0]=='y'):
            main()
        else:
            screen.bye()

main()
    

#ex = screen.textinput(str,"Exit the game(yes/no)?")

#if ex != "":
   # screen.bye()
#screen.exitonclick()