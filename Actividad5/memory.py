"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
numTaps = 0 #Inicializar contador taps
reveladas = 0 #Inicializar contador de tarjetas reveladas

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global numTaps, reveladas #Convertir a variables globales para modificaciones
    spot = index(x, y)
    mark = state['mark']
    numTaps+=1 #Aumentar el numero de taps al ejecutar la funcion

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        reveladas+=1 #Aumentar el contador de acuerdo al estado de la tarjeta
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 27, y) #Centrar
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align="center") #Centrar y alinear el digito
    
    if (reveladas==32): #Evalua si todas las cartas ya fueron reveladas
        goto(60,203)
        write("Ganaste!", font=("Arial",20))

    update()
    goto(-200,203)
    write("Taps:"+str(numTaps), font=('Arial',20)) #Imprime el numero de taps
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
