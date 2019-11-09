import copy

from Driver import Driver
from algos.DepthLimitedSearch import DepthLimitedSearch

def IterativeDeepeningSearch(state):
    k = 0
    limit = 1000
    while True:
        find = copy.deepcopy(state)
        result = DepthLimitedSearch(find, k)
        print(k)
        if result != False:
            return result
        if k == limit:
            return False
        k = k + 1