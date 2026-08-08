from pygame import *

width = 700
height = 500
window = display.set_mode((width, height))
background_color = (25, 184, 209)
window.fill(background_color)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #e.g. 55,55 - parameters
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Racket(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 10:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - 10:
            self.rect.y += self.speed

racket1 = Racket('racket.png', 30, 200, 4, 50, 150)
racket2 = Racket('racket.png', 600, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

game = True
FPS = 60
clock = time.Clock()

speed_x = 3
speed_y = 5
finish = False

font.init()
font = font.Font(None, 35)
lose1 = font.render('Left Player Lose!', True, (180, 0, 0))
lose2 = font.render('Right Player Lose!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(background_color)

        racket1.reset()
        racket1.update()
        racket1.update_l()

        racket2.reset()
        racket2.update()
        racket2.update_r()

        ball.reset()
        ball.update()

        # Bola bergerak horizontal karena 2 program ini yang bekerja secara bersamaan
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        # Bola ketika terkena dinding maka akan memantul
        if ball.rect.y > height - 10 or ball.rect.y < 0:
            speed_y *= -1

        # Bola mantul pas kena raket
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= -1

        # Program jika player kiri kalah
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        # Program jika player kanan kalah
        if ball.rect.x > width:
            finish = True
            window.blit(lose2, (200, 200))


        display.update()
    clock.tick(FPS)
