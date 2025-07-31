# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from bpy.props import PointerProperty
# Addon Prefs
from .dev import BMT_PROPS_Dev
from .gui import (
    BMT_PROPS_GUI_Settings,
    BMT_PROPS_GUI_Colors,
    BMT_PROPS_GUI,
)
from .settings import BMT_PROPS_Settings
from .addon import BMT_ADDON_Prefs
# ID Props
from .object import BMT_PROPS_Object
from .mesh import BMT_PROPS_Mesh

# ------------------------------------------------------------------------------- #
# REGISTER
# ------------------------------------------------------------------------------- #

CLASSES = (
    # Addon Prefs
    BMT_PROPS_Dev,
    BMT_PROPS_GUI_Settings,
    BMT_PROPS_GUI_Colors,
    BMT_PROPS_GUI,
    BMT_PROPS_Settings,
    BMT_ADDON_Prefs,
    # ID Props
    BMT_PROPS_Object,
    BMT_PROPS_Mesh,
)


def register():
    from bpy.utils import register_class
    for cls in CLASSES:
        register_class(cls)

    bpy.types.Object.bmt = PointerProperty(type=BMT_PROPS_Object)
    bpy.types.Mesh.bmt = PointerProperty(type=BMT_PROPS_Mesh)


def unregister():
    del bpy.types.Object.bmt
    del bpy.types.Mesh.bmt

    from bpy.utils import unregister_class
    for cls in reversed(CLASSES):
        unregister_class(cls)
