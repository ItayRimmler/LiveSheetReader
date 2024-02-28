# Starting with importing the General functions and the libraries
from src.lib.all import g
from src.lib.chain_process.Chain import Chain
from src.lib.all.Note import Note

def TB_recieve_notes_from_input(file=None):
    fictional_first_note = Note(1, "Do", 1)
    fictional_chain = Chain(fictional_first_note)
    for i in range(1, 9):
        for j in range(1, 9):
            fictional_chain + Chain(Note(i, "Do", 8 * (i - 1) + j + 1))
    fictional_chain.insert_t([0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22],
                             ["Sol", "Mi", "Fa", "Fa", "Re", "Re", "Re", "Mi", "Fa", "Sol", "Sol", "Sol", "Fa", "Re"
                              , "Re", "Fa", "Re", "Re", "Re", "Sol", "Sol"])
    return fictional_chain
