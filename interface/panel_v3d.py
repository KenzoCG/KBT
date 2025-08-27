# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from .. import utils

# ------------------------------------------------------------------------------- #
# BASE
# ------------------------------------------------------------------------------- #

class KBT_Panel_V3D(bpy.types.Panel):
    bl_label = 'KBT_Panel_V3D'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "KBT"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.mode in {'OBJECT', 'EDIT_MESH'}

# ------------------------------------------------------------------------------- #
# PANEL
# ------------------------------------------------------------------------------- #

class KBT_PT_Ops_V3D(KBT_Panel_V3D):
    bl_label = "Operators"
    bl_options = {'HEADER_LAYOUT_EXPAND'}

    def draw(self, context):
        prefs = utils.addon.prefs()
        box = self.layout.box()
        row = box.row()
        row.operator("kbt.rnd_modal")
        row = box.row()
        row.operator("kbt.bm_demo_one")


class KBT_PT_Settings_V3D(KBT_Panel_V3D):
    bl_label = "Settings"

    def draw(self, context):
        prefs = utils.addon.prefs()
        settings = prefs.settings
        box = self.layout.box()
        box.prop(settings, 'prop_1', text="Demo Prop 1")
