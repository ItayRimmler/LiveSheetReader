import numpy as np
import ver2.src.lib.all.State as State

def cat(a, b):
    a.append(npfy(b))
    return a

def npfy(a):
    return np.array(a)

def nothing(a):
    return a
def multicat(my_range, catter, catted, function=nothing):
    for i in range(my_range):
        catter = cat(catter, function(catted[i]))
    return npfy(catter)


Event = State.State()
