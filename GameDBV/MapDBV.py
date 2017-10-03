#!/usr/bin/env python3
# coding=utf-8

from PyQt5.QtGui import QImage
from ConfigDBV import conf

class MapDBV(object):

    def __init__(self, map_data):
        """
        map data:
        [img, cover, terrain, x, y]
        """
        self.img = QImage(map_data[0])
        self.cover_img = QImage(map_data[1])
        self.terrain_img = QImage(map_data[2])
        self.width = self.img.width()
        self.height = self.img.height()
        self.x = 0
        self.y = 0

    def show(self, num, painter):
        """
        渲染地图
        """
        if num == 1:
            show_img = self.img
        elif num == 2:
            show_img = self.cover_img
        else:
            raise ValueError("arg 'num' in 'show()' can only be int '1' or '2'")
        
        painter.drawImage(0, 0, show_img, self.x, self.y, conf.screen_width, conf.screen_height)


    def setCoordinate(self, new_x, new_y):
        """
        改变显示坐标, 用于角色移动时
        """
        if (new_x < 0 or new_x > self.width - conf.screen_width or new_y < 0 or new_y > self.height - conf.screen_height):
            raise ValueError("the coordinate in 'MapDBV.setCoordinate()' out of range")
        else:
            self.x = new_x
            self.y = new_y

if __name__ == "__main__":
    data = ["dt04.png", "dt04_2.png", "dt04_3.png"]
    map1 = MapDBV(data)

    print("width: ", map1.width, " height: ", map1.height)
    print("origin: ", "x = ", map1.x, " y = ", map1.y)
    map1.setCoordinate(100, 360)
    print("new: ", "x = ", map1.x, " y = ", map1.y)
