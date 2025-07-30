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
from ..maths import Rect2D

# ------------------------------------------------------------------------------- #
# MENU SYSTEMS
# ------------------------------------------------------------------------------- #

class BoxMenu:
    def __init__(self, x=0, y=0, w=0, h=0, anchor=ANCHOR.MID_C):
        self.rect = Rect2D(x, y, w, h, anchor)
        self.DT = None
        self.containers = []


    def build(self, context, event, ANCHOR):
        self.DT = Data(context, event)
        for container in self.containers:
            container.build(self.DT)


    def close(self, context):
        for container in self.containers:
            container.close(self.DT)


    def update(self, context, event):
        for container in self.containers:
            container.update(self.DT)


    def draw_2d(self, context):
        for container in self.containers:
            container.draw_2d(self.DT)


