# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from .menu_v3d import (
    KBT_MT_Menu_V3D,
)
from .panel_v3d import (
    KBT_PT_Ops_V3D,
    KBT_PT_Settings_V3D,
)

# ------------------------------------------------------------------------------- #
# REGISTER
# ------------------------------------------------------------------------------- #

CLASSES = (
    # 3D View - Menu
    KBT_MT_Menu_V3D,
    # 3D View - Panels
    KBT_PT_Ops_V3D,
    KBT_PT_Settings_V3D,
)


def register():
    from bpy.utils import register_class
    for cls in CLASSES:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(CLASSES):
        unregister_class(cls)

