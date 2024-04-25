# Starting with importing the General functions and the libraries
from ver2.src.lib.all import g
from ver2.src.lib.all import constants as c

def process_tempo(tempo):
    return 60/tempo

def get_input(my_sound, name, frequency):
    my_sound.record()
    my_sound.send_to_cpp()
    #my_sound.note_detect(frequency, name)
    #note = Note(type=my_sound.note)
