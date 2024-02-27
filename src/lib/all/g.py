import numpy as np

def cat(a, b):
    a.append(npfy(b))
    return a

def npfy(a):
    return np.array(a)

def nothing(a):
    return a

def gray(image):
    from cv2 import (cvtColor as color, COLOR_BGR2GRAY as gray)
    return color(image, gray)

def multicat(my_range, catter, catted, function=nothing):
    for i in range(my_range):
        catter = cat(catter, function(catted[i]))
    return npfy(catter)


def f(x, function):
    return function(x)



def length(end, beginning):
    return end - beginning

def significantly_greater(old, new, relativity):
    if new - old > relativity:
        return new
    return old

def about_the_same(a, b, relativity):
    if np.abs(a - b) <= relativity:
        return True
    return False

def set(l):
    for e in l:
        e = npfy(e)
    return npfy(l)
