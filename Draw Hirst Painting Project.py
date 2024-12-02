import turtle as t
import random
timy=t.Turtle()
t.colormode(255)
timy.shape("turtle")
timy.color("blue")
timy.penup()
timy.speed("fastest")
timy.hideturtle()

def colour():
  r=random.randint(0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  return (r,g,b)
timy.speed(9)
timy.setheading(225)
timy.forward(320)
timy.dot(30,colour())
timy.setheading(0)
def line():
  
  for i in range(10):
    timy.forward(50)
    timy.dot(30,colour())
line()
for i in range(10):
  
  timy.left(90)
  timy.forward(50)
  timy.setheading(180)
  timy.dot(30,colour())
  line()
  timy.setheading(0)
  timy.forward(500)










screen=t.Screen()
screen.exitonclick()
