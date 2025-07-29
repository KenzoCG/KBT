# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy

# ------------------------------------------------------------------------------- #
# FUNCTIONS
# ------------------------------------------------------------------------------- #

def prefs():
    name = __name__.partition('.')[0]
    return bpy.context.preferences.addons[name].preferences


def name():
    from .. import bl_info
    return bl_info['name']


def version():
    from .. import bl_info
    version = bl_info['version']
    return (version[0], version[1], version[2])


def name_and_version_string():
    from .. import bl_info
    version = bl_info['version']
    return f"{bl_info['name']} ({version[0]}.{version[1]}.{version[2]})"


def exists(name="", exact_match=False):
    addon_keys = bpy.context.preferences.addons.keys()
    if exact_match:
        if name in addon_keys:
            return True
    else:
        for key in addon_keys:
            if name in key:
                return True
    return False
