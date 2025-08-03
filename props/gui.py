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

class KBT_PROPS_GUI_Colors(PropertyGroup):
    font : FloatVectorProperty(name="Font", size=4, min=0, max=1, subtype='COLOR', default=(1, 1, 1, 1)) # type: ignore
    background : FloatVectorProperty(name="Background", size=4, min=0, max=1, subtype='COLOR', default=(0, 0, 0, 0.125)) # type: ignore
    container : FloatVectorProperty(name="Container", size=4, min=0, max=1, subtype='COLOR', default=(0, 0, 0, 0.125)) # type: ignore
    element : FloatVectorProperty(name="Element", size=4, min=0, max=1, subtype='COLOR', default=(0, 0, 0, 0.125)) # type: ignore
    border : FloatVectorProperty(name="Border", size=4, min=0, max=1, subtype='COLOR', default=(0, 0, 0, 0.25)) # type: ignore


class KBT_PROPS_GUI_Settings(PropertyGroup):
    padding   : IntProperty(name="UI Padding", min=3, max=10, default=3) # type: ignore
    font_size : IntProperty(name="Font Size", min=8, max=24, default=12) # type: ignore


class KBT_PROPS_GUI(PropertyGroup):
    settings : PointerProperty(type=KBT_PROPS_GUI_Settings) # type: ignore
    colors   : PointerProperty(type=KBT_PROPS_GUI_Colors) # type: ignore

    @staticmethod
    def draw(layout):
        # Prefs
        prefs = utils.addon.prefs()
        gui = prefs.gui
  
        # Settings
        settings = gui.settings
        box = layout.box()
        box.label(text="GUI Settings", icon='TOOL_SETTINGS')
        # Props
        row = box.row(align=True)
        row.prop(settings, 'padding', text="Padding")
        row = box.row(align=True)
        row.prop(settings, 'font_size', text="Font Size")
  
        # Colors
        colors = gui.colors
        box = layout.box()
        box.label(text="GUI Colors", icon='COLOR')
        # Props
        row = box.row(align=True)
        row.prop(colors, 'font', text="font")
        row = box.row(align=True)
        row.prop(colors, 'background', text="background")
        row = box.row(align=True)
        row.prop(colors, 'container', text="container")
        row = box.row(align=True)
        row.prop(colors, 'element', text="element")
        row = box.row(align=True)
        row.prop(colors, 'border', text="border")

