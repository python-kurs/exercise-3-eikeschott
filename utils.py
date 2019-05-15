# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script
#def counter(list):
def countwords(lst):
    elements={}
    for e in lst:
        if e in elements.keys():
            elements[e] += 1
        else:
            elements[e] = 1
    return elements

def dircheck(pa):
    d='"{}"'.format(pa)
    if pa.exists()==False:
        print("Directory", d, "does not exist - creating now")
        pa.mkdir()
    else:
        print("Directory", d, "already exists")