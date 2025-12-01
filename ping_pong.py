from pygame import *

GAME = True
FPS = 60
WIN_WIDTH = 700
WIN_HEIGH = 500
BACK = (180, 230, 255)

#создание сцены
window = display.set_mode((WIN_WIDTH, WIN_HEIGH))
display.set_caption('Ping-pong')
window.fill(BACK)

clock = time.Clock()

while GAME == True:
    for e in event.get():
        if e.type == QUIT:
            GAME = False

    display.update()
    clock.tick(FPS)