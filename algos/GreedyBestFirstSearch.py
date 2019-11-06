from Driver import Driver
from algos.utils import h

def GreedyBestFirstSearch(state):
    open = [(0, state)]
    state.parent = None
    visited = []
    while len(open) > 0:
        (_, current) = open.pop(0)
        visited.append((current.x, current.y, current.destinationX, current.destinationY))
        if current.goal():
            return current
        for succ in current.succesors():
            if ((succ.x, succ.y, succ.destinationX, succ.destinationY) in visited):
                continue
            succ.parent = current
            succ.estimatedCost = h(succ)
            open.append((h(succ), succ))
            open = sorted(open, key=lambda x: x[0])
    return False