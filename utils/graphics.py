# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import bpy
import blf
import gpu
from gpu import state
from gpu_extras.batch import batch_for_shader
from mathutils import (
    Vector,
    Matrix,
    Quaternion
)
from math import (
    cos,
    sin,
    pi,
)
from . import addon
from . import screen

# ------------------------------------------------------------------------------- #
# CONSTANTS
# ------------------------------------------------------------------------------- #

UNIFORM_COLOR = gpu.shader.from_builtin('UNIFORM_COLOR')
SMOOTH_COLOR = gpu.shader.from_builtin('SMOOTH_COLOR')

# ------------------------------------------------------------------------------- #
# TYPES
# ------------------------------------------------------------------------------- #

class COLORS:
    WHITE  = Vector((1.0, 1.0, 1.0, 1.0))
    BLACK  = Vector((0.0, 0.0, 0.0, 1.0))
    GREY   = Vector((0.5, 0.5, 0.5, 1.0))
    RED    = Vector((1.0, 0.0, 0.0, 1.0))
    GREEN  = Vector((0.0, 1.0, 0.0, 1.0))
    BLUE   = Vector((0.0, 0.0, 1.0, 1.0))
    CYAN   = Vector((0.0, 1.0, 1.0, 1.0))
    YELLOW = Vector((1.0, 1.0, 0.0, 1.0))
    ORANGE = Vector((1.0, 0.2, 0.0, 1.0))
    PURPLE = Vector((1.0, 0.0, 1.0, 1.0))


class BLENDING_MODES:
    NONE             = 'NONE'             # No blending
    ALPHA            = 'ALPHA'            # The original color channels are interpolated according to the alpha value
    ALPHA_PREMULT    = 'ALPHA_PREMULT'    # The original color channels are interpolated according to the alpha value with the new colors pre-multiplied by this value
    ADDITIVE         = 'ADDITIVE'         # The original color channels are added by the corresponding ones
    ADDITIVE_PREMULT = 'ADDITIVE_PREMULT' # The original color channels are added by the corresponding ones that are pre-multiplied by the alpha value
    MULTIPLY         = 'MULTIPLY'         # The original color channels are multiplied by the corresponding ones
    SUBTRACT         = 'SUBTRACT'         # The original color channels are subtracted by the corresponding ones
    INVERT           = 'INVERT'           # The original color channels are replaced by its complementary color


class DEPTH_TEST:
    NONE          = 'NONE'           # No depth testing
    ALWAYS        = 'ALWAYS'         # The depth test always passes, regardless of existing depth
    LESS          = 'LESS'           # Passes if new depth is less than the existing depth
    LESS_EQUAL    = 'LESS_EQUAL'     # Passes if new depth is less than or equal to the existing depth
    EQUAL         = 'EQUAL'          # Passes if new depth is equal to the existing depth
    GREATER       = 'GREATER'        # Passes if new depth is greater than the existing depth
    GREATER_EQUAL = 'GREATER_EQUAL'  # Passes if new depth is greater than or equal to the existing depth

# ------------------------------------------------------------------------------- #
# STATE
# ------------------------------------------------------------------------------- #

def set_blending_mode(mode=BLENDING_MODES.NONE):
    state.blend_set(mode)


def set_depth_test(test=DEPTH_TEST.NONE):
    if test == DEPTH_TEST.NONE:
        state.depth_test_set(DEPTH_TEST.NONE)
        state.depth_mask_set(False)
    else:
        state.depth_test_set(test)
        state.depth_mask_set(True)


def set_scissor_test(on=False, x_pos=0, y_pos=0, x_size=0, y_size=0):
    if on:
        state.scissor_set(x_pos, y_pos, x_size, y_size)
        state.scissor_test_set(True)
    else:
        state.scissor_set(0, 0, 0, 0)
        state.scissor_test_set(False)


def set_point_size(size=0):
    state.point_size_set(size)


def set_line_width(width=0):
    state.line_width_set(width)

# ------------------------------------------------------------------------------- #
# UNIFORM COLOR BATCHES
# ------------------------------------------------------------------------------- #

def gen_uniform_color_points_batch(points=None):
    """
    points : list of vectors
    """
    return batch_for_shader(UNIFORM_COLOR, 'POINTS', {"pos": points})


def gen_uniform_color_line_batch(lines=None):
    """
    lines : list of vectors, vectors will be paired
    """
    return batch_for_shader(UNIFORM_COLOR, 'LINES', {"pos": lines})


def gen_uniform_color_tri_batch(tris=None):
    """
    tris : list of tuples containing 3 vectors each
    """
    points = [v for tri in tris for v in tri]
    indices = [(i, i+1, i+2) for i in range(0, len(tris), 3)]
    return batch_for_shader(UNIFORM_COLOR, 'TRIS', {"pos": points}, indices=indices)


def gen_uniform_color_tri_batch_indexed(points=None, indices=None):
    """
    points  : list of vectors
    indices : list of tuples where each tuple contains 3 integers
    """
    return batch_for_shader(UNIFORM_COLOR, 'TRIS', {"pos": points}, indices=indices)


def draw_uniform_color_batch(batch, color=(0,0,0,1)):
    UNIFORM_COLOR.uniform_float("color", color)
    batch.draw(UNIFORM_COLOR)

# ------------------------------------------------------------------------------- #
# SMOOTH COLOR BATCHES
# ------------------------------------------------------------------------------- #

def gen_smooth_color_line_batch(lines=None, colors=None):
    """
    lines  : list of vectors, vectors will be paired
    colors : list of vectors with length 4, count must match total points
    """
    return batch_for_shader(SMOOTH_COLOR, 'LINES', {"pos": lines, "color": colors})


def gen_smooth_color_tri_batch(tris=None, colors=None):
    """
    tris   : list of tuples containing 3 vectors each
    colors : list of vectors with length 4, count must match total points
    """
    points = [v for tri in tris for v in tri]
    indices = [(i, i+1, i+2) for i in range(0, len(points), 3)]
    return batch_for_shader(SMOOTH_COLOR, 'TRIS', {"pos": points, "color": colors}, indices=indices)


def gen_smooth_color_tri_batch_indexed(points=None, colors=None, indices=None):
    """
    points  : list of vectors
    colors  : list of vectors of length 4, count must match total points
    indices : list of tuples where each tuple contains 3 integers
    """
    return batch_for_shader(SMOOTH_COLOR, 'TRIS', {"pos": points, "color": colors}, indices=indices)


def draw_smooth_color_batch(batch):
    batch.draw(SMOOTH_COLOR)

# ------------------------------------------------------------------------------- #
# PRESETS
# ------------------------------------------------------------------------------- #

def draw_circle_2d(radius=12, res=32, center=Vector((0,0)), color=(0,0,0,1)):
    step = (pi * 2) / res
    points = [ Vector((cos(step * i), sin(step * i))) * radius + center for i in range(res + 1)]
    batch = batch_for_shader(UNIFORM_COLOR, 'LINE_STRIP', {"pos": points})
    UNIFORM_COLOR.uniform_float("color", color)
    batch.draw(UNIFORM_COLOR)

# ------------------------------------------------------------------------------- #
# TEXT
# ------------------------------------------------------------------------------- #

def get_scaled_font_size(size=12):
    return size * screen.ui_scale()


def get_scaled_font_size_from_prefs():
    prefs = addon.prefs()
    size = prefs.gui.settings.font_size
    return size * screen.ui_scale()


def get_measured_font_height(size=12):
    blf.size(0, size)
    font_h = round(blf.dimensions(0, "Klgjy`")[1])
    return font_h


def get_measured_font_descender(size=12):
    blf.size(0, size)
    font_h = round(blf.dimensions(0, "Klgjy`")[1])
    return round(font_h / 4)


def get_measured_text_dimensions(text="", size=12):
    blf.size(0, size)
    width, height = blf.dimensions(0, text)
    return width, height


def set_word_wrap(on=True, width=100):
    if on:
        blf.word_wrap(0, width)
        blf.enable(0, blf.WORD_WRAP)
    else:
        blf.disable(0, blf.WORD_WRAP)
        blf.word_wrap(0, 0)


def draw_text(text="", x=0, y=0, size=12, color=(1,1,1,1)):
    blf.position(0, x, y, 0)
    blf.size(0, int(size))
    blf.color(0, *color)
    blf.draw(0, text)
