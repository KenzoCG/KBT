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
from .. import addon
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
    font_size = graphics.get_scaled_font_size()
    font_height = graphics.get_measured_font_height(size=font_size)
    return padding + font_height + padding


def get_box_width(text=""):
    padding = get_padding()
    font_size = graphics.get_scaled_font_size()
    text_width, text_height = graphics.get_measured_text_dimensions(text=text, size=font_size)
    return padding + text_width + padding

# ------------------------------------------------------------------------------- #
# TYPES
# ------------------------------------------------------------------------------- #

class Data:
    def __init__(self, context, event):
        # Context
        self.context = context
        # Dimensions
        self.screen = screen.ScreenDimensions(context)
        self.padding = get_padding()
        self.font_size = graphics.get_scaled_font_size()
        self.box_height = get_box_height()
        # Event
        self.events = Events()
        self.events.CONFIRM = {'RET', 'NUMPAD_ENTER'}
        self.events.CANCEL  = {'ESC'}
        self.controls = UserControls(events=self.events)
        # Start
        self.update(context, event)


    def update(self, context, event):
        self.controls.update(context, event)
