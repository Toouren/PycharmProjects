import pygame

from pygame import *

MONSTER_WIDTH = 16
MONSTER_HEIGHT = 16


class Monster(sprite.Sprite):
    def __init__(self, coords, move_speed, helth, monster_color):
        sprite.Sprite.__init__(self)
        self.current_cords = coords
        self.move_speed = move_speed
        self.x_cord = coords[1] * MONSTER_WIDTH
        self.y_cord = coords[0] * MONSTER_HEIGHT
        self.helth_level = helth
        self.image = Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.image.fill(Color(monster_color))
        self.rect = Rect(coords[1] * MONSTER_WIDTH, coords[0] * MONSTER_HEIGHT, MONSTER_WIDTH, MONSTER_HEIGHT)

    def move(self, current_cords, next_coords):
        self.x_cord += (next_coords[1] - current_cords[1]) * MONSTER_WIDTH
        self.y_cord += (next_coords[0] - current_cords[0]) * MONSTER_HEIGHT
        self.current_cords = next_coords

    def draw(self, screen):
        screen.blit(self.image, (self.x_cord, self.y_cord))
        pygame.time.delay(100)
