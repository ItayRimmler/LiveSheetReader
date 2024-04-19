# Starting with importing the General functions and the libraries
from src.lib.all import g


class Note:

    def __init__(self, group=0, type="Do", index=0, n_of_groups=1):
        self.ngrp = n_of_groups
        self.grp = group
        self.type = type
        self.index = index
        self.med = False

