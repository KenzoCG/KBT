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


# Label | Button | Toggle | DropdownBox | ValueBox | SliderBar


class Label:
    def __init__(self, text=""):
        pass


    def build(self, DT:Data):
        pass


    def update(self, DT:Data):
        pass


    def draw_2d(self, DT:Data):
        pass


