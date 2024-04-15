print("hello world")

import turtle

TURTLEDRAWTEXT = 'turtledraw.txt'

# Todo: Ask user for the file name. 

print('TurtleDraw AW')


turtleDraw10 = turtle.Turtle()
turtleDrawScreen = turtle.Screen()
turtleDrawScreen.setup(450, 450)
turtleDraw10.speed(10)
turtleDraw10.penup()

turtleDrawTextfile = open(TURTLEDRAWTEXT, 'r')
line = turtleDrawTextfile.readline()
while line: 
    print(line, end='')
    parts = line.split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        
        turtleDraw10.color(color)
        turtleDraw10.goto(x,y)
        turtleDraw10.pendown()

    if (len(parts) == 1):
        turtleDraw10.penup()

line = turtleDrawTextfile.readline()


turtle.done()
turtleDrawTextfile.close()
