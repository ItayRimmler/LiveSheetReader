# Starting with importing the General functions and the libraries
from src.lib.all import g

def pdf_to_pngs(pdf_path):
    from fitz import (open as open_pdf)
    pdf = open_pdf(pdf_path)
    images = []
    for p in range(pdf.page_count):
        page = pdf.load_page(p)
        pixels = page.get_pixmap(dpi=100)
        g.cat(images, g.np.frombuffer(pixels.samples, dtype=g.np.uint8).reshape(pixels.height, pixels.width, 3))
    return g.npfy(images)
