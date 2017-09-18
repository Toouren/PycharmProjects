import pygame

from pygame import *

TOWER_WIDTH = 16
TOWER_HEIGHT = 16
TOWER_COLOR = "#000000"


class Tower(sprite.Sprite):
    def __init__(self, coords, range, damage):
        sprite.Sprite.__init__(self)
        self.unnormal_coords = coords
        self.x_cord = coords[1] * TOWER_WIDTH
        self.y_cord = coords[0] * TOWER_HEIGHT
        self.range = range
        self.damage = damage
        self.image = Surface((TOWER_WIDTH, TOWER_HEIGHT))
        self.image.fill(Color(TOWER_COLOR))
        self.rect = Rect(coords[1] * TOWER_WIDTH, coords[0] * TOWER_HEIGHT, TOWER_WIDTH, TOWER_HEIGHT)

    def draw(self, screen):
        screen.blit(self.image, (self.x_cord, self.y_cord))

    def range_check(self):
        shooted_places = list()
        range_list = ((0, self.range), (0, -self.range), (self.range, 0), (-self.range, 0), (self.range, -self.range), (-self.range, self.range), (-self.range, -self.range), (self.range, self.range))
        for ranges in range_list:
            shooted_places.append((self.unnormal_coords[0] + ranges[0], self.unnormal_coords[1] + ranges[1]))

        return shooted_places