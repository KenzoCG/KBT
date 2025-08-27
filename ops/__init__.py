# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from .RND_modal import KBT_OT_RND_Modal
from .bm_demo_one import KBT_OT_BM_ExampleOne

# ------------------------------------------------------------------------------- #
# REGISTER
# ------------------------------------------------------------------------------- #

CLASSES = (
    KBT_OT_RND_Modal,
    KBT_OT_BM_ExampleOne,
)


def register():
    from bpy.utils import register_class
    for cls in CLASSES:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(CLASSES):
        unregister_class(cls)
