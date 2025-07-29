# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import time
import inspect
from .addon import prefs

# ------------------------------------------------------------------------------- #
# TYPES
# ------------------------------------------------------------------------------- #

class FCOLS:
    BLACK   = "\033[30m"
    WHITE   = "\033[37m"
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    BLUE    = "\033[34m"
    YELLOW  = "\033[33m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"


class FMODS:
    RESET     = "\033[0m"
    BOLD      = "\033[1m"
    UNDERLINE = "\033[4m"

# ------------------------------------------------------------------------------- #
# FUNCTIONS
# ------------------------------------------------------------------------------- #

def write_to_console(msg=""):
    # Prefs
    if not prefs().dev.debug_on:
        return
    # Frame
    stack = inspect.stack()
    caller_frame = stack[1]
    function_name = caller_frame.function
    line_number = caller_frame.lineno
    traced = []
    for frame in stack[1:]:
        module = inspect.getmodule(frame[0])
        module_name = module.__name__ if module else "<unknown>"
        traced.append(f"{module_name}.{frame.function}")
    # Divider
    print(f"{FCOLS.RED}{'-' * 120}", FMODS.RESET)
    # Time
    print(f"• {time.ctime()}")
    # Stack
    for i, trace in enumerate(reversed(traced)):
        print(f"{i+1}) {trace}")
    # Function Name
    print(f"• {FCOLS.GREEN}{function_name}{FMODS.RESET} • {FCOLS.CYAN}{line_number}{FMODS.RESET}")
    # Msg
    print(f"• {FMODS.BOLD}{msg}{FMODS.RESET}")
    # Divider
    print(f"{FCOLS.RED}{'-' * 120}{FMODS.RESET}")
    # Reset
    print(FMODS.RESET)