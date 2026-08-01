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

racket1 = GameSprite('racket.png', 30, 200, 4, 50, 150)
racket2 = GameSprite('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

game = True
FPS = 60
clock = time.Clock()


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    racket1.reset()
    racket1.update()

    racket2.reset()
    racket2.update()

    ball.reset()
    ball.update()


    display.update()
    clock.tick(FPS)
