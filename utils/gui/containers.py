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
# CONTAINERS | SEPARATORS
# ------------------------------------------------------------------------------- #

class StackPanel:
    def __init__(self):
        pass


    def build(self, DT:Data):
        pass


    def update(self, DT:Data):
        pass


    def draw_2d(self, DT:Data):
        pass


class ScrollPanel:
    def __init__(self):
        pass


    def build(self, DT:Data):
        pass


    def update(self, DT:Data):
        pass


    def draw_2d(self, DT:Data):
        pass


class TabsBar:
    def __init__(self):
        pass


    def build(self, DT:Data):
        pass


    def update(self, DT:Data):
        pass


    def draw_2d(self, DT:Data):
        pass

