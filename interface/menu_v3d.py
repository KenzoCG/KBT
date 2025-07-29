# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from ..utils import addon

# ------------------------------------------------------------------------------- #
# MENU
# ------------------------------------------------------------------------------- #

class MS_MT_Menu_V3D(bpy.types.Menu):
    bl_idname = "MS_MT_Menu_V3D"
    bl_label = addon.name_and_version_string()


    def draw(self, context):
        # Prefs
        prefs = addon.prefs()
        # Layout
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'
        # Ops
        layout.operator("ms.rnd_modal", text="R&D Modal", icon="TOOL_SETTINGS")
        # Blender
        layout.separator()
        layout.menu("SCREEN_MT_user_menu", text="Quick Favorites", icon="BLENDER")
        # Developer
        layout.separator()
        dev = prefs.dev
        if dev.debug_on:
            draw_dev_ops(context, layout, dev)


def draw_dev_ops(context, layout, dev):
    layout.operator("wm.url_open", text="Docs").url = "https://kenzocg.github.io"
