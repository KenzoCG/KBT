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

class MS_PROPS_Settings(PropertyGroup):
    prop_1: BoolProperty(name="Prop 1")
    prop_2: BoolProperty(name="Prop 2")


    @staticmethod
    def draw(layout):
        # Prefs
        prefs = utils.addon.prefs()
        settings = prefs.settings
        # Settings
        box = layout.box()
        box.label(text="Settings", icon='TOOL_SETTINGS')
        row = box.row(align=True)
        row.prop(settings, 'scripts_dir')
