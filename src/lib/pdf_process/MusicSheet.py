# Starting with importing the General functions and the libraries
from src.lib.all import g

class MusicSheet:
    def __init__(self, pages=g.np.array([]), current_page=0):
        self.pages = pages
        temp = []
        self.pages = g.multicat(pages.shape[0], temp, self.pages, g.gray)
        self.current_page = current_page
    def next_page(self):
        self.current_page += 1
    def previous_page(self):
        self.current_page -= 1
    def show(self, wait=1):
        from cv2 import (imshow, setWindowProperty, waitKey, WND_PROP_TOPMOST as full)
        imshow("Loaded Image", self.pages[self.current_page])
        setWindowProperty("Loaded Image", full, 1)
        waitKey(wait)
    def get(self):
        return self.pages[self.current_page]
