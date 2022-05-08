# #!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time   : {2022/5/8  20:11}
# @Author : {}
# @Email  : 824935520@qq.com
# @File   : {}
import sys
import pygame


def check_events(ship):
    # 响应鼠标和键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.ship_moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.ship_moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.ship_moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.ship_moving_left = False


def update_screen(screen, game_settings, ship):
    """ 屏幕刷新 """
    screen.fill(game_settings.screen_bg_color)

    ship.ship_blit()

    pygame.display.flip()



