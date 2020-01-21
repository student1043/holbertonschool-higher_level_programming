#!/usr/bin/python3
def add_attribute(obj, name, value):
    """Definition To Add Attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
