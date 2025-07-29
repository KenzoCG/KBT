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
from .. import screen

# ------------------------------------------------------------------------------- #
# UTILS
# ------------------------------------------------------------------------------- #

class Data:
    def __init__(self, context, event):
        # Context
        self.context = context
        self.screen = screen.ScreenDimensions(context)
        # Event
        self.events = Events()
        self.events.CONFIRM = {'RET', 'NUMPAD_ENTER'}
        self.events.CANCEL  = {'ESC'}
        self.controls = UserControls(events=self.events)


    def update(self, context, event):
        pass
