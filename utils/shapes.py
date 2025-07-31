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

# ------------------------------------------------------------------------------- #
# 2D
# ------------------------------------------------------------------------------- #

class Rect2D:
    def __init__(self):
        # Position
        self.x = 0
        self.y = 0
        # Dimensions
        self.w = 0
        self.h = 0
        # Basis
        self.anchor = ANCHOR.MID_C
        # Bounds
        self.tl = Vector((0, 0))
        self.tr = Vector((0, 0))
        self.bl = Vector((0, 0))
        self.br = Vector((0, 0))


    def set_props(self, x=0, y=0, w=0, h=0, anchor=ANCHOR.MID_C):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.anchor = anchor


    def build(self):
        def set_boundary_points(lx=0, rx=0, ty=0, by=0):
            self.tl = Vector((lx, ty))
            self.tr = Vector((rx, ty))
            self.bl = Vector((lx, by))
            self.br = Vector((rx, by))

        half_w = self.w / 2
        half_h = self.h / 2

        if self.anchor == ANCHOR.TOP_L:
            lx = self.x
            rx = self.x + self.w
            ty = self.y
            by = self.y - self.h
            set_boundary_points(lx, rx, ty, by)
            return
        if self.anchor == ANCHOR.TOP_C:
            lx = self.x - half_w
            rx = self.x + half_w
            ty = self.y
            by = self.y - self.h
            set_boundary_points(lx, rx, ty, by)
            return
        if self.anchor == ANCHOR.TOP_R:
            lx = self.x - self.w
            rx = self.x
            ty = self.y
            by = self.y - self.h
            set_boundary_points(lx, rx, ty, by)
            return
        if self.anchor == ANCHOR.MID_L:
            lx = self.x
            rx = self.x + self.w
            ty = self.y + half_h
            by = self.y - half_h
            set_boundary_points(lx, rx, ty, by)
            return
        if self.anchor == ANCHOR.MID_C:
            lx = self.x - half_w
            rx = self.x + half_w
            ty = self.y + half_h
            by = self.y - half_h
            set_boundary_points(lx, rx, ty, by)
            return
        if self.anchor == ANCHOR.MID_R:
            lx = self.x - self.w
            rx = self.x
            ty = self.y + half_h
            by = self.y - half_h
            set_boundary_points(lx, rx, ty, by)
            return
        if self.anchor == ANCHOR.BOT_L:
            lx = self.x
            rx = self.x + self.w
            ty = self.y + self.h
            by = self.y
            set_boundary_points(lx, rx, ty, by)
            return
        if self.anchor == ANCHOR.BOT_C:
            lx = self.x - half_w
            rx = self.x + half_w
            ty = self.y + self.h
            by = self.y
            set_boundary_points(lx, rx, ty, by)
            return
        if self.anchor == ANCHOR.BOT_R:
            lx = self.x - self.w
            rx = self.x
            ty = self.y + self.h
            by = self.y
            set_boundary_points(lx, rx, ty, by)
            return


    def shift_position(self, x=0, y=0):
        self.x += x
        self.y += y
        self.build_boundary()


    def test_point_intersection(self, x=0, y=0, tolerance=0):
        lx = self.tl.x - tolerance
        rx = self.tr.x + tolerance
        ty = self.tl.y + tolerance
        by = self.bl.y - tolerance
        if x >= lx and x <= rx:
            if y <= ty and y >= by:
                return True
        return False


    def get_tris_and_indices(self):
        tris = [self.bl, self.br, self.tr, self.tl]
        indices = [(0, 1, 2), (0, 2, 3)]
        return tris, indices


    def get_boundary_lines(self):
        lines = [
            self.bl, self.br,
            self.br, self.tr,
            self.tr, self.tl,
            self.tl, self.bl
        ]
        return lines


