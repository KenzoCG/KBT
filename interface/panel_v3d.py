# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from .. import utils

# ------------------------------------------------------------------------------- #
# BASE
# ------------------------------------------------------------------------------- #

class MS_Panel_V3D(bpy.types.Panel):
    bl_label = 'KT_Panel_V3D'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "MeshSketch"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.mode in {'OBJECT', 'EDIT_MESH'}

# ------------------------------------------------------------------------------- #
# PANEL
# ------------------------------------------------------------------------------- #

class MS_PT_Ops_V3D(MS_Panel_V3D):
    bl_label = "Operators"
    bl_options = {'HEADER_LAYOUT_EXPAND'}

    def draw(self, context):
        prefs = utils.addon.prefs()
        box = self.layout.box()
        box.operator("ms.rnd_modal", text="R&D Modal")
        box.operator("wm.url_open", text="Docs").url = "https://kenzocg.github.io"


class MS_PT_Settings_V3D(MS_Panel_V3D):
    bl_label = "Settings"

    def draw(self, context):
        prefs = utils.addon.prefs()
        settings = prefs.settings
        box = self.layout.box()
        box.prop(settings, 'prop_1', text="Demo Prop 1")
        box.prop(settings, 'prop_2', text="Demo Prop 2")
