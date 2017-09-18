# -*- coding: utf-8 -*-

import pygame
import pygame.locals
import Grids_In_Graph
import MonsterObject
import TowerObject
import Menu

from pygame import *

WIN_WIDTH = 800                     #ширина окна
WIN_HEIGHT = 640                    #высота окна
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)   #поместим высоту и ширину в один объект
BACKGROUND_COLOR = "#004400"        #цвет заднего фона
BLOCK_WIDTH = 16
BLOCK_HEIGHT = 16
BLOCK_COLOR = "#FF6262"
TOWER_COLOR = "#000000"


def main():

    pygame.init()                                           #инициализация pygame
    screen = pygame.display.set_mode(DISPLAY, pygame.locals.DOUBLEBUF|pygame.locals.SRCALPHA)               #создание окна с заданными размерами
    pygame.display.set_caption("Super_Tower_Defense")       #Добавляем заголовок

    background = Surface((WIN_WIDTH, WIN_HEIGHT))           #Создаём рабочую область, её размеры совпадают с размерами окна
    background.fill(Color(BACKGROUND_COLOR))                #Заполняем её цветом заднего фона


    came_from_dict = Grids_In_Graph.create_came_from_dict([(9, 0)])

    towered_places = []

    test_monster_1 = MonsterObject.Monster((18, 44), 7, 1, "#B22222")
    test_monster_2 = MonsterObject.Monster((18, 46), 7, 1, "#FFFF00")
    test_monster_3 = MonsterObject.Monster((18, 48), 7, 1, "#EE82EE")

    monsters = list()
    shooted_places = list()

    monsters.append(test_monster_1)
    monsters.append(test_monster_2)
    monsters.append(test_monster_3)

    screen_maket = [[' '] * 25 for i in range(20)]

    ''' создание меню '''
    punkts = [(120, 140, u'Game', (250, 250, 30), (250, 30, 250, 0)),
              ((130, 210, u'Quit', (250, 250, 30), (250, 30, 250, 1)))]

    game = Menu.Menu(punkts)

    while 1:                                                #Основной цикл программы

        screen.blit(background, (0, 0))

        for event in pygame.event.get():  # Для всех событий проверяем, какие случились
            if event.type == QUIT:  # Если случился выход, то
                raise SystemExit("QUIT")  # Закрывает
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # С этим нужно что-то делать, ужасное зрелище
                    towered_position = list(event.pos)
                    towered_position[0] = towered_position[0] // BLOCK_WIDTH
                    towered_position[1] = towered_position[1] // BLOCK_HEIGHT
                    towered_position[0], towered_position[1] = towered_position[1], towered_position[0]
                    if tuple(towered_position) not in towered_places:
                        towered_places.append(tuple(towered_position))
                    came_from_dict = Grids_In_Graph.create_came_from_dict(towered_places)

                if event.button == 3:
                    towered_position = list(event.pos)
                    towered_position[0] = towered_position[0] // BLOCK_WIDTH
                    towered_position[1] = towered_position[1] // BLOCK_HEIGHT
                    towered_position[0], towered_position[1] = towered_position[1], towered_position[0]
                    if tuple(towered_position) in towered_places:
                        towered_places.remove(tuple(towered_position))
                        came_from_dict = Grids_In_Graph.create_came_from_dict(towered_places)
                        screen_maket = [[' '] * 25 for i in range(20)]

        for tower_place in towered_places:
            test_tower = TowerObject.Tower(tower_place, 1, 1)
            test_tower.draw(screen)
            shooted_places.extend(test_tower.range_check())

        for monster in monsters:

            current = monster.current_cords
            next_after_current = came_from_dict.get(monster.current_cords)

            while (current != next_after_current):

                monster.move(current, came_from_dict.get(current))
                monster.draw(screen)

                pygame.display.update()
                current = monster.current_cords

            if current in shooted_places:
                monsters.remove(monster)

        shooted_places.clear()

if __name__=="__main__":
    main()

