# Starting with importing the General functions and the libraries
from src.lib.all import g

class Sound:
    def __init__(self, duration=2, samplerate=44100, channels=2):
        self.dur = duration
        self.sr = int(samplerate)
        self.ch = int(channels)
        self.time = g.npfy(list(range(-self.sr, self.sr)))
        self.amp = g.np.zeros(self.time.shape)
        self.famp = None
        self.freq = g.np.zeros(self.time.shape)
        self.note = None

    def note_detect(self, frequencies, name):
        # TODO: Figure out how (maybe use ML) to overcome the problem of misrecognizing harmonies.
        # i'll explain:  i tried to recognize a note, and then reduce the fourier where it is to 0, then recognize
        #another one. problem is it still may recognize the same note. sometimes it works as intended, but sometimes
        #this mistake happens. i have a reason to believe that this mistake is simply the program recognizing a harmony
        #of the note. now, why choose ML as a solution: a. its easy and can solve other problems b. lets say i go on the
        #dumb way of reducing a Do note, and its harmonies. what happens if i play 2 notes that one of them is a harmony
        #of the other? with ML, i can overcome this problem.
        file_length = self.amp.shape[0]
        f_s = self.sr  # sampling frequency
        sound = self.amp  # blank array
        sound = g.np.divide(sound, float(2 ** 15))  # scaling it to 0 - 1
        counter = 2  # number of channels mono/sterio
        fourier = g.np.fft.fft(sound)
        fourier = g.np.absolute(fourier)
        imax = g.np.argmax(fourier[0:int(file_length / 2)])  # index of max element
        i_begin = -1
        threshold = 0.3 * fourier[imax]
        for i in range(0, imax + 100):
            if fourier[i] >= threshold:
                if (i_begin == -1):
                    i_begin = i
            if (i_begin != -1 and fourier[i] < threshold):
                break
        i_end = i
        imax = g.np.argmax(fourier[0:i_end + 100])
        freq = (imax * f_s) / (file_length * counter)  # formula to convert index into sound frequency
        for i in range(frequencies.shape[0] - 1):
            if (freq < frequencies[0]):
                note = name[0]
                break
            if (freq > frequencies[-1]):
                note = name[-1]
                break
            if freq >= frequencies[i] and frequencies[i + 1] >= freq:
                if freq - frequencies[i] < (frequencies[i + 1] - frequencies[i]) / 2:
                    note = name[i]
                else:
                    note = name[i + 1]
                break
        self.note = note


    def record(self):
        import sounddevice as sd
        recording = sd.rec(int(self.dur * self.sr), samplerate=self.sr, channels=self.ch, dtype='float64')
        sd.wait()
        self.amp = recording[:, 0] #* 5
