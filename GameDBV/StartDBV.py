#!/usr/bin/env python3
# coding=utf-8

from PyQt5.QtWidgets import QApplication
import sys
from StageDBV import StageDBV
from MapDBV import MapDBV
from ObjectDBV import ObjectDBV
from RoleDBV import RoleDBV
from SceneDBV import SceneDBV


def start(scene):
    app = QApplication(sys.argv)
    stage = StageDBV(scene)
    sys.exit(app.exec_())



if __name__ == "__main__":
    map_data = ["dt04.png", "dt04_2.png", "dt04_3.png"]
    map = MapDBV(map_data)

    role = RoleDBV()
    role.id = 'r01'
    role.setImage("rw0201.png")
    role.setSize(48, 68)
    role.setLocation(map)
    role.setCoordinate(600, 250)
    role.setSpeed(15)
    X_list=[]
    for i in range(8):
        tmp = 36 + i * 120
        X_list.append(tmp)


    role.setFrameX(X_list)
    Y_list = [0,0,0,0, 0,0,0,0]
    tmp_list = []
    for i in range(4):
        tmp = 41 + i * 150
        tmp_list.append(tmp)
    Y_list[0] = tmp_list[2]
    Y_list[1] = tmp_list[1]
    Y_list[2] = tmp_list[0]
    Y_list[3] = tmp_list[3]

    role.setFrameY(Y_list)
    #print(role.x_img)
    #print(role.y_img)

    npc = ObjectDBV(id='npc01', img="rw0101.png", width=100, height=150, x=480, y=460)
    npc.setLocation(map)
    npc.x_img = [300]
    y_lst = [0, 0, 450, 0, 0, 0, 0, 0]
    npc.setFrameY(y_lst)

    scene = SceneDBV()
    scene.loadMap(map)
    scene.addRole(role)
    scene.addObject(npc)
    
    start(scene)

