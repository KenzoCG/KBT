# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from bpy.types import PropertyGroup
from bpy.props import (
    BoolProperty,
    BoolVectorProperty,
    CollectionProperty,
    EnumProperty,
    FloatProperty,
    FloatVectorProperty,
    IntProperty,
    IntVectorProperty,
    PointerProperty,
    StringProperty,
)
from .. import utils

# ------------------------------------------------------------------------------- #
# PROPS
# ------------------------------------------------------------------------------- #

class KBT_PROPS_Mesh(PropertyGroup):
    uuid = StringProperty(name="uuid", default="")

