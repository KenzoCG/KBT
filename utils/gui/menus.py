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
# MENU SYSTEMS
# ------------------------------------------------------------------------------- #

class BoxMenu:
    def __init__(self):
        self.DT = None
        self.containers = []


    def build(self, context, event):
        self.DT = Data(context, event)


    def close(self, context):
        pass


    def update(self, context, event):
        pass


    def draw_2d(self, context):
        pass

