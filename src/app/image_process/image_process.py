# Starting with importing the General functions and the libraries
from src.lib.all import g
from src.lib.chain_process.Chain import Chain
from src.lib.all.Note import Note

def TB_recieve_notes_from_file(file=None):
    fictional_first_note = Note(1, "Do", 1)
    fictional_chain = Chain(fictional_first_note)
    for i in range(1, 14):
        fictional_chain + Chain(Note(1, "Do", i))
    for i in range(14, 24):
        fictional_chain + Chain(Note(2, "Do", i))
    fictional_chain.insert_t([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                             ["Sol", "Mi", "Mi", "Fa", "Re", "Re", "Do", "Re", "Mi", "Fa", "Sol", "Sol", "Sol", "Sol", "Mi"
                              , "Mi", "Fa", "Re", "Re", "Do", "Mi", "Sol", "Sol", "Do"])
    return fictional_chain
