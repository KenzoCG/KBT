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
from ..enums import (
    GUI_STATUS,
    ANCHOR,
    SPAN,
)

# ------------------------------------------------------------------------------- #
# MENU SYSTEMS
# ------------------------------------------------------------------------------- #

class Menu:
    def __init__(self, context, event):
        pass


    def build(self):
        pass


    def close(self, context):
        pass


    def update(self, context, event):
        pass


    def draw_2d(self, context):
        pass


