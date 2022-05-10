# _*_ coding:utf-8 _*_
# @Time    : 2022/5/10 14:09
# @Author  : lxk
# @File    : scoreboard.py

import pygame.font


class ScoreBoard:
    """ 显示积分系统 """
    def __init__(self, screen, game_settings, stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats

        self.font = pygame.font.SysFont(None, 24)
        self.text_color = (0, 255, 0)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def show_font(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def prep_score(self):
        """ 记分 """
        score_str = "{:,}".format(round(self.stats.score))
        self.score_image = self.font.render("Score: "+score_str, True, self.text_color,
                                            self.game_settings.screen_bg_color)
        self.score_rect = self.score_image.get_rect()

        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10

    def prep_high_score(self):
        """ 记高分 """
        high_score_str = "{:,}".format(round(self.stats.high_score))
        self.high_score_image = self.font.render("High Score: " + high_score_str, True, self.text_color,
                                            self.game_settings.screen_bg_color)
        self.high_score_rect = self.high_score_image.get_rect()

        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 10

    def prep_level(self):
        """ 水平 """
        level_str = "{:,}".format(round(self.stats.level))
        self.level_image = self.font.render("Level: " + level_str, True, self.text_color,
                                            self.game_settings.screen_bg_color)
        self.level_rect = self.level_image.get_rect()

        self.level_rect.right = self.screen_rect.right - 10
        self.level_rect.top = self.score_rect.bottom + 10




