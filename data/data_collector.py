# TODO: Record sounds of a piano, sometimes include one note, sometimes multiple, and alter the parameters of recording.
# TODO: This file should look normal...
# TODO: DO NOT WORK HARD. LOOK UP ONLINE IF ANYONE DID THIS ALREADY
# https://www.youtube.com/watch?v=rj9NOiFLxWA
import csv

# Starting with importing the General functions and the libraries
from src.lib.all import g
from src.lib.audio_process.Sound import Sound
from data.note_freqs_and_names import name, frequency

nam = ["Below C0", "C0", "C#0", "D0", "D#0", "E0", "F0", "F#0", "G0", "G#0", "A0", "A#0", "B0", "C1", "C#1", "D1", "D#1", "E1", "F1",
     "F#1", "G1", "G#1", "A1", "A#1", "B1", "C2", "C#2", "D2", "D#2", "E2", "F2", "F#2", "G2", "G2#", "A2", "A2#", "B2",
     "C3", "C3#", "D3", "D3#", "E3", "F3", "F3#", "G3", "G3#", "A3", "A3#", "B3", "C4", "C4#", "D4", "D4#", "E4", "F4",
     "F4#", "G4", "G4#", "A4", "A4#", "B4", "C5", "C5#", "D5", "D5#", "E5", "F5", "F5#", "G5", "G5#", "A5", "A5#", "B5",
     "C6", "C6#", "D6", "D6#", "E6", "F6", "F6#", "G6", "G6#", "A6", "A6#", "B6", "C7", "C7#", "D7", "D7#", "E7", "F7",
     "F7#", "G7", "G7#", "A7", "A7#", "B7", "C8", "C8#", "D8", "D8#", "E8", "F8", "F8#", "G8", "G8#", "A8", "A8#", "B8",
     "Beyond B8"]

# Creating Sound objects:
data_sound_1 = Sound()
data_sound_2 = Sound(duration=1)
data_sound_3 = Sound(duration=0.6)
data_sound_4 = Sound(samplerate=22050)
data_sound_5 = Sound(duration=1, samplerate=22050)
data_sound_6 = Sound(duration=0.6, samplerate=22050)
data_sound_7 = Sound(channels=1)
data_sound_8 = Sound(duration=1, channels=1)
data_sound_9 = Sound(duration=0.6, channels=1)
data_sound_10 = Sound(channels=1, samplerate=22050)
data_sound_11 = Sound(duration=1, channels=1, samplerate=22050)
data_sound_12 = Sound(duration=0.6, channels=1, samplerate=22050)
data_sound_13 = Sound(samplerate=88200)
data_sound_14 = Sound(duration=1, samplerate=88200)
data_sound_15 = Sound(duration=0.6, samplerate=88200)
data_sound_16 = Sound(channels=1)
data_sound_17 = Sound(duration=1, channels=1)
data_sound_18 = Sound(duration=0.6, channels=1)
data_sound_19 = Sound(channels=1, samplerate=88200)
data_sound_20 = Sound(duration=1, channels=1, samplerate=88200)
data_sound_21 = Sound(duration=0.6, channels=1, samplerate=88200)

# Creating a list containing them:
data_sound_list = [data_sound_1, data_sound_2, data_sound_3, data_sound_4, data_sound_5, data_sound_6, data_sound_7,
                   data_sound_8, data_sound_9, data_sound_10, data_sound_11, data_sound_12, data_sound_13,
                   data_sound_14, data_sound_15, data_sound_16, data_sound_17, data_sound_18, data_sound_19,
                   data_sound_20, data_sound_21]

# Starting to collect data:
import csv
with open('audio_data_for_ML.csv', 'w', newline='') as f:
    w = csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    print("Let's record")
    for s in data_sound_list:
        for i in range(100):
            if i == 0:
                print("Test attempt. This won't affect anything")
                s.record()
                s.note_detect1(frequency, name, s.ch)
            if 0 < i < 34:
                print("Play 1 note")
                s.famp = None
                s.record()
                l = []
                for j in range(5):
                    d1, d2 = s.note_detect1(frequency, name, s.ch)
                    l.append(d1)
                    l.append(d2)
                a1 = input("What note was it?")
                a2 = input("Specify")
                w.writerow(l + [a1, frequency[nam.index(a2)]])
                from matplotlib import pyplot as plt
                plt.plot(list(range(s.amp.shape[0])), )
                plt.show()
