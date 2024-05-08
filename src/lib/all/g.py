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


def is_multiple_within_threshold(x, y, threshold):
    if int(x) == 0 or int(y) >= 10 * int(x):
        return False
    remainder = min(int(y) % int(x), int(y) % int(x - threshold), int(y) % int(x + threshold),int(y - threshold) % int(x), int(y + threshold) % int(x))
    #print("X:", x, "Y:", y, "REM:", remainder, "TH:", threshold)
    return 0 <= remainder <= threshold

