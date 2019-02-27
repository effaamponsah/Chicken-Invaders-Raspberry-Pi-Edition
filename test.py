#simple module written by Effa Amponsah as part of the  CITSA week celebration

backgroundImage = 'backgroud-resized.jpg'
mouseImage = 'shooter.png'

import pygame

# if pygame.font is None:
#     print("Font module not found")
#     exit()

from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640,480),FULLSCREEN,32)
#32 is the bit depth
#0 is the flag

pygame.display.set_caption("Chicken invaders, the pi edition")

background = pygame.image.load(backgroundImage).convert()
mouse = pygame.image.load(mouseImage).convert_alpha()  #convert_alpha removes extra stuff from the image

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background, (0,0))

    x,y = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)
    x-=mouse.get_width()/1/5
    y-=mouse.get_width()/1.5
    screen.blit(mouse, (x,y))

    pygame.display.update()  #makes the image loaded in memory not to flicker
