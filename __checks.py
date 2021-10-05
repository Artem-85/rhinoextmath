"""
Check-up functions for rhinoextmath package
"""

def is_iterable(item):
    """ Check an item for iterability """
    return (isinstance(item, list) or isinstance(item, tuple))

__all__ = ["is_iterable"] 
