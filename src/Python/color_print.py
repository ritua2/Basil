"""
BASICS

Prints in color
"""

# Colors
colors = {
    "RED":"\033[0;31m",
    "GREEN": "\033[0;32m",
    "YELLOW": "\033[1;33m",
    "BLUE": "\033[1;34m",
    "PURPLE": "\033[1;35m",
    "NC": "\033[0m" # No color
}


def color_print(text, color, at_end="\n"):
    print(colors[color]+text+colors["NC"], end=at_end)