#!/usr/bin/env python3
# coding=utf-8

class SceneDBV(object):
    def __init__(self):
        self.map = None
        self.roles = []
        self.objects = []

        self.width = self.map.width
        self.height = self.map.height

    def loadMap(self, map):
        self.map = map

    def addRole(self, role):
        self.roles.append(role)

    def addObject(self, obj):
        self.objects.append(obj)

