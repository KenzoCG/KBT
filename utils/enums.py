# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

from enum import (
    Enum,
    Flag,
    auto
)

# ------------------------------------------------------------------------------- #
# MODAL
# ------------------------------------------------------------------------------- #

class MODAL_STATUS(Enum):
    RUNNING       = 0
    INTERFACE     = 1
    FINISHED      = 2
    CANCELLED     = 3
    PASS_THROUGH  = 4

# ------------------------------------------------------------------------------- #
# GUI
# ------------------------------------------------------------------------------- #

class GUI_STATUS(Enum):
    IDLE     = 0
    FOCUSED  = 1
    DISABLED = 2


class ANCHOR(Enum):
    TOP_L = 0
    TOP_C = 1
    TOP_R = 2
    MID_L = 3
    MID_C = 4
    MID_R = 5
    BOT_L = 6
    BOT_C = 7
    BOT_R = 8


class SPAN(Enum):
    NONE       = 0
    BOTH       = 1
    HORIZONTAL = 2
    VERTICAL   = 3


class FILL(Enum):
    NONE           = 0
    SOLID          = 1
    FADE_TO_BOTTOM = 2
    FADE_TO_TOP    = 3
    FADE_TO_LEFT   = 4
    FADE_TO_RIGHT  = 5


class DTYPE(Enum):
    NONE     = 0
    BOOL     = 1
    INT      = 2
    FLOAT    = 3
    STRING   = 4
    COLOR    = 5
    VECTOR_2 = 6
    VECTOR_3 = 7
