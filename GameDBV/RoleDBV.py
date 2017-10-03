#!/usr/bin/env python3
# coding=utf-8

from ObjectDBV import ObjectDBV
from ConfigDBV import conf

class RoleDBV(ObjectDBV):
    def __init__(self):
        super().__init__()


    def move(self):
        delta_x, delta_y = self.motionDetection()
        #print("*************************************")
        #print(delta_x, delta_y)
        self.x = self.x + delta_x
        self.y = self.y + delta_y

        x_tmp = self.x + (self.width // 2) - (conf.screen_width // 2)
        y_tmp = self.y + self.height // 2 - conf.screen_height // 2
        
        if x_tmp < 0:    # 检测地图是否超过边界范围
            self.location.x = 0
        elif x_tmp > self.location.width - conf.screen_width:
            self.location.x = self.location.width - conf.screen_width
        else:
            self.location.x = x_tmp

        if y_tmp < 0:
            self.location.y = 0
        elif y_tmp > self.location.height - conf.screen_height:
            self.location.y = self.location.height - conf.screen_height
        else:
            self.location.y = y_tmp

        if self.x_step == len(self.x_img) - 1:
            self.x_step = 0
        else:
            self.x_step = self.x_step + 1


if __name__ == "__main__":
    r = RoleDBV()
