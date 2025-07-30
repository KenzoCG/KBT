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
# CONTROLS
# ------------------------------------------------------------------------------- #

class Style:
    def __init__(self):
        # Border
        self.show_border = True
        self.border_color = Vector((0,0,0,1))
        self.border_highlight_color = Vector((0,0,0,1))
        # Background
        self.show_background = True
        self.background_color = Vector((0,0,0,1))
        self.background_highlight_color = Vector((0,0,0,1))
        # Batches
        self.border_batch = None
        self.background_batch = None


class Label:
    def __init__(self, text="", span=SPAN.FIT, anchor=ANCHOR.MID_C):
        self.rect = None


    def build(self, DT:Data):
        pass


    def update(self, DT:Data):
        pass


    def draw_2d(self, DT:Data):
        pass


class Button:
    def __init__(self, text=""):
        pass


    def build(self, DT:Data):
        pass


    def update(self, DT:Data):
        pass


    def draw_2d(self, DT:Data):
        pass


class Toggle:
    def __init__(self, text=""):
        pass


    def build(self, DT:Data):
        pass


    def update(self, DT:Data):
        pass


    def draw_2d(self, DT:Data):
        pass


class DropdownBox:
    def __init__(self, text=""):
        pass


    def build(self, DT:Data):
        pass


    def update(self, DT:Data):
        pass


    def draw_2d(self, DT:Data):
        pass


class InputBox:
    def __init__(self, text=""):
        pass


    def build(self, DT:Data):
        pass


    def update(self, DT:Data):
        pass


    def draw_2d(self, DT:Data):
        pass


class SliderBar:
    def __init__(self, text=""):
        pass


    def build(self, DT:Data):
        pass


    def update(self, DT:Data):
        pass


    def draw_2d(self, DT:Data):
        pass
