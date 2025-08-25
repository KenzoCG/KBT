# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
import bmesh
import math
import mathutils
from contextlib import contextmanager
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

@contextmanager
def bmesh_from_object_mode(obj, update=False):
    if not isinstance(obj, Object) or not isinstance(obj.data, Mesh):
        yield None
        return
    bm = bmesh.new(use_operators=True)
    bm.from_mesh(obj.data)
    try:
        yield bm
    finally:
        if update:
            bm.select_flush_mode()
            bm.to_mesh(obj.data)
            obj.data.update()
        bm.free()
        del bm


@contextmanager
def bmesh_from_edit_mode(obj, update=False):
    if not isinstance(obj, Object) or not isinstance(obj.data, Mesh) or not obj.data.is_editmode:
        yield None
        return
    bm = bmesh.from_edit_mesh(obj.data)
    try:
        yield bm
    finally:
        if update:
            bm.select_flush_mode()
            bmesh.update_edit_mesh(obj.data, loop_triangles=False)
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


