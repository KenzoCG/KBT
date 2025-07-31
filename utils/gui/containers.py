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


class TabsBar:
    def __init__(self, containers=None):
        self.rect = Rect2D()
        self.containers = containers


    def build(self, DT:Data):
        for container in self.containers:
            container.build(DT)


    def update(self, DT:Data):
        for container in self.containers:
            container.update(DT)


    def draw_2d(self, DT:Data):
        for container in self.containers:
            container.draw_2d(DT)

