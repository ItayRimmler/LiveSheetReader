# Starting with importing the General functions and the libraries
from src.lib.all import g
from src.lib.chain_process.Chain import Chain
from src.lib.all.Note import Note

def process_tempo(tempo):
    return 60/tempo

def turn_over_page(page, my_sound, name, frequency):
    og_page = page
    input_chain_list = []
    while True:
        if len(input_chain_list) < 1:
            score = []
            input_chain_list = []
            page.unmatch()
            page = og_page
        if not len(input_chain_list) < 2:
            if input_chain_list[-1].len() == 0 and input_chain_list[-2].len() == 0:
                score = []
                input_chain_list = []
                page.unmatch()
                page = og_page
        input_chain_list.append(get_input(my_sound, name, frequency))
        temp = input_chain_list[-1].med()
        if "Intermediate" in list(g.Event.read().split(" ")):
            g.Event.write("Matching + Intermediate + Remember " + list(g.Event.read().split(" "))[-1])
        else:
            g.Event.write("Matching + Remember " + list(g.Event.read().split(" "))[-1])
        page = input_chain_list[-1].match(page)
        input_chain_list[-1].calc_score()
        if not g.np.all(temp == input_chain_list[-1].med()):
            score.append(input_chain_list[-1].score)
        if sum(score) > 0.01 * page.score:
            if "Intermediate" in list(g.Event.read().split(" ")):
                g.Event.write("Matched + Intermediate + Remember " + list(g.Event.read().split(" "))[-1])
            else:
                g.Event.write("Matched + Remember " + list(g.Event.read().split(" "))[-1])
            return True

def get_input(my_sound, name, frequency):
    my_sound.record()
    my_sound.note_detect(frequency, name)
    print(my_sound.note)
    note = Note(type=my_sound.note)
    c = Chain(note)
    return c


