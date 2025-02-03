
'''STAR PATTERN
import turtle
star=turtle.Turtle()
star.fillcolor("red")
star.begin_fill()
star.right(75)
star.forward(100)
for i in range(4):
    star.right(144)
    star.forward(100)
star.end_fill()
turtle.done()
'''
'''SQUARE PATTERN
import turtle
s=turtle.Turtle()
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.hideturtle()  #it hides the arrow
'''
'''using loop
import turtle
s=turtle.Turtle()
for i in range(4):
    s.forward(100)  #moves the turtle forward by the specified amount
    s.left(90)  #turns the turtle in anticlock wise
turtle.done()
'''
'''using penup and pendown
import turtle
s=turtle.Turtle()
s.forward(100)
s.penup()  #picks up the turtle's pen
s.right(90)
s.forward(100)
s.right(90)
s.pendown()  #puts down the turtle's pen
s.forward(100)
'''
'''COLOUR FILLING
import turtle
s=turtle.Turtle()
s.fillcolor("black")

s.begin_fill()  #start colour filling inside
for i in range(4):
    s.forward(100)
    s.right(90)
s.end_fill()  #completing the colour

'''

'''Drawing heart include name
import turtle
s=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("black")
s.fillcolor("red")
s.begin_fill()
s.right(45)
s.forward(100)
s.left(90)
s.forward(100)
s.circle(50,180)
s.right(90)
s.circle(50,180)
s.end_fill()
s.write("DUKE",align="left",font=("Arial", 37, "bold","italic"))
'''
'''Draw the rangoli'''
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
spiral = turtle.Turtle()
spiral.speed(20)
spiral.width(3)
colors = ["red","green","orange", "yellow",  "blue", "purple","teal"]
for i in range(360):
    spiral.color(colors[i % 7]) 
    spiral.forward(i)
    spiral.right(0)
    spiral.left(100)
turtle.done()

















