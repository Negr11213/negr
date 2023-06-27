#создай игру "Лабиринт"!
from pygame import *
import pygame
pygame.init()
mixer.init()

WIDTH = 700
HEIGHT = 500
FPS = 60 

wi = display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, p1x, p1y, player_speen):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = p1x
        self.rect.y = p1y
        self.speen = player_speen


    def reset(self):
        wi.blit(self.image, (self.rect.x, self.rect.y))



display.set_caption("Лабиринт")

#работа со звуками
mixer.music.load("jungles.ogg")
mixer.music.play()

class Player (GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speen
        if keys [K_RIGHT] and self.rect.x < WIDTH - 80:
            self.rect.x += self.speen
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speen 
        if keys [K_DOWN] and self.rect.y < HEIGHT - 80:
            self.rect.y += self.speen

hero = Player('hero.png', 100, 300, 5)

class Enemy (GameSprite):
    def  update (self):
        if self.rect.x <= 450:
            self.direction = "right"
        elif self.rect.x >= WIDTH - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speen
        else:
            self.rect.x += self.speen


class Wall(pygame.sprite.Sprite):
    """
    Класс стены

    Keyword arguments:

    color -- цвет стены, RGB;

    wall_x -- позиция стены по X;

    wall_y -- позиция стены по Y;

    wall_width -- ширина стены;

    wall_height -- высота стены;

    screen -- поверхность, на которой будет стена;
    """

    def __init__(
        self,
        color: tuple,
        wall_x: int,
        wall_y: int,
        wall_width: int,
        wall_height: int,
        screen: pygame.Surface,
    ):
        super().__init__()
        self.color = color
        self.width = wall_width
        self.height = wall_height
        # картинка стены - прямоугольник нужных размеров и цвета
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)
        # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.screen = screen

    def draw_wall(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))


w1 = Wall((55, 66, 77), 165, 70, 30, 450, wi)
w2 = Wall((55, 66, 77), 265, -30, 30, 450, wi)
w3 = Wall((55, 66, 77), 365, 70, 30, 450, wi)
w4 = Wall((55, 66, 77), 465, -30, 30, 450, wi)
w5 = Wall((55, 66, 77), 665, 70, 500, 500, wi)
cyborg = Enemy('cyborg.png', 450, 350, 5)

background = transform.scale(image.load("background.jpg"), (700, 500))
game = True

while game:
    clock.tick(FPS)
    wi.blit(background,(0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    hero.reset()
    cyborg.reset()
    hero.update()
    cyborg.update()
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    w4.draw_wall()
    w5.draw_wall()
    display.update()



