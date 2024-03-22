# Starting with importing the General functions and the libraries
from src.lib.all import g
from src.lib.pdf_process.MusicSheet import MusicSheet
from src.app.pdf_process.pdf_opener import list_of_pdfs
from src.app.pdf_process.png_transformer import pdf_to_pngs

# Reading the file:
temp, tempo = list_of_pdfs()
file = '../../../assets/' + temp
images = pdf_to_pngs(file)
sheet = MusicSheet(pages=images)

# Extracting the note from each page:
# Saving it in a list of lists
# Each sub-list contains chains of 24 notes or fewer
# The major list contains a sub-list for each page

# Loading the dictionaries of the note harmonies

# Audio Processing:
# if turn_over_page(tempo, TB_recieve_notes_from_file()):
#    enter intermediate
#    if turn_over_page(tempo, TB_recieve_notes_from_file()):
#       exit intermediate
#       sheet.next_page()
