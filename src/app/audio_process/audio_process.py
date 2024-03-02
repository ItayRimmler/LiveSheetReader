# Starting with importing the General functions and the libraries
from src.lib.all import g
from src.lib.chain_process.Chain import Chain
from src.lib.all.Note import Note
from src.lib.audio_process.Sound import TB_was_sound_made


def TB_get_input_with_timeout(timeout):
    from inputimeout import inputimeout, TimeoutOccurred
    try:
        # Wait for input with a timeout
        user_input = inputimeout(timeout=timeout)
        return user_input.strip()
    except TimeoutOccurred:
        # Handle timeout
        return None

def TB_play_caps(a):
    if a == "D":
        return "Do"
    if a == "R":
        return "Re"
    if a == "M":
        return "Mi"
    if a == "F":
        return "Fa"
    if a == "S":
        return "Sol"
    if a == "L":
        return "La"
    if a == "C":
        return "Si"
    if a == "D2":
        return "Do2"
    if a == "R2":
        return "Re2"
    if a == "M2":
        return "Mi2"
    if a == "F2":
        return "Fa2"
    if a == "S2":
        return "Sol2"
    return None


def process_tempo(tempo):
    return 60/tempo

def turn_over_page(tempo, page):
    og_page = page
    input_chain_list = []
    while True:
        if len(input_chain_list) < 1:
            score = []
            input_chain_list = []
            page.unmatch()
            page = og_page
        if not len(input_chain_list) < 2:
            if len(input_chain_list[-1]) == 0 and len(input_chain_list[-2]) == 0:
                score = []
                input_chain_list = []
                page.unmatch()
                page = og_page
        input_chain_list.append(get_input_for_k_seconds(tempo*2))
        for a in input_chain_list:
            for b in a:
                temp = b.med()
                b.match(page)
                if not g.np.all(temp == b.med()):
                    score.append(b.score)
        for a in input_chain_list:
            for b in a:
                print(b.type())
        if sum(score) > 0.004 * page.score:
            return True

def get_input_for_k_seconds(k):
    l = []
    note = None
    c = None
    import time
    t = time.time()
    typ = None
    while time.time() - t < k:
        if c:
            l[-1] + note
        elif typ:
            c = Chain(note)
            l.append(c)
        if TB_was_sound_made():
            # note = Sound.get_note()
            typ = TB_play_caps(TB_get_input_with_timeout(k))
            if typ:
                note = Note(type=typ)
        if len(l) > 0:
            if not l[-1].can_I_add():
                c = None
    return l

