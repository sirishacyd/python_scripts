#!python
"""
build_json
"""
import json

funcdict = {
    'steps_build':'test_module.steps_build',
    'steps_test':'test_module.steps_test',
    'steps_deploy':'test_module.steps_deploy',
    'steps_clean':'test_module.steps_clean'
}

array_of_procedures = [
    {'func':'steps_build', 'pos':['pheonix_project'], 'key':{'count':21}},
    {'func':'steps_test', 'pos':[], 'key':{'easy':False, 'speed':True}},
    {'func':'steps_deploy', 'pos':[['east', 'west']], 'key':{}},
    {'func':'steps_clean', 'pos':[], 'key':{'nuke':True}},
]

myconfig = {
    'function_map':funcdict,
    'array_of_procedures': array_of_procedures,
    'module':'steps'
}

with open("resources/conf.json", mode="w", encoding="utf-8") as file_handle:
    file_handle.write(json.dumps(myconfig))
