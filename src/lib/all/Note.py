# Starting with importing the General functions and the libraries
from ver2.src.lib.all import g
from ver2.src.lib.all import constants as c



class Note:
    def __init__(self, group=0, type="Do", index=0):
        self.grp = group
        self.type = type
        self.index = index

