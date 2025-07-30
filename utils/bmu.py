# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
import bmesh
import math
import mathutils
from bpy.types import (
    Object,
    Mesh
)
from bmesh.types import (
    BMesh,
    BMVert,
    BMEdge,
    BMFace
)
from mathutils import (
    geometry,
    Vector,
    Matrix,
    Quaternion,
)

# ------------------------------------------------------------------------------- #
# MANAGE
# ------------------------------------------------------------------------------- #

def get_bmesh(obj:Object):
    if isinstance(obj, Object):
        if obj.type == 'MESH':
            bm = None
            if obj.data.is_editmode:
                bm = bmesh.from_edit_mesh(obj.data)
            else:
                bm = bmesh.new()
                bm.from_mesh(obj.data)
            if isinstance(bm, BMesh) and bm.is_valid:
                ensure_tables(bm)
                ensure_indexes(bm)
                return bm
    return None


def close_bmesh(bm:BMesh, obj:Object):
    if isinstance(bm, BMesh) and bm.is_valid:
        if isinstance(obj, Object) and obj.type == 'MESH':
            ensure_selections(bm)
            if bm.is_wrapped:
                bmesh.update_edit_mesh(obj.data)
            else:
                bm.to_mesh(obj.data)
                bm.free()
            obj.data.calc_loop_triangles()
            obj.update_tag()
        else:
            bm.free()
    bm = None
    del bm


def ensure_tables(bm:BMesh):
    if isinstance(bm, BMesh) and bm.is_valid:
        bm.verts.ensure_lookup_table()
        bm.edges.ensure_lookup_table()
        bm.faces.ensure_lookup_table()
        return True
    return False


def ensure_indexes(bm:BMesh):
    if isinstance(bm, BMesh) and bm.is_valid:
        bm.verts.index_update()
        bm.edges.index_update()
        bm.faces.index_update()
        return True
    return False


def ensure_normals(bm:BMesh):
    if isinstance(bm, BMesh) and bm.is_valid:
        bm.normal_update()
        return True
    return False


def ensure_selections(bm:BMesh):
    if isinstance(bm, BMesh) and bm.is_valid:
        tool_sel_mode = bpy.context.tool_settings.mesh_select_mode
        bm.select_mode = {mode for mode, sel in zip(['VERT', 'EDGE', 'FACE'], tool_sel_mode) if sel}
        bm.select_flush_mode()
        bm.select_history.validate()
        return True
    return False

# ------------------------------------------------------------------------------- #
# FUNCTIONS
# ------------------------------------------------------------------------------- #


