# Starting with importing the General functions and the libraries
from ver2.src.lib.all import g
from ver2.src.lib.all import constants as c

# Imports specific to this script:
import sounddevice as sd
import math
from ver2.data.note_freqs_and_names import name, frequency

class Sound:
    def __init__(self, tempo):
        self.tempo = tempo
        self.values = None
        self.notes = None

    def record(self):
        recording = sd.rec(2 ** math.ceil(math.log2(int(c.DUR * self.tempo * c.SR))), samplerate=c.SR, channels=c.CH, dtype='int16')
        sd.wait()
        self.values = recording[:, 0]

    def send_to_cpp(self, path="../../../data/recording.bin"):
        with open(path, 'wb') as file:
            self.values.tofile(file)

    def index_2_note(self, nums):
        self.notes = []
        for num in nums:
            freq = (num * c.SR) / (self.values.shape[0] * c.CH)
            for i in range(frequency.shape[0] - 1):
                if (freq < frequency[0]):
                    note = name[0]
                    break
                if (freq > frequency[-1]):
                    note = name[-1]
                    break
                if freq >= frequency[i] and frequency[i + 1] >= freq:
                    if freq - frequency[i] < (frequency[i + 1] - frequency[i]) / 2:
                        note = name[i]
                    else:
                        note = name[i + 1]
                    break
            self.notes.append(note)
