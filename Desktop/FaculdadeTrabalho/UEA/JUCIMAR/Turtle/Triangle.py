# biblioteca que permite a utilização de formas através de comandos
import turtle

# abre a tela de visualização
TurtleVisualization = turtle.Screen()

# creating tess object
drawing = turtle.Turtle()


def criar_triangulo(x, y):
    # desenha a caneta
    drawing.penup()

    # move o cursor para posição predeterminada
    drawing.goto(x, y)

    # it is used to draw in the pen
    drawing.pendown()

    for i in range(3):

        # move a caneta 100 unidades para frente do clique
        drawing.forward(100)

        # move a caneta 120 graus para a esquerda
        drawing.left(120)

        # move mais 100 unidades para frente
        drawing.forward(100)


# informa a posição atual do cursor para a função

turtle.onscreenclick(criar_triangulo, 1)  # número 1 representa o clique esquerdo
turtle.onscreenclick(criar_triangulo, 3)  # número 3 representa o clique direito


# mantém a tela aberta
turtle.done()
