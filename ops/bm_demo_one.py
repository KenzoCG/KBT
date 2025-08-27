# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
import bmesh
from bpy.types import Operator
import mathutils
from mathutils import (
    Vector,
    Quaternion,
    Matrix,
)
import math
import time
import traceback
from .. import utils
from ..utils import bmu

# ------------------------------------------------------------------------------- #
# OPERATOR
# ------------------------------------------------------------------------------- #

class KBT_OT_BM_ExampleOne(Operator):
    bl_idname      = "kbt.bm_demo_one"
    bl_label       = "KBT - BM Demo 1"
    bl_options     = {'REGISTER', 'UNDO'}
    bl_description = f"{utils.addon.name()} | BM Demo 1"

    @classmethod
    def poll(cls, context):
        return context.mode == 'OBJECT'


    def execute(self, context):
        obj = utils.object.create_mesh_object(obj_name="Obj", mesh_name="Mesh", link=True)

        with bmu.bmesh_from_object_mode(obj, update=True) as bm:
            generate_mesh(context, bm)

        return {'FINISHED'}


def generate_mesh(context, bm):
    bmu.ensure_tables(bm)
    bmu.ensure_indexes(bm)

    bmesh.ops.create_circle(bm, segments=32, radius=1, matrix=Matrix.Identity(4))
