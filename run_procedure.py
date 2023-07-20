#!python

"""
run_procedure
"""

import argparse
import json
import importlib


parser = argparse.ArgumentParser(prog="RunProcedure", description="This program takes in a" +
                                 "a json file that is a list of funtions and arguments to run" +
                                 "proceduraly",
                                 epilog="If you still have questions look here: " +
                                 "https://docs.python.org/3/library/argparse.html#module-argparse")
# Add some positional arguments
parser.add_argument('conf_file')
args = parser.parse_args()


with open(args.conf_file, mode='r', encoding='utf-8') as file_handle:
    myjson = file_handle.read()

myconf = json.loads(myjson)

test_module = importlib.import_module(myconf['module'])

#The following turns a string that references a function into a python object
# representing the function.  The use of eval is kinda dangerous.  It would allow
# a bad actor to inject code into your system.  In this case... its kinda the intneded
# model of this program.  If you want to get around the use of eval you can hard code
# a function dict like below.
for k in myconf['function_map'].keys():
    myconf['function_map'][k]=eval(myconf['function_map'][k])

##################################################################
##funcdict = {
##    'steps_build':steps.steps_build,
##    'steps_test':steps.steps_test,
##    'steps_deploy':steps.steps_deploy,
##    'steps_clean':steps.steps_clean
##}
###################################################################

results = []

for procedure in myconf['array_of_procedures']:
    results.append([procedure['func'],
                   myconf['function_map'][procedure['func']](*procedure['pos'],
                                                             **procedure['key'])])


print("Summary ..")
for line in results:
    print(line[0], "Pass" if line[1] == 0 else "Fail")
