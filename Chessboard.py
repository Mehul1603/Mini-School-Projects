import turtle
turtle.screensize(canvwidth=1000, canvheight=1000, bg='white')
turtle.speed(10)
turtle.color('black')
turtle.hideturtle()

y = -400

turtle.penup()

for i in range(8):
    
    if (i-1)%2 == 1:
        x = -400
    else:
        x = -300
        
    for j in range(4):

        turtle.goto(x,y)
        turtle.pendown()
        
        turtle.begin_fill()
        for m in range(4):
            turtle.forward(100)
            turtle.left(90)
        turtle.end_fill()

        turtle.penup()
        x += 200

    y += 100

turtle.goto(-400,400)
turtle.color('black')
turtle.pendown()
for m in range(4):
    turtle.forward(800)
    turtle.right(90)
turtle.penup()

            
