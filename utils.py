# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script
#def counter(list):

def countwords(lst:list):
    """
    Goes through each element and adds +1 if it already exists else set the element to 1
    """
    elements={}
    for e in lst:
        if e in elements.keys():
            elements[e] += 1
        else:
            elements[e] = 1
    return(elements)

def dircheck(pa):
    """
    Create a directory if it does not exist and notify the user, else just print that the directory already exists
    """
    if pa.exists()==False:
        print("Directory \"{}\" does not exist - creating now".format(pa))
        pa.mkdir()
    else:
        print("Directory \"{}\" already exists".format(pa))