# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from .menu_v3d import (
    BMT_MT_Menu_V3D,
)
from .panel_v3d import (
    BMT_PT_Ops_V3D,
    BMT_PT_Settings_V3D,
)

# ------------------------------------------------------------------------------- #
# REGISTER
# ------------------------------------------------------------------------------- #

CLASSES = (
    # 3D View - Menu
    BMT_MT_Menu_V3D,
    # 3D View - Panels
    BMT_PT_Ops_V3D,
    BMT_PT_Settings_V3D,
)


def register():
    from bpy.utils import register_class
    for cls in CLASSES:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(CLASSES):
        unregister_class(cls)

