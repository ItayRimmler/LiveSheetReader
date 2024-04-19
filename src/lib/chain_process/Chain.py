# Starting with importing the General functions and the libraries
from src.lib.all import g, Note
from src.lib.chain_process import SubSeries
from config.chain_config import *

class Chain:
    def __init__(self, value, page_num=1):
        self.val = g.npfy([value])
        self.cont = g.npfy([])
        self.score = 0
        self.page_num = page_num
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

    def __sub__(self, other):
        if isinstance(other, int):
            mask = self.val != other
            self.val = self.val[mask]
            return self

    def type(self):
        v_array = []
        for v in self.val:
            v_array.append(v.type)
        return v_array

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

    def med(self):
        v_array = []
        for v in self.val:
            v_array.append(v.med)
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
        self.score = 0
        if 0 in self.index() or 0 in self.grp():
            return
        self.score += SUBSET_LENGTH(self) * SUBSET_SCORE(self)
        for i in range(self.len()):
            self.score += GROUP_SCORE(self.grp()[i])
        return True

    def can_I_add(self):
        return self.len() < CHAIN_LEN

    def more(self, value=1):
        for e in self.val:
            e.ngrp += value

    def insert_i(self, ind, vals):
        for i, v in enumerate(self.val[ind]):
            v.index = vals[i]
        self.sort()
        self.update_cont()
        self.calc_score()

    def insert_t(self, ind, vals):
        for i, v in enumerate(self.val[ind]):
            v.type = vals[i]
        self.sort()
        self.update_cont()
        self.calc_score()


    def match(self, other):
        med_notes = None  # This will be a chain of notes that we will return
        flag = False  # A flag that signifies if we already opened a chain or not
        notes = self.val
        onotes = other.val  # other notes
        note_subseries = []  # a list of chains from notes
        other_note_subseries = []  # a list of chains from other notes
        ind_subseries = []  # the indices of the notes in the chains inside note_subseries
        ind_subseries_o = []  # ditto, but this will not be manipulated
        done = []  # a list of indices inside ind_subseries_o that are done
        other_ind_subseries = []  # the indices of the notes in the chains inside other_note_subseries
        med_ind = []  # indices from ind_subseries that are marked potentially as matched
        med_other_ind = []  # indices from other_ind_subseries that are marked potentially as matched
        ind_of_max = 0  # index of the maximum length chain
        max_len_of_subseries = 0  # the maximum length of a chain
        ## SEGMENT ZERO ##
        already_matched = onotes[other.med() == True]
        onotes = onotes[other.med() == False]
        ## SEGMENT A1 ##
        for i in range(self.len() + 1):
            for j in range(self.len() + 1):
                if j < i:
                    note_subseries.append(Chain(notes[j]))
                    for k in range(j + 1, i):
                        note_subseries[-1] + notes[k]
                    series = []
                    for k in range(j, i):
                        series.append(k)
                    ind_subseries.append(series)
                    ind_subseries_o.append(series)
        ## SEGMENT A2 ##
        for i in range(onotes.shape[0] + 1):
            for j in range(onotes.shape[0] + 1):
                if j < i:
                    other_note_subseries.append(Chain(onotes[j]))
                    for k in range(j + 1, i):
                        other_note_subseries[-1] + onotes[k]
                    series = []
                    for k in range(j, i):
                        series.append(k)
                    other_ind_subseries.append(series)
        while True:
            ## SEGMENT B ##
            for k, sub in enumerate(note_subseries):
                for q, osub in enumerate(other_note_subseries):
                    if osub.len() == sub.len():
                        if osub.type() == sub.type():
                            if not (k in done):
                                med_ind.append(ind_subseries[k])
                            med_other_ind.append(other_ind_subseries[q])
                            break
            ## SEGMENT C1 ##
            if len(med_other_ind) == 0:
                notes[0].index = -1
                med_notes = Chain(notes[0])
                for note in notes[1:]:
                    if note.index == 0:
                        note.index = -1
                        med_notes + note
                break
            ## SEGMENT C2 ##
            if len(med_ind) == 0:
                break
            ## SEGMENT D ##
            subseries_lengths = [len(i) for i in med_ind]
            for j, i in enumerate(subseries_lengths):
                if i > max_len_of_subseries:
                    max_len_of_subseries = i
                    ind_of_max = j
            ## SEGMENT E1 ##
            if not med_notes:
                flag = True
                onotes[med_other_ind[ind_of_max]][0].med = True
                med_notes = Chain(onotes[med_other_ind[ind_of_max][0]])
            ## SEGMENT E2 ##
            if flag:
                for i in onotes[med_other_ind[ind_of_max][1:]]:
                    i.med = True
                    med_notes + i
            ## SEGMENT E3 ##
            else:
                for i in onotes[med_other_ind[ind_of_max]]:
                    i.med = True
                    med_notes + i
            ## SEGMENT E4 ##
            flag = False
            ## SEGMENT F1 ##
            for k, sub in enumerate(ind_subseries):
                if any(element in sub for element in med_ind[ind_of_max]):
                    done.append(k)
            ## SEGMENT F2 ##
            temp = []
            ## SEGMENT F3 ##
            for q, osub in enumerate(other_ind_subseries):
                if not any(element in osub for element in med_other_ind[ind_of_max]):
                    temp.append(q)
            ## SEGMENT F4 ##
            other_ind_subseries = [other_ind_subseries[i] for i in temp]
            ## SEGMENT F5 ##
            other_note_subseries = [other_note_subseries[i] for i in temp]
            ## SEGMENT G ##
            if len(other_ind_subseries) == 0:
                for note in notes:
                    if note.index == 0:
                        note.index = -1
                        med_notes + note
                break
            ## SEGMENT H ##
            med_ind = []
            med_other_ind = []
            max_len_of_subseries = 0
        ## SEGMENT I ##
        other.val = onotes
        for i in already_matched:
            other + i
        other.sort()
        self.val = med_notes.val
        return other

    def delete_duplicates(self):
        temp = []
        for i, note in enumerate(self.val):
            if i < self.len() - 1:
                for j in range(i + 1, self.len()):
                    if note == self.val[j]:
                        temp.append(j)
        return g.np.delete(self.val, temp)

    def unmatch(self):
        for i in self.val:
            i.med = False

    def __gt__(self, other):
        self.val = g.npfy([x for x in self.val if x.index > other])