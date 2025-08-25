# ------------------------------------------------------------------------------- #
# Author     : KenzoCG
# Copyright  : ©CGBoundary
# ------------------------------------------------------------------------------- #

# ------------------------------------------------------------------------------- #
# ADDON
# ------------------------------------------------------------------------------- #

bl_info = {
    'name'       : "KBT",
    'description': "KenzoCG Blender Addon Template",
    'author'     : "KenzoCG",
    'version'    : (1, 0, 0),
    'blender'    : (4, 5, 0),
    'location'   : "View3D",
    'category'   : "3D View",
}

# ------------------------------------------------------------------------------- #
# REGISTER
# ------------------------------------------------------------------------------- #

def register():
    # Handles
    from . import utils
    utils.register()
    # Props
    from . import props
    props.register()
    # Ops
    from . import ops
    ops.register()
    # Interface
    from . import interface
    interface.register()
    # Keys
    register_keymaps()


def unregister():
    # Keys
    unregister_keymaps()
    # Interface
    from . import interface
    interface.unregister()
    # Ops
    from . import ops
    ops.unregister()
    # Props
    from . import props
    props.unregister()
    # Handles
    from . import utils
    utils.unregister()

# ------------------------------------------------------------------------------- #
# KEYMAPS
# ------------------------------------------------------------------------------- #

KEYS = []


def register_keymaps():
    # Global
    import bpy
    global KEYS
    # Addons
    kc = bpy.context.window_manager.keyconfigs.addon
    # Keymap
    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
    # Menu V3D
    kmi = km.keymap_items.new("wm.call_menu", 'Q', "PRESS", ctrl=False, shift=False, alt=False)
    kmi.properties.name = "KBT_MT_Menu_V3D"
    KEYS.append((km, kmi))


def unregister_keymaps():
    # Global
    import bpy
    global KEYS
    # Keymaps
    keymaps = [km for km, kmi in KEYS]
    # Remove Keymap Items
    for km, kmi in KEYS:
        km.keymap_items.remove(kmi)
    # Remove Keymaps
    kc = bpy.context.window_manager.keyconfigs.addon
    for km in keymaps[:]:
        if km.name in kc.keymaps.keys():
            kc.keymaps.remove(km)
    # Clear
    KEYS = []
