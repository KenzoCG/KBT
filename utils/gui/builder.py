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
from ..event import (
    Events,
    UserControls,
)
from ..enums import (
    GUI_STATUS,
    ANCHOR,
    SPAN,
    FILL,
)
from .. import graphics
from .. import screen

# ------------------------------------------------------------------------------- #
# FUNCTIONS
# ------------------------------------------------------------------------------- #

def get_padding():
    prefs = addon.prefs()
    settings = prefs.gui.settings
    padding = int(settings.padding * screen.ui_scale())
    return padding


def get_box_height():
    padding = get_padding()
    font_size = graphics.get_scaled_font_size_from_prefs()
    font_height = graphics.get_measured_font_height(size=font_size)
    return padding + font_height + padding


def get_box_width(text=""):
    padding = get_padding()
    font_size = graphics.get_scaled_font_size_from_prefs()
    text_width, text_height = graphics.get_measured_text_dimensions(text=text, size=font_size)
    return padding + text_width + padding


def get_faded_smooth_colors(c1=None, c2=None, prep_for='QUAD_TRIS', fill=FILL.FADE_TO_TOP):
    if (not isinstance(c1, Vector)) or (not isinstance(c2, Vector)) or (fill == FILL.NONE):
        return None
    if fill == FILL.FADE_TO_BOTTOM:
        if prep_for == 'QUAD_TRIS':
            return [c2, c2, c1, c1]
        elif prep_for == 'QUAD_LINES':
            return [c2, c2, c2, c1, c1, c1, c1, c2]
    if fill == FILL.FADE_TO_TOP:
        if prep_for == 'QUAD_TRIS':
            return [c1, c1, c2, c2]
        elif prep_for == 'QUAD_LINES':
            return [c1, c1, c1, c2, c2, c2, c2, c1]
    if fill == FILL.FADE_TO_LEFT:
        if prep_for == 'QUAD_TRIS':
            return [c2, c1, c1, c2]
        elif prep_for == 'QUAD_LINES':
            return [c2, c1, c1, c1, c1, c2, c2, c2]
    if fill == FILL.FADE_TO_RIGHT:
        if prep_for == 'QUAD_TRIS':
            return [c1, c2, c2, c1]
        elif prep_for == 'QUAD_LINES':
            return [c1, c2, c2, c2, c2, c1, c1, c1]
    return None

# ------------------------------------------------------------------------------- #
# TYPES
# ------------------------------------------------------------------------------- #

class Data:
    def __init__(self, context, event):
        # Prefs
        self.prefs = addon.prefs()
        self.gui = self.prefs.gui
        self.colors = self.gui.colors
        # Runtime
        self.status = GUI_STATUS.IDLE
        # Context
        self.context = context
        # Dimensions
        self.screen = screen.ScreenDimensions(context)
        self.padding = get_padding()
        self.font_size = graphics.get_scaled_font_size_from_prefs()
        self.box_height = get_box_height()
        # Event
        self.events = Events()
        self.events.CONFIRM = {'RET', 'NUMPAD_ENTER'}
        self.events.CANCEL  = {'ESC'}
        self.controls = UserControls(events=self.events)
        # Focus
        self.focussed_item = None
        # Start
        self.update(context, event)


    def update(self, context, event):
        self.controls.update(context, event)
