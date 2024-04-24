# Starting with importing the General functions and the libraries
from ver2.src.lib.all import g
from ver2.src.lib.all import constants as c

# Imports specific to this script:
import sounddevice as sd

class Sound:
    def __init__(self, tempo):
        self.tempo = tempo
        self.values = None
        self.notes = None

    def record(self):
        recording = sd.rec(int(c.DUR * self.tempo * c.SR), samplerate=c.SR, channels=c.CH, dtype='int16')
        sd.wait()
        self.values = recording[:, 0]

    def send_to_cpp(self):
        path = "../../../data/recording.bin"
        with open(path, 'wb') as file:
            self.values.tofile(file)