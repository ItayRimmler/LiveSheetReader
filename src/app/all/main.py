# Starting with importing the General functions and the libraries
import cv2

from src.lib.all import g
from src.lib.pdf_process.MusicSheet import MusicSheet
from src.app.pdf_process.pdf_opener import list_of_pdfs
from src.app.pdf_process.png_transformer import pdf_to_pngs
from src.app.audio_process.audio_process import *
from src.lib.audio_process.Sound import Sound

# Reading the file:
temp, tempo = list_of_pdfs()
print(g.Event.read())
file = '../../../assets/' + temp
images = pdf_to_pngs(file)
sheet = MusicSheet(pages=images)
sheet.show()

if sheet.pages.shape[0] > 1:  # True:
    # Extracting the note from each page:
    while not list(g.Event.read().split(" "))[-1] == str(sheet.pages.shape[0]):  # str(2):
        if not (list(g.Event.read().split(" "))[-1].isdigit()):
            g.Event.write("Process Page 1 + Remember 1")
            g.Event.write("Divide Notes into Chains + Remember + 1")
        else:
            g.Event.write("Process Page " + str(int(list(g.Event.read().split(" "))[-1]) + 1) + " + Remember " +\
                          str(int(list(g.Event.read().split(" "))[-1]) + 1))
            g.Event.write("Divide Notes into Chains + Remember + " + list(g.Event.read().split(" "))[-1])

    # Saving it in a list of lists
    # Each sub-list contains chains of 24 notes or fewer
    # The major list contains a sub-list for each page

    # Loading the dictionaries of the note harmonies
    from data.note_freqs_and_names import name, frequency

    # Audio Processing:
    g.Event.write("Remember 1")
    tempo = process_tempo(int(tempo))
    my_sound = Sound(duration=tempo)
    while not list(g.Event.read().split(" "))[-1] == str(sheet.pages.shape[0]):
        g.Event.write("Read Page " + list(g.Event.read().split(" "))[-1] + " Remember " + list(g.Event.read().split(" "))[-1])
        sheet.show()
        g.Event.write("Recording + Remember " + list(g.Event.read().split(" "))[-1])
        if turn_over_page(sheet.pages[sheet.current_page], my_sound, name, frequency):
            g.Event.write("Read Page " + str(int(list(g.Event.read().split(" "))[-1]) + 1) + " Remember " + str(int(list(g.Event.read().split(" "))[-1]) + 1))
            sheet.next_page()
            # change the windows so they will be visable side by side here
            sheet.show()
            g.Event.write("Recording + Intermediate + Remember " + list(g.Event.read().split(" "))[-1])
            if turn_over_page(sheet.pages[sheet.current_page], my_sound, name, frequency):
                g.Event.write("Next Page + Remember " + list(g.Event.read().split(" "))[-1])
                cv2.destroyAllWindows()

if not g.Event.read()[-1].isdigit():
    g.Event.write("Last Page + Remember 1")
else:
    g.Event.write("Last Page + Remember " + (list(g.Event.read().split(" "))[-1]))
sheet.show(0)
