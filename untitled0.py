from turtle import Screen, Turtle
import math

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


GRID_SIZE = 600


screen = Screen()
sub_divisions = int(screen.numinput("Grid size:","Enter n for nXn Grid Size(5/7/9)"))
print(sub_divisions)

cell_size = GRID_SIZE / float(sub_divisions)  # force float for Python 2


screen.title("")

screen.bgcolor('lightblue')



screen.bgpic("proj.gif")

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
  #  if steps != 2 and steps != 3 and steps != 4 and steps != 5:
   #     continue
    
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
    if(dist_x == 0 or dist_y ==0):
        screen.title("Player lost the game!")
        str = "Player lost the game!"
        win=0
        break
    
    if(dist_x<0 and dist_y<0):
        screen.title("Player won the game!")
        str = "Player won the game!"
        win=1
        break
ex = screen.textinput(str,"Press any character(a-z)")

if ex != "":
    screen.bye()
screen.exitonclick()