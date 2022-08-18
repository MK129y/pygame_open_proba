import math

import pygame
from setingx import *
from USER import Player

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
   # player.movement()

    sc.fill(BLACK)

    pygame.draw.circle(sc, GREEN, player_pos, 12)
    #pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH* math.cos()))

    pygame.display.flip()
    clock.tick()

