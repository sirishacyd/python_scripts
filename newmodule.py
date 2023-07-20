# newmodule.py
"""
newmodule

Demonstrate python modules and functions
"""
import random

def hello_world():
    """
    This is just going to print hello world
    """
    print("Hello World")

def repeater(r_min, r_max):
    """
    Call hello_world between min & max times
    """
    iterations = our_choice(r_min, r_max)

    while iterations > 0:
        hello_world()
        iterations -=1

def our_choice(r_min, r_max):
    """
    return a random number between min and max
    """
    the_choice = random.choice(list(range(r_min, r_max + 1)))
    # The above list generation could have also been done with list comprehention
    # [v for v in range(r_min, r_max + 1)]

    return the_choice
