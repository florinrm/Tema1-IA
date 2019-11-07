from Driver import Driver
from algos.utils import g
from heapq import heappush, heappop

def UniformCostSearch(state):
    open = []
    open.append((0, state))
    state.parent = None
    visited = []
    while len(open) > 0:
        (_, current) = open.pop(0)
        visited.append((current.x, current.y))

        if current.goal():
            return (current, len(visited))

        for succ in current.succesors():
            if ((succ.x, succ.y) in visited):
                continue
            succ.parent = current
            succ.costFromInitial = g(succ)
            open.append((g(succ), succ))
            open = sorted(open, key=lambda elem: elem[0])

    return False