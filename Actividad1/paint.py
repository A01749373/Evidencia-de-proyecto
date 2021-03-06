"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
import turtle as t
from freegames import vector
import math

def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    up()
    rx= (end.x-start.x)/2  #Radio de acuerdo a la distancia x
    ry= (end.y-start.y)/2  #Radio de acuerdo a la distancia y
    goto(start.x+rx, start.y+ry) #Posicion de inicio del circulo
    down()
    begin_fill()
    r=math.sqrt((end.x-start.x)**2+(end.y-start.y)**2) #Distancia entre puntos x,y
    t.circle(r)
    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        if(count%2==0):
            forward(end.x - start.x) #Ancho del rectangulo
        else: 
            forward((end.x - start.x)/2) #Alto del rectangulo
        left(90)
    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    rx = (end.x - start.x)/2 #Distancia x
    ry = (end.y - start.y)/2 #Distancia y
    goto(start.x + rx, start.y + ry) #Posicion de inicio del triangulo
    down()
    begin_fill()
    r = math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2) #Distancia entre puntos x, y
    t.circle(r, steps=3) #Numero de lados de la figura
    end_fill()



def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('#ACE7FF'), 'P') #Agregar un color
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
