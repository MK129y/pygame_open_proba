from setingx import *
import pygame

class Player:
    def __int__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

        #сваойство позиции
        @property
        def pos(self):
            return (self.x, self.y)

        def movement(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.y -= player_speed
            if keys[pygame.K_s]:
                self.x -= player_speed
            if keys[pygame.K_d]:
                self.x += player_speed
            if keys[pygame.K_LEFT]:
                self.angle -= 0.02
            if keys[pygame.K_RIGHT]:
                self.y -= player_speed

