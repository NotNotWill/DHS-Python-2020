import time
from turtle import *
color('red', 'black')
begin_fill()

### Square with X

turnangle = 90
for side in range(4):
  forward(90)
  left(90)
left(0.5*turnangle)
forward(127)

right(135)
forward(90)

right(1.50*turnangle)
forward(127)

backward(63.5)

time.sleep(1)

clear()

### Multi-Colored Circle

color('red')
circle(50)
color('yellow')
circle(40)
color('orange')
circle(30)
color('blue')
circle(20)
color('purple')
circle(10)

time.sleep(1)

clear()

### Hexagon

color('red')
forward(70)
left(60)
forward(70)
left(60)
forward(70)
left(60)
forward(70)
left(60)
forward(70)
left(60)
forward(70)

time.sleep(1)
clear()

### Star (Normal)

color('red')
forward(100)
right(144)
forward(100)
right(144)
forward(100)
right(144)
forward(100)
right(144)
forward(100)