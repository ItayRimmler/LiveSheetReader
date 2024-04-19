class SubSeries:
    def __init__(self, note):
        self.val = [note]
    def __add__(self, other):
        self.val.append(other)
    def type(self):
        v_array = []
        for v in self.val:
            v_array.append(v.type)
        return v_array
    def index(self):
        v_array = []
        for v in self.val:
            v_array.append(v.index)
        return v_array