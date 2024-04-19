# Starting with importing the General functions and the libraries
from src.lib.all import g
import os

def list_of_pdfs():
    path_of_assets = os.listdir("../../../assets")
    file_num = 1
    v_file_num = []
    for file in path_of_assets:
        if ends_with_pdf(file):
            print(file_num, ".", file)
            v_file_num = g.cat(v_file_num, [file_num, file])
            file_num += 1
    v_file_num = g.npfy(v_file_num)
    choice = input("choose a file")
    if str(choice) in v_file_num[:, 0]:
        q = v_file_num[int(choice) - 1, 1]
        tempo = input("what tempo are you going to play?\n")
        return q, tempo
    print("Wrong choice, bye bye...")
    return

def ends_with_pdf(path):
    if path[-4:] == ".pdf":
        return True
