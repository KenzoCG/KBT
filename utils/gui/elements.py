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

# ------------------------------------------------------------------------------- #
# CONTROLS
# ------------------------------------------------------------------------------- #

class Label:
    def __init__(self, text=""):
        pass


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
