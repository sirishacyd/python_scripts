#!python
"""
regex_ohya
Demonstrate basic use of python regex
"""
import re

# This is a great resousrce: https://pythex.org/
# So is this:
# https://www.dataquest.io/wp-content/uploads/2019/03/python-regular-expressions-cheat-sheet.pdf

# Ok here we go

bpf_changes = re.compile(r'type=BPF.*prog-id=(\d+)\sop=(\w+)')
new_starts = re.compile(r'type=SERVICE_START.*pid=(\d+)')

with open("resources/audit.log", mode="r", encoding="utf-8") as file_handle:
    audit_txt = file_handle.read()

bpf_result = bpf_changes.findall(audit_txt)
print(bpf_result)

new_start_result = new_starts.findall(audit_txt)
if len(set(new_start_result)) > 1:
    print('Sound the Alarm')
