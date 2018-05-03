"""Flatten problem"""
import json
def flatten(inlist):
    """Return flatten list from inlist."""
    outlist = []
    for item in inlist:
        if isinstance(item, list):
            inlist.extend(item)
        else:
            outlist.append(item)
    outlist.sort(reverse=True)
    return outlist
print(flatten(json.loads(input())))
