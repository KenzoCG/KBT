# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
import math
import time
import traceback
from uuid import uuid4
from mathutils import (
    Vector,
    Matrix,
    Color,
)
from .builder import Data
from ..enums import (
    GUI_STATUS,
    ANCHOR,
    SPAN,
)
from ..shapes import Rect2D

# ------------------------------------------------------------------------------- #
# CONTAINERS | SEPARATORS
# ------------------------------------------------------------------------------- #

class StackPanel:
    def __init__(self, elements=None):
        self.rect = Rect2D()
        self.visible = True
        self.elements = elements


    def build(self, DT:Data):
        for element in self.elements:
            element.build(DT)


    def update(self, DT:Data):
        for element in self.elements:
            element.update(DT)


    def draw_2d(self, DT:Data):
        for element in self.elements:
            element.draw_2d(DT)


class TabItem:
    def __init__(self):
        self.label = ""
        self.rect = Rect2D()
        self.container = None


    def draw_2d(self, DT:Data):
        pass


class TabsBar:
    def __init__(self):
        self.rect = Rect2D()
        self.visible = True
        self.tabs = []
        self.active_tab = None


    def add_tab(self, label="", container=None):
        tab_item = TabItem()
        tab_item.label = label
        tab_item.container = container
        self.tabs.append(tab_item)


    def build(self, DT:Data):
        for tab in self.tabs:
            tab.build(DT)


    def update(self, DT:Data):
        controls = DT.controls
        mouse_pos = controls.mouse_pos
        switch_tab = False
        if self.rect.test_point_intersection(x=mouse_pos.x, y=mouse_pos.y, tolerance=-1):
            for tab in self.tabs:
                if tab.rect.test_point_intersection(x=mouse_pos.x, y=mouse_pos.y, tolerance=-1):
                    if controls.mouse_click_down:
                        self.active_tab = tab
                        switch_tab = True
                        break
        if switch_tab:
            for tab in self.tabs:
                if tab == self.active_tab:
                    tab.container.visible = True
                else:
                    tab.container.visible = False
        if self.active_tab:
            self.active_tab.container.update(DT)


    def draw_2d(self, DT:Data):
        for tab in self.tabs:
            tab.draw_2d(DT)
        if self.active_tab:
            self.active_tab.container.draw_2d(DT)

