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

class BMT_PROPS_Dev(PropertyGroup):
    debug_on : BoolProperty(name="Debug", default=True)

    @staticmethod
    def draw(layout):
        # Prefs
        prefs = utils.addon.prefs()
        dev = prefs.dev
        # Settings
        box = layout.box()
        box.label(text="Dev", icon='TOOL_SETTINGS')
        row = box.row(align=True)
        row.prop(dev, 'debug_on')
