#!/usr/bin/env python3
# coding=utf-8

import sys
from PyQt5.QtWidgets import QWidget
from operator import itemgetter, 

class StageDBV(QWidget):
    def __init__(self):
        super().__init__()
        self.scene = None
        

    def switchScene(self, scene):
        self.scene = scene

    def display(self, painter):
        self.scene.map.show(1, painter)

        bottom_layer = []
        top_layer = []
        for role in self.scene.roles:
            if role.coverOrderDetection():
                top_layer.append(role)
            else:
                bottom_layer.append(role)

        for obj in self.scene.objects:
            if obj.coverOrderDetection():
                top_layer.append(obj)
            else:
                bottom_layer.append(obj)




