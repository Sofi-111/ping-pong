from pygame import *

GAME = True
FPS = 60
WIN_WIDTH = 700
WIN_HEIGH = 500
BACK = (180, 230, 255)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_hight, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_hight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < WIN_HEIGH - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < WIN_HEIGH - 80:
            self.rect.y += self.speed

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

