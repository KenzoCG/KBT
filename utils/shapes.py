# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import mathutils
from mathutils import (
    Vector,
    Quaternion,
    Matrix,
)
from .enums import ANCHOR
from .graphics import (
    BLENDING_MODES,
    set_blending_mode,
    gen_uniform_color_line_batch,
    gen_uniform_color_tri_batch_indexed,
    draw_uniform_color_batch,
    gen_smooth_color_line_batch,
    gen_smooth_color_tri_batch_indexed,
    draw_smooth_color_batch,
)

# ------------------------------------------------------------------------------- #
# 2D
# ------------------------------------------------------------------------------- #

class Rect2D:
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

