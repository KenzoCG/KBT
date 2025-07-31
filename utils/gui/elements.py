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
from ..enums import (
    GUI_STATUS,
    ANCHOR,
    SPAN,
    DTYPE,
)
from ..shapes import Rect2D
from .builder import Data

# ------------------------------------------------------------------------------- #
# GENERATORS
# ------------------------------------------------------------------------------- #


