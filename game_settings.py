# #!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time   : {2022/5/8  19:52}
# @Author : {}
# @Email  : 824935520@qq.com
# @File   : {}

class GameSettings:
    """ 设置类 """
    def __init__(self):

        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.screen_bg_color = (230, 230, 230)
        self.screen_caption = "Alien Invaision"

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # 外星人设置
        self.alien_drop_speed = 10
        self.alien_point = 50

        # 以什么速度加速
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 4

        self.fleet_direction = 1  # 外星舰队运动方向

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale



