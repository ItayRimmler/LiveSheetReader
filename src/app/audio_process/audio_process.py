# Starting with importing the General functions and the libraries
from src.lib.all import g
from src.lib.chain_process.Chain import Chain
from src.lib.all.Note import Note


def TB_recieve_notes_from_input(file=None):
    fictional_first_note = Note(1, "Do", 1)
    fictional_chain = Chain(fictional_first_note)
    for i in range(1, 21):
        fictional_chain + Chain(Note())
    fictional_chain.insert_t([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                             ["Sol", "Mi", "Fa", "Re", "Re", "Do", "Re", "Mi", "Fa", "Sol", "Sol", "Sol", "Sol", "Mi"
                              , "Mi", "Fa", "Re", "Re", "Do", "Mi", "Sol", "Sol"])
    return fictional_chain


def process_tempo(tempo):
    return 60/tempo