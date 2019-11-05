from Driver import Driver
from algos.DepthLimitedSearch import DepthLimitedSearch

def IterativeDeepeningSearch(state, budget):
    k = 0
    while True:
        result = DepthLimitedSearch(state, budget, k)
        if result != False:
            return result
        k = k + 1