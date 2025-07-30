# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
from . import addon
from . import bmu
from . import context
from . import debug
from . import enums
from . import event
from . import graphics
from . import maths
from . import ray
from . import screen
from . import shader
from . import shapes
from . import gui

# ------------------------------------------------------------------------------- #
# REGISTER
# ------------------------------------------------------------------------------- #

def register():
    from .shader import unload_shader_handles
    bpy.app.handlers.load_post.append(unload_shader_handles)


def unregister():
    from .shader import unload_shader_handles
    bpy.app.handlers.load_post.remove(unload_shader_handles)
