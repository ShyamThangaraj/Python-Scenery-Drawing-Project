import turtle
import random
t1 = turtle.Turtle()
t1.shape("turtle")
t1.speed(0)
t1.penup()

def background():
  t1.penup()
  t1.goto(-200,-200)
  
  #sand
  t1.color("wheat")
  t1.begin_fill()
  for i in range(2):
    t1.fd(400)
    t1.left(90)
    t1.fd(175)
    t1.left(90)
  t1.end_fill()
  
  t1.penup()
  t1.goto(-200,-25)
  
  #beach
  t1.color("cornflower blue")
  t1.begin_fill()
  for i in range(2):
    t1.fd(400)
    t1.left(90)
    t1.fd(100)
    t1.left(90)
  t1.end_fill()

  #sky
  t1.color("light sky blue")
  t1.begin_fill()
  t1.penup()
  t1.seth(90)
  t1.fd(100)
  t1.pendown()
  t1.seth(0)
  t1.fd(400)
  t1.seth(90)
  t1.fd(125)
  t1.seth(180)
  t1.fd(400)
  t1.seth(270)
  t1.fd(125)
  t1.seth(0)
  t1.end_fill()

  #sun
  t1.color("yellow")
  t1.penup()
  t1.goto(-200,125)
  t1.begin_fill()
  t1.pendown()
  t1.seth(0)
  t1.circle(100,74)
  t1.seth(180)
  t1.fd(100)
  t1.left(90)
  t1.fd(70)
  t1.end_fill()
  t1.penup()
  t1.goto(-200,125)
  t1.pendown()
  t1.pensize(4)
  t1.color("orange")
  t1.seth(0)
  t1.circle(100,74)
   
  t1.pensize(1) 
  
  #waves
  t1.penup()
  t1.color("royal blue")
  t1.goto(-230, 75)
  t1.seth(30)
  t1.pendown()

  t1.begin_fill()
  for i in range(4):
    t1.fd(30)
    for x in range(5):
      t1.right(5)
      t1.fd(10)
    t1.seth(225)
    t1.fd(20)
    t1.seth(17)
    for j in range(5):
      t1.right(3)
      t1.fd(10)
    t1.seth(40)
    t1.fd(-20)
    for i in range(5):
      t1.seth(30)
      t1.right(5)
      t1.fd(10)
    t1.seth(225)
    t1.fd(41)
    t1.seth(30)
  t1.end_fill()
  
    
def umbrella_two():
  t1.speed(0)
  t1.penup()
  t1.goto(-150,-190)
  t1.seth(270)
  t1.color("gray")
  t1.pendown()
  t1.begin_fill()
  for i in range(5):
    t1.left(30)
    t1.fd(4)
  t1.seth(90)
  t1.fd(160)
  for i in range(5):
    t1.left(30)
    t1.fd(4)
  t1.seth(270)
  t1.fd(10)
  t1.end_fill()
  t1.penup()
  t1.color("tomato")
  t1.begin_fill()
  t1.penup()
  t1.goto(-270,-10)
  t1.seth(340)
  t1.circle(400,38)
  t1.goto(-150,100)
  t1.goto(-270,-10)
  t1.end_fill()

def chair():
  t1.speed(0)
  t1.penup()
  t1.penup()
  t1.goto(-85,-130)
  t1.begin_fill()
  t1.penup()
  t1.seth(90)
  t1.color("midnight blue")
  t1.fd(75)
  for i in range(7):
    t1.fd(3)
    t1.right(13)
  t1.seth(0)
  t1.fd(85)
  for i in range(7):
    t1.fd(3)
    t1.right(13)
  t1.seth(270)
  t1.fd(75)
  t1.seth(180)
  t1.fd(10)
  t1.seth(90)
  t1.fd(62)
  for i in range(7):
    t1.fd(3)
    t1.left(13)
  t1.seth(180)
  t1.fd(65)
  for i in range(7):
    t1.fd(3)
    t1.left(13)
  t1.seth(270)
  t1.fd(68)
  t1.seth(180)
  t1.fd(10)
  t1.penup()
  t1.end_fill()
  t1.seth(0)
  t1.penup()
  t1.fd(5)
  t1.pendown()
  t1.pensize(13)
  t1.color("steel blue")
  t1.fd(103)
  t1.penup()
  t1.seth(90)
  t1.fd(30)
  cList = ["medium purple", "lime green"]
  for i in range(1):
    t1.color(cList[0])
    t1.pendown()
    t1.seth(180)
    t1.fd(102)
    t1.seth(90)
    t1.penup()
    t1.fd(30)
    t1.pendown()
    t1.seth(0)
    t1.color(cList[1])
    t1.fd(102)
    t1.seth(90)
    t1.penup()
    t1.fd(30)
    t1.pendown()
  t1.penup()
  t1.goto(-85,-130)
  t1.seth(0)
  t1.fd(5)
  t1.seth(270)
  
  #chair seat
  t1.seth(315)
  t1.color("midnight blue")
  t1.pendown()
  t1.fd(75)
  t1.seth(0)
  t1.fd(102)
  t1.seth(135)
  t1.fd(75)
  t1.color(cList[0])
  t1.penup()
  t1.fd(-25)
  t1.seth(180)
  t1.pendown()
  t1.fd(102)
  t1.fd(-102)
  t1.penup()
  t1.seth(315)
  t1.fd(25)
  t1.seth(180)
  t1.color(cList[1])
  t1.pendown()
  t1.fd(102)
  t1.penup()
  t1.seth(315)
  t1.fd(25)
  t1.seth(270)
  t1.pendown()
  t1.color("midnight blue")
  t1.fd(30)
  t1.penup()
  t1.seth(0)
  t1.fd(102)
  t1.seth(90)
  t1.pendown()
  t1.fd(30)
  t1.penup()
  t1.seth(180)
  t1.fd(102)
  t1.seth(270)
  t1.fd(30)
  t1.seth(135)
  t1.fd(75)
  t1.seth(90)
  t1.pendown()
  t1.fd(25)
  t1.penup()
  
def ball():
  t1.speed(0)
  x = random.randint(-200, 200)
  y = random.randint(-200,200)
  t1.seth(0)
  t1.fd(185)
  t1.pensize(2)
  t1.pendown()
  t1.color("white smoke")
  t1.begin_fill()
  t1.circle(40)
  t1.end_fill()
  t1.seth(90)
  t1.color("blue")
  t1.fd(80)
  t1.penup()
  t1.shape("")
  t1.fd(-70)
  t1.seth(0)
  t1.fd(27)
  t1.seth(90)
  t1.color("crimson")
  t1.pendown()
  t1.fd(60)
  t1.penup()
  t1.fd(-60)
  t1.seth(180)
  t1.fd(53)
  t1.seth(90)
  t1.pendown()
  t1.fd(60)
  t1.penup()

def clouds():
  t1.color("white smoke")
  t1.speed(0)
  t1.pensize(1)
  t1.goto(-75,150)
  t1.seth(270)
  t1.pendown()
  t1.begin_fill()
  for x in range(5):
    for i in range(15):
      t1.left(7)
      t1.fd(1.5)
    t1.right(90)
  t1.seth(90)
  for i in range(5):
    for x in range(15):
      t1.left(7)
      t1.fd(1.5)
    t1.right(90)
  t1.end_fill()
  t1.penup()
  t1.seth(0)
  t1.fd(150)
  t1.seth(270)
  t1.pendown()
  t1.begin_fill()
  for x in range(5):
    for i in range(15):
      t1.left(7)
      t1.fd(1.5)
    t1.right(90)
  t1.seth(90)
  for i in range(5):
    for x in range(15):
      t1.left(7)
      t1.fd(1.5)
    t1.right(90)
  t1.end_fill()

background()
umbrella_two()
chair()
ball()
clouds()
