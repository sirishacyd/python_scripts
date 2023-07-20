#!python
"""The purpose of this module is to show the main feature of the argprase module"""
import argparse


parser = argparse.ArgumentParser(prog="ComplexUserInput",
                                 description="Show off features of argparse",
                                 epilog="If you still have questions look here: " +
                                 "https://docs.python.org/3/library/argparse.html#module-argparse")
# Add some positional arguments
parser.add_argument('in_file')
parser.add_argument('count', type=int)
# Addsome options
parser.add_argument('-o', '--output', help='Location of the output file', dest='out_file')
parser.add_argument('-c', '--color', help='I just needed another argument', default='blue')

# There is a 'required' flag in the add_argument function, but I would suggest
# following std convention and not use it.  In general in linux positional arguments are
# required and options, arguments specificed by a - or -- are considered optional.  The python
# argparse module has been inplemented to follow that convention, which means by default
# options are optional and positional arguments are required.

# Actually parse the args
args = parser.parse_args()

# Show the value of the args that have been read in
print(args.in_file)
print(args.count + 7)
print(args.out_file)
print(args.color)
