"""
Rhino Extended Math

A very simple alternative to numpy for using in Rhino Python
"""
from rhinoextmath.matrix import *

__VERSION = "0.0.1"

def version():
    """
    Returns version (str)
    """
    return str(__VERSION)

__all__ = ["matrix", "version"] 
