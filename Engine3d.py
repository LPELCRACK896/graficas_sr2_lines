import math
from gl import Renderer, NewColor, V2
width, height = 1024, 512
rend = Renderer(width, height)
def drawFigure(vertices, clr = None):
    for i in range(len(vertices)):
        rend.glLine(vertices[i], vertices[(i+1)%len(vertices)], clr)
#Lineas
# y = mx+b
v1 = V2(0, 250)
v0 = V2(50, 50)
rend.glClear()

#----------------Cuadrado----------------
vertices_de_cuadrado = [V2(100, 100), V2(100, 200), V2(200, 200), V2(200, 100)]
color_poligono = NewColor(1, 0, 0)
drawFigure(vertices_de_cuadrado, color_poligono)
#----------------Triangulo----------------
vertices_de_triangulo = [V2(250, 100), V2(450, 100), V2(350, 273)]
color_poligono_2 = NewColor(0, 1, 0)
drawFigure(vertices_de_triangulo, color_poligono_2)
#----------------Paralelogramo----------------
vertices_de_paralelogramo = [V2(500, 100), V2(600, 200), V2(800, 200), V2(700, 100)]
color_poligono_3 = NewColor(0, 0, 1)
drawFigure(vertices_de_paralelogramo, color_poligono_3)
#----------------Rombo----------------
vertices_de_rombo = [V2(150, 300), V2(200, 350), V2(150, 400), V2(100, 350)]
color_poligono_4 = NewColor(1, 1, 0)
drawFigure(vertices_de_rombo, color_poligono_4)
#----------------Hexagono----------------
vertices_de_hexagono = [V2(250, 371), V2(321, 300), V2(421, 300), V2(492, 371),V2(421, 442),V2(321, 442)]
color_poligono_5 = NewColor(1, 127/255, 0)
drawFigure(vertices_de_hexagono, color_poligono_5)


rend.glFinish('output.bmp')
print('Fin de programa')