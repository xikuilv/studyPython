# #!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time   : {2022/5/8  20:11}
# @Author : {}
# @Email  : 824935520@qq.com
# @File   : {}
import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, screen, game_settings, stats, aliens, ship, bullets):
    """ 按键按下 """
    if event.key == pygame.K_RIGHT:
        ship.ship_moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.ship_moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(screen, game_settings, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()

    elif event.key == pygame.K_p:
        game_start(screen, game_settings, stats, aliens, bullets, ship)


def fire_bullet(screen, game_settings, ship, bullets):
    if len(bullets) < game_settings.bullet_allowed:
        new_bullet = Bullet(screen, game_settings, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """ 按键松开 """
    if event.key == pygame.K_RIGHT:
        ship.ship_moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.ship_moving_left = False


def check_events(screen, game_settings, stats, ship, aliens, bullets, button):
    # 响应鼠标和键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, game_settings, stats, aliens, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mose_x, mose_y = pygame.mouse.get_pos()
            check_button(screen, game_settings, stats, button, aliens, bullets, ship, mose_x, mose_y)


def check_button(screen, game_settings, stats, button, aliens, bullets, ship, mose_x, mose_y):

    if button.rect.collidepoint(mose_x, mose_y) and not stats.game_active:
        game_start(screen, game_settings, stats, aliens, bullets, ship)


def game_start(screen, game_settings, stats, aliens, bullets, ship):
    """ 开始游戏 """
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    stats.game_active = True

    game_settings.initialize_dynamic_settings()

    aliens.empty()
    bullets.empty()

    fleet_aliens(screen, game_settings, ship, aliens)
    ship.ship_center()


def update_screen(screen, game_settings, stats, ship, aliens, bullets, button):
    """ 屏幕刷新 """
    screen.fill(game_settings.screen_bg_color)

    ship.ship_blit()

    aliens.draw(screen)

    for bullet in bullets:
        bullet.bullet_draw()

    if not stats.game_active:
        button.button_draw()

    pygame.display.flip()


def update_bullet(screen, game_settings, ship, aliens, bullets):
    """ 刷新子弹 """
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_alien_bullet_collision(screen, game_settings, ship, aliens, bullets)


def check_alien_bullet_collision(screen, game_settings, ship, aliens, bullets):
    """ 响应子弹和外星人相碰撞 """
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # 创建外星人舰队
        fleet_aliens(screen, game_settings, ship, aliens)

        game_settings.increase_speed()
        # 清空子弹
        bullets.empty()


def update_alien(screen, game_settings, stats, aliens, ship, bullets):
    """ 更新 alien """
    for alien in aliens:
        if alien.alien_edge():
            check_alien_direction(game_settings, aliens)
            break

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(screen, game_settings, stats, ship, aliens, bullets)

    for alien in aliens:
        if alien.rect.bottom >= game_settings.screen_height:
            ship_hit(screen, game_settings, stats, ship, aliens, bullets)
            break

    aliens.update()


def ship_hit(screen, game_settings, stats, ship, aliens, bullets):

    if stats.ship_left > 0:
        # ship_left 减一
        stats.ship_left -= 1
        # 子弹和外星人均清零
        aliens.empty()
        bullets.empty()

        # 创建外星人舰队
        fleet_aliens(screen, game_settings, ship, aliens)

        # 飞船显示在底部中央
        ship.ship_center()

        # 暂停1秒
        sleep(1)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_alien_direction(game_settings, aliens):
    """ 如果 alien 碰到屏幕边缘，aliens舰队下移 """
    for alien in aliens:
        alien.rect.y += game_settings.alien_drop_speed
    game_settings.fleet_direction *= -1


def get_number_row(game_settings, alien):
    available_space_x = game_settings.screen_width - 2 * alien.rect.width
    number_row = int(available_space_x / (2 * alien.rect.width))
    return number_row


def get_number_col(game_settings, alien, ship):
    available_space_y = game_settings.screen_height - 5 * alien.rect.height - ship.rect.height
    number_col = int(available_space_y / (2 * alien.rect.height))
    return number_col


def create_alien(screen, game_settings, ship, aliens, num_x, num_y):
    alien = Alien(screen, game_settings, ship)
    alien.x = alien.rect.width + 2 * alien.rect.width * num_x
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*num_y
    aliens.add(alien)


def fleet_aliens(screen, game_settings, ship, aliens):
    alien = Alien(screen, game_settings, ship)
    number_col = get_number_col(game_settings, alien, ship)
    number_row = get_number_row(game_settings, alien)

    for num_y in range(number_col):
        for num_x in range(number_row):
            create_alien(screen, game_settings, ship, aliens, num_x, num_y)



