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
from .builder import Data
from ..enums import (
    GUI_STATUS,
    ANCHOR,
    SPAN,
)
from ..shapes import Rect2D

# ------------------------------------------------------------------------------- #
# GENERATORS
# ------------------------------------------------------------------------------- #

