# Starting with importing the General functions and the libraries
from src.lib.all import g, Note
from src.lib.chain_process import SubSeries
from config.chain_config import *

class Chain:
    def __init__(self, value):
        self.val = g.npfy([value])
        self.cont = g.npfy([])
        self.score = 0
        if 0 not in self.index():
            self.calc_score()

    def __add__(self, other):
        if isinstance(other, Note.Note):
            return self + Chain(other)
        else:
            self.val = g.np.append(self.val, other.val)
            if self.ngrp() < g.np.max(other.grp()):
                self.more(g.np.max(other.grp()) - self.ngrp())
            if 0 in self.index():
                return self
            self.sort()
            self.update_cont()
            self.score = 0
            self.calc_score()
            return self

    def type(self):
        v_array = []
        for v in self.val:
            v_array.append(v.type)
        return g.npfy(v_array)

    def index(self):
        v_array = []
        for v in self.val:
            v_array.append(v.index)
        return g.npfy(v_array)

    def grp(self):
        v_array = []
        for v in self.val:
            v_array.append(v.grp)
        return g.npfy(v_array)

    def ngrp(self):
        return self.val[0].ngrp

    def sort(self):
        if 0 in self.index():
            return
        self.val = self.val[self.index().argsort()]

    def update_cont(self):
        q = self.index()
        self.cont = []
        for i in range(q.shape[0] - 1):
            self.cont.append(q[i + 1] - q[i] == 1)

    def len(self):
        return self.val.shape[0]

    def calc_score(self):
        if 0 in self.index():
            return
        self.score = 0
        for i in self.index():
            if i == -1:
                self.score -= BAD_NOTE
        self.score += SUBSET_LENGTH(self) * SUBSET_SCORE(self)
        for i in range(self.len()):
            self.score += GROUP_SCORE(self.grp()[i], self.ngrp())
        return True

    def can_I_add(self):
        return self.len() < CHAIN_LEN

    def more(self, value=1):
        for e in self.val:
            e.ngrp += value

    def insert(self, ind, vals):
        for i, v in enumerate(self.val[ind]):
            v.index = vals[i]
        self.sort()
        self.update_cont()

    def match(self, other):
        matched_notes = []
        previous_longest_subseries_length = 0
        list_of_subseries = []
        for k, note in enumerate(self.val):
            for i in range(len(other.type())):
                if note.type == other.type()[i]:
                    list_of_subseries.append(SubSeries.SubSeries(other.val[i]))
                    for j in range(i, len(other.type())):
                        if k < self.len() - 1:
                            if self.val[k + 1].type == other.val[j].type:
                                list_of_subseries[-1] + other.val[j]
                                self.val = g.np.delete(self.val, k + 1)
            for subseries in list_of_subseries:
                new_longest_subseries_length = max(previous_longest_subseries_length, len(subseries.val))
                if not new_longest_subseries_length == previous_longest_subseries_length:
                    for sub_note in subseries.val:
                        matched_notes.append(sub_note)
                previous_longest_subseries_length = new_longest_subseries_length
        self.val = g.npfy(matched_notes)
        self.sort()
        self.update_cont()
        self.calc_score()

    def delete_duplicates(self):
        temp = []
        for i, note in enumerate(self.val):
            if i < self.len() - 1:
                for j in range(i + 1, self.len()):
                    if note == self.val[j]:
                        temp.append(j)
        print(temp)
        return g.np.delete(self.val, temp)

    def __gt__(self, other):
        self.val = g.npfy([x for x in self.val if x.index > other])