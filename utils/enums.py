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
    IDLE    = 0
    FOCUSED = 1


class ANCHOR(Enum):
    CENTER_LEFT   = 0
    CENTER_MIDDLE = 1
    CENTER_RIGHT  = 2
    TOP_LEFT      = 3
    TOP_RIGHT     = 4
    BOTTOM_LEFT   = 5
    BOTTOM_RIGHT  = 6


class SPAN(Enum):
    FILL       = 0
    HORIZONTAL = 1
    VERTICAL   = 2
