# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from bpy.props import PointerProperty
# Addon Prefs
from .dev import MS_PROPS_Dev
from .gui import (
    MS_PROPS_GUI_Settings,
    MS_PROPS_GUI_Colors,
    MS_PROPS_GUI,
)
from .settings import MS_PROPS_Settings
from .addon import MS_ADDON_Prefs
# ID Props
from .object import MS_PROPS_Object
from .mesh import MS_PROPS_Mesh

# ------------------------------------------------------------------------------- #
# REGISTER
# ------------------------------------------------------------------------------- #

CLASSES = (
    # Addon Prefs
    MS_PROPS_Dev,
    MS_PROPS_GUI_Settings,
    MS_PROPS_GUI_Colors,
    MS_PROPS_GUI,
    MS_PROPS_Settings,
    MS_ADDON_Prefs,
    # ID Props
    MS_PROPS_Object,
    MS_PROPS_Mesh,
)


def register():
    from bpy.utils import register_class
    for cls in CLASSES:
        register_class(cls)

    bpy.types.Object.mesh_sketch = PointerProperty(type=MS_PROPS_Object)
    bpy.types.Mesh.mesh_sketch = PointerProperty(type=MS_PROPS_Mesh)


def unregister():
    del bpy.types.Object.mesh_sketch
    del bpy.types.Mesh.mesh_sketch

    from bpy.utils import unregister_class
    for cls in reversed(CLASSES):
        unregister_class(cls)
