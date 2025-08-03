# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from bpy.props import PointerProperty
# Addon Prefs
from .dev import KBT_PROPS_Dev
from .gui import (
    KBT_PROPS_GUI_Settings,
    KBT_PROPS_GUI_Colors,
    KBT_PROPS_GUI,
)
from .settings import KBT_PROPS_Settings
from .addon import KBT_ADDON_Prefs
# ID Props
from .object import KBT_PROPS_Object
from .mesh import KBT_PROPS_Mesh

# ------------------------------------------------------------------------------- #
# REGISTER
# ------------------------------------------------------------------------------- #

CLASSES = (
    # Addon Prefs
    KBT_PROPS_Dev,
    KBT_PROPS_GUI_Settings,
    KBT_PROPS_GUI_Colors,
    KBT_PROPS_GUI,
    KBT_PROPS_Settings,
    KBT_ADDON_Prefs,
    # ID Props
    KBT_PROPS_Object,
    KBT_PROPS_Mesh,
)


def register():
    from bpy.utils import register_class
    for cls in CLASSES:
        register_class(cls)

    bpy.types.Object.kbt = PointerProperty(type=KBT_PROPS_Object)
    bpy.types.Mesh.kbt = PointerProperty(type=KBT_PROPS_Mesh)


def unregister():
    del bpy.types.Object.kbt
    del bpy.types.Mesh.kbt

    from bpy.utils import unregister_class
    for cls in reversed(CLASSES):
        unregister_class(cls)
