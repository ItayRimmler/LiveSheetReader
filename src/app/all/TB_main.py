# Starting with importing the General functions and the libraries
from src.lib.all import g
from src.lib.pdf_process.MusicSheet import MusicSheet
from src.app.pdf_process.pdf_opener import list_of_pdfs
from src.app.pdf_process.png_transformer import pdf_to_pngs

temp, tempo = list_of_pdfs()
file = '../../../assets/' + temp
images = pdf_to_pngs(file)
sheet = MusicSheet(pages=images)
