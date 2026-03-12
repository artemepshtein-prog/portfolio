import pygame
import random

pygame.init()


width = 1200
height = 800
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('cats bombing rats simulator')
clock = pygame.time.Clock()

background_image = pygame.image.load('images/bg.png')
background_image = pygame.transform.scale(background_image, (width, height))


class Plane():
    def __init__(self):
        self.image = pygame.image.load('images/plane.png')
        self.image = pygame.transform.scale(self.image, (160, 100))
        self.rect = self.image.get_rect(x=0, y=50)
        self.direction = 1  # 1 - вправо, -1 - влево
        self.speed = 5

        self.bomb_img = pygame.image.load('images/bomb.png')
        self.bomb_img = pygame.transform.scale(self.bomb_img, (40, 40))

        self.img_explosion = pygame.image.load('images/explosion.png')
        self.img_explosion = pygame.transform.scale(self.img_explosion, (160, 100))

        self.bombs_list = []
        self.current_image = self.image
        self.plane_destroy = False

    def update(self):
        if self.rect.colliderect(rat.rocket_rect):
            self.plane_destroy = True
            self.current_image = self.img_explosion
        if self.rect.right >= width:
            self.direction = -1
        elif self.rect.left <= 0:
            self.direction = 1

        if self.direction == -1 and self.plane_destroy == False:
            self.rect.x -= self.speed
            self.current_image = self.image
        elif self.direction == 1 and self.plane_destroy == False:
            self.rect.x += self.speed
            self.current_image = pygame.transform.flip(self.image, True, False)
        elif self.plane_destroy == True:
            self.rect.y +=3
            if self.rect.y == height:
                self.plane_destroy = False
                self.direction = -1
                self.current_image = self.image




        if self.rect.x % 230 == 0:
            new_bomb_rect = self.bomb_img.get_rect(center=(self.rect.centerx, self.rect.bottom))
            self.bombs_list.append(new_bomb_rect)

    def bombs(self):
        for b_rect in self.bombs_list[:]:
            b_rect.y += 3
            display.blit(self.bomb_img, b_rect)

    def draw(self):
        display.blit(self.current_image, self.rect)

class Player():
    def __init__(self):
        self.image = pygame.image.load('images/cat.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

    def update(self, x, y, cat_dir):
        self.rect.y = y - 13
        if cat_dir == -1:
            image = pygame.transform.flip(self.image, True, False)
            self.rect.x = x + 10
        else:
            image = self.image
            self.rect.x = x + 50
        display.blit(image, self.rect)

class Rat():
    def __init__(self):
        self.image = pygame.image.load("images/mouse.png")
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect(x = width //2 - 30, y = height - 100)

        self.rocket_img = pygame.image.load('images/rocket.png')
        self.rocket_img = pygame.transform.scale(self.rocket_img, (90, 60))
        self.rocket_rect = self.rocket_img.get_rect(x = self.rect.x + 10, y = height - 120)
        self.start_rocket = False
    def rocket(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.start_rocket = True
        if self.start_rocket == True:
            self.rocket_rect.y -= 3
        display.blit(self.rocket_img, self.rocket_rect)
        if self.rocket_rect.top == 50:
            self.start_rocket = False
            self.rocket_rect.y = height - 120

    def update(self):
        display.blit(self.image, self.rect)
        rat_pos = pygame.mouse.get_pos()
        self.rect.x = rat_pos[0]
        if self.start_rocket == False:
            self.rocket_rect.x = self.rect.x + 10



player = Player()
plane = Plane()
rat = Rat()

run = True
while run:
    clock.tick(60)

    display.blit(background_image, (0, 0))

    plane.update()

    plane.bombs()
    player.update(plane.rect.x, plane.rect.y, plane.direction)
    plane.draw()
    rat.update()
    rat.rocket()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()