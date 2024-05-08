# Starting with importing the General functions and the libraries
from ver2.src.lib.all import g
from ver2.src.lib.all import constants as c

# Imports specific to this script:
# PDF Process imports:
from ver2.src.app.pdf_process.pdf_opener import *
from ver2.src.app.pdf_process.png_transformer import *
from ver2.src.lib.pdf_process.MusicSheet import *
from cv2 import destroyAllWindows as daw
# Audio Process imports:
from ver2.src.lib.audio_process.audio_process import process_tempo
from ver2.src.lib.audio_process.Sound import Sound


# Code for test. Play on the piano a note, see if python was correct, then play 1-3 notes and see if its correct.
a = Sound(1)
a.record()
a.send_to_cpp()
from matplotlib import pyplot as plt
#plt.plot(a.values)
#plt.show()
a.values = g.np.absolute(g.np.fft.fft(a.values))
#from scipy import signal
#l, m = signal.butter(4, 1000, fs=c.SR , btype='low')
#a.values = signal.lfilter(l, m, a.values)
a.values = a.values/max(a.values)
import subprocess as sp
output = sp.check_output(["main.exe"])
result = list(map(int, output.strip().split()))
print("Result:", result)
print(a.index_2_note(result))
plt.plot(list(range(len(a.values))), a.values)
plt.plot([list(range(len(a.values)))[i] for i in result], [a.values[i] for i in result], 'ro')
plt.show()


# Reading the file (PDF Process):
temp, tempo = list_of_pdfs()
file = '../../../assets/' + temp
images = pdf_to_pngs(file)
sheet = MusicSheet(pages=images)
sheet.show()

# Image Process:
if sheet.pages.shape[0] > 1:  # Checks whether there are 2 or more pages.
    image_notes = []
    while not g.Event.num == str(sheet.pages.shape[0]):  # While the number we remember isn't the number of pages
            g.Event.advance()
            g.Event.write("Process Page " + str(g.Event.num) + " + Remember " + str(g.Event.num))
            page_image_notes = []
            g.Event.write("Divide Notes into Chains + Remember + " + str(g.Event.num))
            image_notes.append(page_image_notes)

    # Loading the dictionaries of the note harmonies
    from ver2.data.note_freqs_and_names import name, frequency

    # Audio Processing:
    g.Event.num = 1
    g.Event.write("Remember 1")
    tempo = process_tempo(int(tempo))
    my_sound = Sound(tempo)

    while not g.Event.num == str(sheet.pages.shape[0]):
        g.Event.write("Read Page " + str(g.Event.num) + " Remember " + str(g.Event.num))
        sheet.show()
        g.Event.write("Recording + Remember " + str(g.Event.num))
        my_image = image_notes[g.Event.num]
        if turn_over_page(my_image, my_sound, name, frequency):
            g.Event.advance()
            g.Event.write("Read Page " + str(g.Event.num) + " Remember " + str(g.Event.num))
            sheet.next_page()
            sheet.show()
            # Here you should present both pages next to each other
            g.Event.write("Recording + Intermediate + Remember " + str(g.Event.num))
            my_image = image_notes[g.Event.num]
            if turn_over_page(my_image, my_sound, name, frequency):
                g.Event.write("Next Page + Remember " + str(g.Event.num))
                daw()

if not g.Event.read()[-1].isdigit():
    g.Event.write("Last Page + Remember 1")
else:
    g.Event.write("Last Page + Remember " + str(g.Event.num))
sheet.show(0)

