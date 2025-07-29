# ------------------------------------------------------------------------------- #
# ADDON
# ------------------------------------------------------------------------------- #

bl_info = {
    "name": "Mesh Sketch",
    "description": "Mesh editing pen tool",
    "author": "KenzoCG",
    "version": (1, 0, 0),
    "blender": (4, 4, 0),
    "location": "View3D",
    "category": "3D View"}

# ------------------------------------------------------------------------------- #
# REGISTER
# ------------------------------------------------------------------------------- #

def register():
    # Load
    from . import utils
    # Props
    from . import props
    props.register()
    # Ops
    from . import ops
    ops.register()
    # Interface
    from . import interface
    interface.register()


def unregister():
    # Interface
    from . import interface
    interface.unregister()
    # Ops
    from . import ops
    ops.unregister()
    # Props
    from . import props
    props.unregister()
