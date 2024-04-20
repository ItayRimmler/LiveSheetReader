# Starting with importing the General functions and the libraries
from ver2.src.lib.all import g
from ver2.src.lib.all import constants as c


class State:
    def __init__(self):
        self.current = "Start"
        self.log = []
        self.num = 0

    def read(self):
        return self.current

    def get_log(self):
        return self.log

    def write(self, other):
        self.log.append(self.current)
        self.current = other

    def show(self):
        print(self.current)

    def advance(self):
        self.num += 1
