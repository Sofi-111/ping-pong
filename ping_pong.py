from pygame import *

GAME = True
FPS = 60
WIN_WIDTH = 700
WIN_HEIGH = 500
BACK = (180, 230, 255)
FINISH = False
SPEED_X = 3
SPEED_Y = 3
RED = (225, 0, 0)

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

font.init()
font = font.Font(None, 70)
lose1 = font.render('Игрок 1 проиграл!', True, RED)
lose2 = font.render('Игрок 2 проиграл!', True, RED)

#создание ракеток и мяча
racket1 = Player('images/bullet.png', 30, 200, 50, 150, 4)
racket2 = Player('images/bullet.png', 620, 200, 50, 150, 4)
ball = GameSprite('images/asteroid.png', 330, 250, 50, 50, 4)

while GAME == True:

    for e in event.get():
        if e.type == QUIT:
            GAME = False

    if FINISH != True:
        window.fill(BACK)
        racket1.reset()
        racket2.reset()
        ball.reset()
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += SPEED_X
        ball.rect.y += SPEED_Y

    if ball.rect.y > WIN_HEIGH- 50 or ball.rect.y < 0:
        SPEED_Y *= -1

    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        SPEED_X *= -1
    
    if ball.rect.x < 0:
        FINISH = True
        window.blit(lose1, (160, 200))

    if ball.rect.x > WIN_WIDTH:
        FINISH = True
        window.blit(lose2, (160, 200))

    display.update()
    clock.tick(FPS)
