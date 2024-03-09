# Starting with importing the General functions and the libraries
from src.lib.all import g
from src.lib.chain_process import Chain
import math
CONT_SCORE = 1
LEN_SCORE = 1
CHAIN_LEN = 8
def SUBSET_LENGTH(chain):
    return g.np.sum(chain.cont)

def SUBSET_SCORE(chain):
    a = []
    b = 1
    if g.np.sum(chain.cont) > 0:
        for i in range(len(chain.cont)):
            if chain.cont[i]:
               b += 1
               if g.np.sum(chain.cont[i:]) == 1:
                   a.append(b)
                   b = 1
            else:
                a.append(b)
                b = 1
    else:
        a = g.np.ones(len(chain.cont) + 1)
    return g.np.mean(g.npfy(a))/2*g.np.max(a)

BAD_NOTE = 0.5


def GROUP_SCORE(gr, ngr):
    return math.exp(gr) * ngr