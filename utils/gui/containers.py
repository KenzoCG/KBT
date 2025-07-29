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

class Panel:
    def __init__(self):
        pass


    def build(self, DT:Data):
        pass


    def update(self, DT:Data):
        pass


    def draw_2d(self, DT:Data):
        pass

