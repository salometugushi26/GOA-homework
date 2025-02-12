from turtle import *

speed(30)
width(7)
color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
begin_fill()
color("brown")
left(90)
forward(120)
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

penup()
goto(0, 0)
pendown()
color("black", "white")
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()

penup()
goto(0, 25)
pendown()
color("black")
forward(50)

penup()
goto(25, 0)
pendown()
left(90)
forward(50)

penup()
goto(0, 25)
pendown()
color("black")
forward(50)

penup()
goto(25, 0)
pendown()
left(90)
forward(50)

penup()
goto(-80, 0)
pendown()
right(90)
color("black", "white")
begin_fill()
for_i_in_range (4)
forward(50)
left(90)

end_fill

exitonclick
