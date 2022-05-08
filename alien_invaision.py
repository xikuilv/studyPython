# #!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time   : {2022/5/8  19:34}
# @Author : {}
# @Email  : 824935520@qq.com
# @File   : {}

import sys
import pygame
from ship import Ship
from game_settings import GameSettings
import game_functions as gf


def main():
    # pygame 初始化
    pygame.init()

    # 创建设置类对象
    game_settings = GameSettings()

    # 创建显示屏幕对象
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption(game_settings.screen_caption)

    # 创建ship对象
    ship = Ship(screen, game_settings)

    while True:

        gf.check_events(ship)

        ship.update_ship()

        gf.update_screen(screen, game_settings, ship)


if __name__ == '__main__':
    main()

