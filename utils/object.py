# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
import math
import mathutils
from bpy.types import (
    Context, Object, Mesh,
)
from mathutils import (
    geometry, Vector, Matrix, Quaternion,
)

# ------------------------------------------------------------------------------- #
# OBJECT
# ------------------------------------------------------------------------------- #

def create_mesh_object(obj_name="Object", mesh_name="Mesh", link=True):
    mesh = bpy.data.meshes.new(mesh_name)
    obj = bpy.data.objects.new(obj_name, mesh)
    if link:
        bpy.context.scene.collection.objects.link(obj)
    return obj


def delete_mesh_object(obj):
    if isinstance(obj, Object):
        mesh = obj.data
        if obj.name in bpy.data.objects:
            bpy.data.objects.remove(obj, do_unlink=True)
        if mesh.name in bpy.data.meshes:
            bpy.data.meshes.remove(mesh, do_unlink=True)
