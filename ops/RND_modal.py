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
import numpy
import time
import traceback
from .. import utils
from ..utils.enums import MODAL_STATUS

# ------------------------------------------------------------------------------- #
# OPERATOR
# ------------------------------------------------------------------------------- #

PRINT_START_STOP = True
PRINT_TIME = False

class MS_OT_RND_Modal(Operator):
    bl_idname      = "ms.rnd_modal"
    bl_label       = "RND Modal"
    bl_options     = {'REGISTER', 'UNDO', 'BLOCKING'}
    bl_description = "Mesh-Sketcher | R&D Modal"

    @classmethod
    def poll(cls, context):
        return context.mode in {'OBJECT', 'EDIT_MESH'}


    def invoke(self, context, event):
        if PRINT_START_STOP:
            print("OP - START")

        try:
            self.status = MODAL_STATUS.RUNNING

            self.events = utils.event.Events()
            self.events.CONFIRM = {'RET', 'NUMPAD_ENTER'}
            self.events.CANCEL  = {'ESC'}
            self.controls = utils.event.Controls(events=self.events)

            self.region_ui_controller = utils.screen.RegionUI_Controller(context)
            self.region_ui_controller.hide(header=False, tool_settings=False, toolbar=False, sidebar=False, last_op=False)

            self.setup(context, event)

            self.shader_handler = utils.handles.ShaderHandler()
            self.shader_handler.register(context, callback_2d=self.draw_2d, callback_3d=self.draw_3d)

            context.window_manager.modal_handler_add(self)
            context.area.tag_redraw()
            return {'RUNNING_MODAL'}

        except Exception as e:
            traceback.print_exc()
            return {'CANCELLED'}


    def setup(self, context, event):
        pass


    def modal(self, context, event):
        start_time = 0
        if PRINT_TIME:
            start_time = time.time()

        try:
            self.status = MODAL_STATUS.RUNNING
            self.controls.update(context, event)
            self.update(context, event)

            if self.controls.confirmed:
                self.status = MODAL_STATUS.FINISHED
            elif self.controls.cancelled:
                self.status = MODAL_STATUS.CANCELLED
            elif self.controls.pass_through:
                self.status = MODAL_STATUS.PASS_THROUGH

        except Exception as e:
            traceback.print_exc()
            self.status = MODAL_STATUS.CANCELLED

        if PRINT_TIME:
            end_time = time.time()
            print(f"TIME - {(end_time-start_time):0.4f}")

        if self.status == MODAL_STATUS.FINISHED or self.status == MODAL_STATUS.CANCELLED:
            return self.close(context)
        elif self.status == MODAL_STATUS.PASS_THROUGH:
            return {'PASS_THROUGH'}

        context.area.tag_redraw()
        return {'RUNNING_MODAL'}


    def update(self, context, event):
        pass


    def close(self, context):
        if PRINT_START_STOP:
            print("OP - STOP")

        try:
            self.shader_handler.unregister()
            self.region_ui_controller.restore()
            self.shader_handler = None
            self.region_ui_controller = None
            del self.shader_handler
            del self.region_ui_controller
        except Exception as e:
            traceback.print_exc()

        if hasattr(context, 'area'):
            if hasattr(context.area, 'tag_redraw'):
                context.area.tag_redraw()

        if self.status == MODAL_STATUS.CANCELLED:
            return {'CANCELLED'}
        return {'FINISHED'}


    def draw_2d(self, context):
        pass


    def draw_3d(self, context):
        pass
