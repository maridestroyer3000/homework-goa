from turtle import *


#we want to paint a house

#step 1: draw a square
shape("turtle")
speed(30)
width(7)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of triangle

#drawing a window

left(120)
forward(200)
color("purple")
right(90)
forward(90)
right(90)
forward(30)
color("brown")
begin_fill()
right(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)
left(90)
forward(34)
end_fill()

color("purple")
forward(25)
right(90)
forward(110)
right(90)
forward(200)
right(90)
forward(110)
right(90)
forward(30)
color("brown")
begin_fill()
left(90)
forward(60)
right(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
end_fill()

exitonclick()