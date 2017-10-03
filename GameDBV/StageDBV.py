#!/usr/bin/env python3
# coding=utf-8

from PyQt5.QtWidgets import QWidget
from operator import attrgetter
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QTimer, Qt
from ConfigDBV import conf


class StageDBV(QWidget):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene
        self.timer = QTimer(self)
        #self.timer.start(1000)
        self.timer.setInterval(conf.update_rate)
        self.timer.timeout.connect(self.action)
        self.timer.start()
        self.flag_D = False
        self.flag_A = False
        self.flag_S = False
        self.flag_W = False

        self.initUI()


    def initUI(self):
        self.setGeometry(conf.screen_x, conf.screen_y, conf.screen_width, conf.screen_height)
        self.setWindowTitle(conf.title)
        self.show()


    def action(self):
        if self.scene.roles[0].on_move:
            self.scene.roles[0].move()
        #print(self.scene.roles[0].x_step

        self.update()


    def switchScene(self, scene):
        self.scene = scene

    def display(self, painter):
        self.scene.map.show(1, painter)

        bottom_layer = []
        top_layer = []
        sorted_top = []
        sorted_btm = []
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

        if len(bottom_layer) != 0:
            sorted_btm = sorted(bottom_layer, key=attrgetter('y', 'x'))

        if len(top_layer) != 0:
            sorted_top = sorted(top_layer, key=attrgetter('y', 'x'))

        if len(sorted_btm) != 0:
            for obj in sorted_btm:
                obj.show(painter)

        self.scene.map.show(2, painter)

        if len(sorted_top) != 0:
            for obj in sorted_top:
                obj.show(painter)


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        self.display(painter)
        #print("test")
        painter.end()


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_D and not e.isAutoRepeat():
            self.scene.roles[0].changeDir(conf.Direction.E)
            if not self.flag_D:
                self.long_D = -1
                self.scene.roles[0].on_move = True
            self.flag_D = True
        #print("1")
        #print(e.isAutoRepeat())
        if e.key() == Qt.Key_A and not e.isAutoRepeat():
            self.scene.roles[0].changeDir(conf.Direction.W)
            if not self.flag_A:
                self.long_A = -1
                self.scene.roles[0].on_move = True
            self.flag_A = True
        if e.key() == Qt.Key_S and not e.isAutoRepeat():
            self.scene.roles[0].changeDir(conf.Direction.S)
            if not self.flag_S:
                self.long_S = -1
                self.scene.roles[0].on_move = True
            self.flag_S = True
        if e.key() == Qt.Key_W and not e.isAutoRepeat():
            self.scene.roles[0].changeDir(conf.Direction.N)
            if not self.flag_W:
                self.long_W = -1
                self.scene.roles[0].on_move = True
            self.flag_W = True

        #print(self.scene.roles[0].dir)

    def keyReleaseEvent(self, e):
        if e.key() == Qt.Key_D and not e.isAutoRepeat() and self.long_D == -1:
            if self.flag_D:
                self.long_D = 0
                self.scene.roles[0].on_move = False
                self.scene.roles[0].x_step = 0
            self.flag_D = False
        #print("2")
        #print(e.isAutoRepeat())
        if e.key() == Qt.Key_A and not e.isAutoRepeat() and self.long_A == -1:
            if self.flag_A:
                self.long_A = 0
                self.scene.roles[0].on_move = False
                self.scene.roles[0].x_step = 0
            self.flag_A = False
        if e.key() == Qt.Key_S and not e.isAutoRepeat() and self.long_S == -1:
            if self.flag_S:
                self.long_S = 0
                self.scene.roles[0].on_move = False
                self.scene.roles[0].x_step = 0
            self.flag_S = False
        if e.key() == Qt.Key_W and not e.isAutoRepeat() and self.long_W == -1:
            if self.flag_W:
                self.long_W = 0
                self.scene.roles[0].on_move = False
                self.scene.roles[0].x_step = 0
            self.flag_W = False


    

