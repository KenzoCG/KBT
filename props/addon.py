# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from bpy.types import AddonPreferences
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
from .settings import KBT_PROPS_Settings
from .gui import KBT_PROPS_GUI
from .dev import KBT_PROPS_Dev
from .. import utils

# ------------------------------------------------------------------------------- #
# ADDON PREFS
# ------------------------------------------------------------------------------- #

class KBT_ADDON_Prefs(AddonPreferences):
    bl_idname = utils.addon.name()
    settings : PointerProperty(type=KBT_PROPS_Settings)
    gui      : PointerProperty(type=KBT_PROPS_GUI)
    dev      : PointerProperty(type=KBT_PROPS_Dev)
    tab_opts = (
        ('SETTINGS', "Settings" , ""),
        ('INFO'    , "Info"     , ""),
        ('GUI'     , "GUI"      , ""),
        ('DEV'     , "Dev"      , ""),
    )
    tabs: EnumProperty(name="tabs", items=tab_opts, default='SETTINGS')


    def draw(self, context):
        row = self.layout.row()
        row.prop(self, 'tabs', expand=True)
        if self.tabs == 'SETTINGS':
            KBT_PROPS_Settings.draw(self.layout)
        elif self.tabs == 'INFO':
            draw_info(self.layout)
        elif self.tabs == 'GUI':
            KBT_PROPS_GUI.draw(self.layout)
        elif self.tabs == 'DEV':
            KBT_PROPS_Dev.draw(self.layout)


def draw_info(layout):
    # Websites
    box = layout.box()
    box.label(text="Web Pages", icon='WORLD')
    row = box.row(align=True)
    row.operator("wm.url_open", text="YouTube").url = "https://www.youtube.com/@cg-boundary"
    row = box.row(align=True)
    row.operator("wm.url_open", text="Website").url = "https://github.com/KenzoCG"
    # Contact
    box = layout.box()
    row = box.row()
    row.label(text="Contact", icon='USER')
    row = box.row()
    row.label(text="cg.boundary@gmail.com")

