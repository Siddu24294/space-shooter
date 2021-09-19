import math
import turtle


s=turtle.Screen()
s.bgcolor("black")
s.title("space invaders")

#outline is the turtle for outline
outline=turtle.Turtle()
outline.speed(0)
outline.color("#6f66c4")
outline.penup()
outline.setposition(-300,-300)
outline.pensize(3)
outline.pendown()
for i in range(4):
    outline.fd(600)
    outline.lt(90)
outline.hideturtle()

#score turtle and count score
scoreee= 0
scor=turtle.Turtle()
scor.color("red")
scor.hideturtle()
scor.penup()
scor.setposition(-260,310)
scor.write("score:",align='right',font=('Arial',12,'bold'))

#sid is the player turtle
sid=turtle.Turtle()
sid.speed(0)
sid.penup()
sid.shape("triangle")
sid.color("#0792ef")
sid.setposition(0,-250)
sid.setheading(90)
speed=15

#BULLet IS THE WEAPON TURTLE
bull=turtle.Turtle()
bull.speed(0)
bull.shape("triangle")
bull.color("yellow")
bull.setheading(90)
bull.shapesize(0.5,0.5)
bull.penup()
bull.hideturtle()
bull_speed=20

#state of bull
bull_state= "ready"

#enemy
bot=turtle.Turtle()
bot.color("#ed9d4e")
bot.shape("circle")
bot.penup()
bot.speed(0)
bot.setposition(-200,250)

bot_speed=2

#move the player left and right
def leftt():
    x=sid.xcor()
    x -= speed
    if x < -280:
        x= -280
    sid.setx(x)


def rightt():
    x=sid.xcor()
    x += speed
    if (x > 280):
        x= 280
    sid.setx(x)


#move the bull just above the player
def bullt():
    global bull_state
    if bull_state== "ready":
        bull_state= "fire"
        x = sid.xcor()
        y = sid.ycor()
        bull.setposition(x,y+10)
        bull.showturtle()


#checking collision
def iscollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<15:
        return True
    else :
        return False


#keyboard bindings
turtle.onkey(leftt,"Left")
turtle.onkey(rightt,"Right")
turtle.onkey(bullt,"space")
turtle.listen()

'''main game loop'''
while True:

    #move bot
    x=bot.xcor()
    x += bot_speed
    x=bot.setx(x)

    # bounce enemy
    if bot.xcor()>280:
        y = bot.ycor()
        y-=50
        bot.sety(y)
        bot_speed *= -1
    if bot.xcor()<-280:
        bot_speed *= -1
        y = bot.ycor()
        y-=40
        bot.sety(y)

    #move the bull
    if bull_state== "fire":
        y=bull.ycor()
        y+=bull_speed
        bull.sety(y)

    #if the  bull has gone above the boundary
    if bull.ycor()>275:
        bull.hideturtle()
        bull_state= "ready"
    #collision check
    if iscollision(bull,bot):
        #count the score
        scoreee=scoreee+1
        scor.clear()
        scor.write("score:",align='right',font=('Arial',12,'bold'))
        scor.write(scoreee,align='left',font=('Arial',12,'bold'))
        #hide the bullet
        bull.hideturtle()
        bull_state= "ready"
        bull.setposition(0,-400)
        #set the enemy
        bot.setposition(-200,250)

    if iscollision(sid,bot):
        sid.hideturtle()
        bot.hideturtle()
        r=turtle.Turtle()
        r.hideturtle()
        r.speed(3)
        r.color("red")
        r.penup()
        r.forward(-90)
        r.pendown()
        r.left(90)
        r.forward(20)
        r.left(90)
        r.forward(50)
        r.left(90)
        r.forward(70)
        r.left(90)
        r.forward(50)
        r.left(90)
        r.forward(30)
        r.left(90)
        r.forward(15)
        r.left(180)
        r.forward(20)
        r.penup()
        r.right(90)
        r.forward(30)
        r.left(90)
        r.forward(35)
        r.pendown()
        for i in range(3):
            r.left(90)
            r.forward(30)
        r.left(90)
        r.forward(35)
        r.penup()
        r.forward(5)
        r.pendown()
        r.left(90)
        r.forward(30)
        r.right(90)
        r.forward(20)
        r.right(90)
        r.forward(30)
        r.right(180)
        r.forward(30)
        r.right(90)
        r.forward(20)
        r.right(90)
        r.forward(30)
        r.penup()
        r.left(90)
        r.forward(5)
        r.pendown()
        r.left(90)
        r.forward(30)
        r.left(-90)
        r.forward(20)
        r.left(-90)
        r.forward(10)
        r.left(-90)
        r.forward(20)
        r.left(90)
        r.forward(20)
        r.left(90)
        r.forward(20)
        r.penup()
        r.forward(10)
        r.pendown()
        r.forward(50)
        r.left(90)
        r.forward(70)
        r.left(90)
        r.forward(50)
        r.left(90)
        r.forward(70)
        r.left(90)
        r.forward(50)
        r.penup()
        r.forward(5)
        r.left(90)
        r.forward(30)
        r.pendown()
        r.right(90+71.58)
        r.forward(31.62)
        r.left(71.58+71.58)
        r.forward(31.62)
        r.penup()
        r.right(90+71.58)
        r.forward(30)
        r.left(90)
        r.forward(5)
        r.pendown()
        r.left(90)
        r.forward(30)
        r.left(-90)
        r.forward(20)
        r.left(-90)
        r.forward(10)
        r.left(-90)
        r.forward(20)
        r.left(90)
        r.forward(20)
        r.left(90)
        r.forward(20)
        r.penup()
        r.forward(15)
        r.pendown()
        r.left(90)
        r.forward(30)
        r.left(90)
        r.forward(10)
        r.left(90)
        r.forward(10)
        r.left(90)
        r.forward(30)
        r.left(-90)
        r.forward(21)
        r.left(90)
        r.penup()
        r.forward(20)
        r.right(90)
        r.forward(20)
        r.pendown()
        r.left(90)
        for i in range(2):
            r.left(90)
            r.forward(110)
            r.left(90)
            r.forward(350)
        break
