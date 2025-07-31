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
from .. import addon
from ..enums import (
    GUI_STATUS,
    ANCHOR,
    SPAN,
    FILL,
    DTYPE,
)
from ..shapes import Rect2D
from .builder import Data

# ------------------------------------------------------------------------------- #
# BASE
# ------------------------------------------------------------------------------- #

class Element:
    def __init__(self):
        # Data
        self.prop_name = ''
        self.prop_object = None
        self.prop_data_type = DTYPE.NONE
        self.callback = None
        self.callback_args = None
        # Dimensional
        self.rect = Rect2D()
        # Background
        self.background_style = FILL.NONE
        self.background_color = Vector((0,0,0,1))
        self.background_focus_color = Vector((0,0,0,1))
        self.background_batch = None
        # Border
        self.border_style = FILL.NONE
        self.border_color = Vector((0,0,0,1))
        self.border_focus_color = Vector((0,0,0,1))
        self.border_batch = None
        # Font
        self.font_size = 12
        self.font_color = Vector((1,1,1,1))
        self.font_focus_color = Vector((1,1,1,1))
        # Text
        self.text_anchor = ANCHOR.MID_C
        self.text_width = 0


    def mouse_in_bounds(self, DT:Data):
        mouse_pos = DT.controls.mouse_pos
        if self.rect.test_point_intersection(x=mouse_pos.x, y=mouse_pos.y, tolerance=-1):
            return True
        return False

# ------------------------------------------------------------------------------- #
# TYPES
# ------------------------------------------------------------------------------- #

class Label(Element):
    def __init__(self, text=""):
        super().__int__()
        self.text = text


    def build(self, DT:Data):
        x = 0
        y = 0
        w = 0
        h = 0
        self.rect.set_props(x=x, y=y, w=w, h=h, anchor=ANCHOR.MID_C)


    def update(self, DT:Data):
        # Has Focus
        if self == DT.focussed_element:
            pass
        # Test Focus
        if self.mouse_in_bounds(DT):
            if DT.controls.mouse_click_down:
                DT.focussed_element = self


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
