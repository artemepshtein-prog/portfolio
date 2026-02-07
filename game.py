import pygame
pygame.init()

width = 1920
height = 1080

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('cats bombing rats simulator')

sprite_image = pygame.image.load('images/Cat-5-Sitting.png')
background_image = pygame.image.load('images/Layer_0005_5.png')
background_rect = background_image.get_rect()
sprite_rect = sprite_image.get_rect()
run = True
while run:
    display.blit(sprite_image, sprite_rect)
    display.blit(background_image, background_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()