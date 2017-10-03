#!/usr/bin/env python3
# coding=utf-8

from ConfigDBV import conf
from PyQt5.QtGui import QImage, QColor
import math

class ObjectDBV(object):
    """
    各种对象的基类, 比如主角, NPC, 事件对象等
    """

    def __init__(self, id = None, img = None, width = 1, height = 1, x = 0, y = 0, speed = 0, dir = conf.Direction.S, map = None):
        self.id = id
        self.img = QImage(img)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed
        self.dir = dir
        self.location = map    # 所处地图

        self.y_img = {}    # 动画帧的y坐标, 用方向控制
        self.x_step = 0    # 范围可通过len(x_img)控制
        self.x_img = [0]    # 动画帧的x坐标, 用step控制
        
        self.on_move = False


    def setSize(self, width, height):
        self.width = width
        self.height = height


    def setFrameY(self, Y_list):
        # 设置动画帧
        i = -1
        for member in conf.Direction:
            i = i + 1
            self.y_img[member] = Y_list[i]

    
    def setFrameX(self, X_list):
        self.x_img = X_list

       
    def setLocation(self, map):
        self.location = map

    def setCoordinate(self, new_x, new_y):
        if (new_x < 0 or new_x > self.location.width - self.width or new_y < 0 or new_y > self.location.height - self.height):
            raise ValueError("the coordinate in 'ObjectDBV.setCoordinate()' out of range")
        else:
            self.x = new_x
            self.y = new_y

    def changeDir(self, dir):
        self.dir = dir
        
    def setSpeed(self, speed):
        self.speed = speed

    def setImage(self, img):
        self.img = QImage(img)

    def move(self):
        delta_x, delta_y = self.motionDetection()
        self.x = self.x + delta_x
        self.y = self.y + delta_y

        #print(self.x_step)
        if self.x_step >= (len(self.x_img) - 1):
            self.x_step = 0
        else:
            self.x_step = self.x_step + 1

            #print("**********", self.x_step)



    def motionDetection(self):
        # 检测可移动位置, 包括地形检测和边界检测
        # 返回x, y坐标的变化值
        dete_x1 = self.x + math.floor((self.width -conf.motion_detection_range_X)*0.5)    # 向下取整
        dete_x2 = self.x + math.ceil((self.width + conf.motion_detection_range_X)*0.5)    # 向上取整
        dete_y1 = self.y + self.height - conf.motion_detection_range_Y
        dete_y2 = self.y + self.height

        if self.dir == conf.Direction.E:
            for distance in range(self.speed):
                if self.x + self.width + 1 + distance > self.location.width:
                    return distance, 0    # 检测边界
                else:
                    pix_x = dete_x2 + 1 + distance
                    for pix_y in range(dete_y1, dete_y2):
                        if QColor(self.location.terrain_img.pixel(pix_x, pix_y)) == conf.terrain_color:
                            return distance, 0    # 检测地形
            return self.speed, 0    # 畅行无阻

        elif self.dir == conf.Direction.W:
            for distance in range(self.speed):
                if self.x - 1 - distance < 0:
                    return -distance, 0
                else:
                    pix_x = dete_x1 -1 - distance
                    for pix_y in range(dete_y1, dete_y2):
                        if QColor(self.location.terrain_img.pixel(pix_x, pix_y)) == conf.terrain_color:
                            return -distance, 0
            return -self.speed, 0

        elif self.dir == conf.Direction.S:
            for distance in range(self.speed):
                if self.y + self.height + 1 + distance > self.location.height:
                    return 0, distance
                else:
                    pix_y = dete_y2 + 1 + distance
                    for pix_x in range(dete_x1, dete_x2):
                        if QColor(self.location.terrain_img.pixel(pix_x, pix_y)) == conf.terrain_color:
                            return 0, distance
            return 0, self.speed

        elif self.dir == conf.Direction.N:
            for distance in range(self.speed):
                if self.y - 1 - distance < 0:
                    return 0, -distance
                else:
                    pix_y = dete_y1 - 1 - distance
                    for pix_x in range(dete_x1, dete_x2):
                        if QColor(self.location.terrain_img.pixel(pix_x, pix_y)) == conf.terrain_color:
                            return 0, -distance
            return 0, -self.speed
        else:
            return 0, 0    # 暂时不加另外四个方向

    def coverOrderDetection(self):
        # 检测遮罩顺序, True时role遮cover, False时cover遮role(默认)
        dete_x1 = self.x + math.floor((self.width -conf.motion_detection_range_X)*0.5)    # 向下取整
        dete_x2 = self.x + math.ceil((self.width + conf.motion_detection_range_X)*0.5)    # 向上取整
        dete_y1 = self.y + self.height - conf.motion_detection_range_Y
        dete_y2 = self.y + self.height

        for pix_x in range(dete_x1, dete_x2):
            for pix_y in range(dete_y1, dete_y2):
                if QColor(self.location.terrain_img.pixel(pix_x, pix_y)) == conf.cover_color:
                    return True

        return False



    def show(self, painter):
        if self.x <= self.location.x:
            x_screen = 0
            delta = self.location.x - self.x
            x_image = self.x_img[self.x_step] + delta
            w = self.width - delta
            if w < 0:
                return
        else:
            x_screen = self.x - self.location.x
            #print(self.x_step)
            #print(self.x_img)
            #print(len(self.x_img))
            x_image = self.x_img[self.x_step]
            w = self.width

        if self.y <= self.location.y:
            y_screen = 0
            delta = self.location.y - self.y
            y_image = self.y_img[self.dir] + delta
            h = self.height - delta
            if h < 0:
                return
        else:
            y_screen = self.y - self.location.y
            y_image = self.y_img[self.dir]
            h = self.height

        painter.drawImage(x_screen, y_screen, self.img, x_image, y_image, w, h)
