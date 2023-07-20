#!python
"""
usemodule

This module provides examples on how use custom built modules
"""


import newmodule
import newmodule as nm
from newmodule import repeater

print("Lets call the hello_world function")
newmodule.hello_world()

print()
print("Lets call the repeater function")
newmodule.repeater(3, 7)

print()
print("Lets call nm.repeater")
nm.repeater(3,7)

print()
print("Lets just call repeater")
repeater(3,7)
