# biblioteca que permite a utilização de formas através de comandos
from turtle import *

# define a velocidade da tartaruga
speed('fastest')

# rotacionando a tartaruga em 90 graus
rt(-90)

# definição do ângulo entre a base do Y e seus "ramos"
angle = 30


# função para desenhar um formato de 'Y'
def draw_y_shape(sz, level):

    if level > 0:

        colormode(255)

        # muda o modo de cor para rgb e define o tom de verde em intervalos proporcionais ao nível
        pencolor(0, 255 // level, 0)

        # desenhando a base
        fd(sz)

        # mais uma rotação com ângulo definido previamente
        rt(angle)

        # chamada para o desenho da parte esquerda
        draw_y_shape(0.8 * sz, level - 1)

        pencolor(0, 255 // level, 0)

        # mais uma rotação de direção, dessa vez para a esquerda e com ângulo maior
        lt(2 * angle)

        # chamada para o desenho da parte direita
        draw_y_shape(0.8 * sz, level - 1)

        pencolor(0, 255 // level, 0)

        rt(angle)
        fd(-sz)


# definição de tamanho e nível da árvore
draw_y_shape(80, 7)
