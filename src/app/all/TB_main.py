# Starting with importing the General functions and the libraries

from src.lib.all import g
from src.lib.pdf_process.MusicSheet import MusicSheet
from src.app.pdf_process.pdf_opener import list_of_pdfs
from src.app.pdf_process.png_transformer import pdf_to_pngs
from src.app.audio_process.audio_process import *
from src.lib.audio_process.Sound import Sound
from src.app.image_process.image_process import TB_recieve_notes_from_file
from data.note_freqs_and_names import name, frequency
print(g.Event.read())


page = TB_recieve_notes_from_file()
tempo = process_tempo(60)
my_sound = Sound(duration=tempo)
turn_over_page(page, my_sound, name, frequency)