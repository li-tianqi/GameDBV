#!/usr/bin/env python3
# coding=utf-8

from enum import Enum
from PyQt5.QtGui import QColor

class ConfigDBV(object):
    """
    通用参数配置
    所有纯数值的参数, 都在这里配置, 便于统一修改
    """

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        
        self.Direction = Enum('Direction', ('E','W','S','N','SE','SW','NE','NW'))
        
        self.motion_detection_range_X = 2
        self.motion_detection_range_Y = 2

        self.terrain_color = QColor(0, 0, 0)
        self.cover_color = QColor(100, 0, 0)

        self.update_rate = 160



conf = ConfigDBV()
