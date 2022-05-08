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
        self.ship_speed_factor = 1

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed_factor = 1
        self.bullet_color = (60, 60, 60)


