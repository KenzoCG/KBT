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
    FILL,
    SPAN,
)
from ..graphics import (
    BLENDING_MODES,
    set_blending_mode,
    gen_uniform_color_line_batch,
    gen_uniform_color_tri_batch_indexed,
    gen_smooth_color_line_batch,
    gen_smooth_color_tri_batch_indexed,
    draw_uniform_color_batch,
    draw_smooth_color_batch,
)
from ..shapes import Rect2D
from .builder import (
    Data,
    get_faded_smooth_colors,
)

# ------------------------------------------------------------------------------- #
# MENU SYSTEMS
# ------------------------------------------------------------------------------- #

class BoxMenu:
    def __init__(self, context, event):
        # Data
        self.DT = Data(context, event)
        self.containers = []
        # Dimensional
        self.rect = Rect2D()
        # Colors
        self.show_focus_color = False
        self.background_color = Vector(self.DT.colors.background)
        self.background_focus_color = Vector(self.DT.colors.background_focus)
        self.border_color = Vector(self.DT.colors.border)
        self.border_focus_color = Vector(self.DT.colors.border_focus)
        # Batches
        self.background_batch = None
        self.border_batch = None


    def build(self, x=0, y=0, w=0, h=0, anchor=ANCHOR.MID_C):
        # Rect
        self.rect.set_props(x=x, y=y, w=w, h=h, anchor=anchor)
        self.rect.build()
        # Batches
        self.background_batch = gen_uniform_color_tri_batch_indexed(*self.rect.get_tris_and_indices())
        self.border_batch = gen_uniform_color_line_batch(lines=self.rect.get_boundary_lines())
        # Internal
        for container in self.containers:
            container.build(self.DT)


    def disable(self):
        self.DT.status = GUI_STATUS.DISABLED
        self.DT.focussed_item = None
        self.DT.controls.reset()
        self.show_focus_color = False


    def close(self, context):
        for container in self.containers:
            container.close(self.DT)


    def update(self, context, event):
        # Skip
        if self.DT.status == GUI_STATUS.DISABLED:
            return self.DT.status
        # Controls
        self.DT.controls.update(context, event)
        # Focussed
        if self.DT.focussed_item is not None:
            if self.__update_focussed_item():
                self.DT.status = GUI_STATUS.FOCUSED
                return self.DT.status
        # Status
        self.DT.status = GUI_STATUS.IDLE
        # Skip
        self.show_focus_color = False
        if not self.__mouse_in_bounds():
            return self.DT.status
        self.show_focus_color = True
        # Containers
        for container in self.containers:
            container.update(self.DT)
            # Focussed
            if self.DT.focussed_item is not None:
                if self.__update_focussed_item():
                    self.DT.status = GUI_STATUS.FOCUSED
                    return self.DT.status
        # Done
        return self.DT.status


    def draw_2d(self, context):
        # Skip
        if self.DT.status == GUI_STATUS.DISABLED:
            return
        # State
        set_blending_mode(mode=BLENDING_MODES.ALPHA)
        # Rect
        if self.show_focus_color:
            draw_uniform_color_batch(self.background_batch, color=self.background_focus_color)
            draw_uniform_color_batch(self.border_batch, color=self.border_focus_color)
        else:
            draw_uniform_color_batch(self.background_batch, color=self.background_color)
            draw_uniform_color_batch(self.border_batch, color=self.border_focus_color)
        # Containers
        for container in self.containers:
            container.draw_2d(self.DT)
        # State
        set_blending_mode(mode=BLENDING_MODES.NONE)


    def __update_focussed_item(self):
        """Returns true if the item was updated and is still in focus"""
        if hasattr(self.DT.focussed_item, 'update'):
            self.DT.focussed_item.update(self.DT)
            if self.DT.focussed_item:
                return True
        self.DT.focussed_item = None
        return False


    def __mouse_in_bounds(self):
        """Checks if the mouse is within the menu"""
        mouse_pos = self.DT.controls.mouse_pos
        if self.rect.test_point_intersection(x=mouse_pos.x, y=mouse_pos.y, tolerance=-1):
            return True
        return False
