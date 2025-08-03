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
from ..utils.enums import (
    MODAL_STATUS,
    GUI_STATUS,
    ANCHOR,
    SPAN,
)

# ------------------------------------------------------------------------------- #
# OPERATOR
# ------------------------------------------------------------------------------- #

PRINT_START_STOP = True
PRINT_TIME = False

class KBT_OT_RND_Modal(Operator):
    bl_idname      = "kbt.rnd_modal"
    bl_label       = "RND Modal"
    bl_options     = {'REGISTER', 'UNDO', 'BLOCKING'}
    bl_description = f"{utils.addon.name()} | R&D Modal"

    @classmethod
    def poll(cls, context):
        return context.mode in {'OBJECT', 'EDIT_MESH'}


    def invoke(self, context, event):
        # Start
        if PRINT_START_STOP:
            print("OP - START")
        # Setup
        try:
            # Standards
            self.status = MODAL_STATUS.RUNNING
            self.events = utils.event.Events()
            self.events.CONFIRM = {'RET', 'NUMPAD_ENTER'}
            self.events.CANCEL  = {'ESC'}
            self.controls = utils.event.UserControls(events=self.events)
            self.region_ui_controller = utils.screen.RegionUI_Controller(context)
            self.region_ui_controller.hide(header=True, tool_settings=True, toolbar=True, sidebar=True, last_op=True)
            # Startup
            self.startup(context, event)
            # Shader
            self.shader_handler = utils.shader.ShaderHandler()
            self.shader_handler.register(context, callback_2d=self.draw_2d, callback_3d=self.draw_3d)
            # Modal
            context.window_manager.modal_handler_add(self)
            context.area.tag_redraw()
            return {'RUNNING_MODAL'}
        # Error
        except Exception as e:
            traceback.print_exc()
            if hasattr(self, 'shader_handle'):
                try:
                    self.shader_handler.unregister()
                except Exception as e:
                    print(f"{self.bl_label} : Failed to unregister ")
                    self.__user_callback_2d = None
                    traceback.print_exc()
            return {'CANCELLED'}


    def close(self, context):
        # Stop
        if PRINT_START_STOP:
            print("OP - STOP")
        # Reset
        try:
            self.shader_handler.unregister()
            self.region_ui_controller.restore()
            self.shader_handler = None
            self.region_ui_controller = None
            del self.shader_handler
            del self.region_ui_controller
        except Exception as e:
            traceback.print_exc()
        # Shutdown
        try:
            self.shutdown(context)
        except Exception as e:
            traceback.print_exc()
        # Redraw
        if hasattr(context, 'area'):
            if hasattr(context.area, 'tag_redraw'):
                context.area.tag_redraw()
        # Cancel
        if self.status == MODAL_STATUS.CANCELLED:
            return {'CANCELLED'}
        # Confirm
        return {'FINISHED'}


    def modal(self, context, event):
        # Time
        start_time = 0
        if PRINT_TIME:
            start_time = time.time()
        # Reset
        self.status = MODAL_STATUS.RUNNING
        # Update
        try:
            self.controls.update(context, event)
            self.update(context, event)
            # Controls Status
            if self.controls.confirmed:
                self.status = MODAL_STATUS.FINISHED
            elif self.controls.cancelled:
                self.status = MODAL_STATUS.CANCELLED
            elif self.controls.pass_through:
                self.status = MODAL_STATUS.PASS_THROUGH
        except Exception as e:
            traceback.print_exc()
            self.status = MODAL_STATUS.CANCELLED
        # Time
        if PRINT_TIME:
            end_time = time.time()
            print(f"TIME - {(end_time-start_time):0.4f}")
        # Close
        if self.status == MODAL_STATUS.FINISHED or self.status == MODAL_STATUS.CANCELLED:
            return self.close(context)
        # Pass
        elif self.status == MODAL_STATUS.PASS_THROUGH:
            return {'PASS_THROUGH'}
        # Running
        context.area.tag_redraw()
        return {'RUNNING_MODAL'}

    # --- Operations --- #

    def startup(self, context, event):
        gui = utils.gui
        # Menu
        self.menu = gui.menus.Menu(context, event)
        self.menu.build()


    def shutdown(self, context):
        # Menu
        self.menu.close(context)
        # Cancel
        if self.status == MODAL_STATUS.CANCELLED:
            pass
        # Confirm
        else:
            pass


    def update(self, context, event):
        # Menu
        self.menu.update(context, event)


    def draw_2d(self, context):
        # Menu
        self.menu.draw_2d(context)


    def draw_3d(self, context):
        pass
