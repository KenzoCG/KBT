# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

from enum import (
    Enum,
    Flag,
    auto
)

# ------------------------------------------------------------------------------- #
# ENUMS
# ------------------------------------------------------------------------------- #

class MODAL_STATUS(Enum):
    RUNNING       = 0
    INTERFACE     = 1
    FINISHED      = 2
    CANCELLED     = 3
    PASS_THROUGH  = 4


class GUI_STATUS(Enum):
    IDLE    = 0
    FOCUSED = 1


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
    FILL       = 0
    HORIZONTAL = 1
    VERTICAL   = 2
