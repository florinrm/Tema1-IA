from Driver import Driver
from algos.DepthLimitedSearch import DepthLimitedSearch

def IterativeDeepeningSearch(state):
    k = 0
    while True:
        result = DepthLimitedSearch(state, k)
        if result != False:
            return result
        k = k + 1