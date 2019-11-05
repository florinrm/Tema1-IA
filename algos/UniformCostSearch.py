from Driver import Driver
from algos.utils import g

def UniformCostSearch(state, budget):
    open = [state]
    state.parent = None
    visited = []
    while len(open) > 0:
        current = open.pop(0)
        visited.append((current.x, current.y))
        if current.goal():
            current.fuel = current.fuel + budget
            return current
        for succ in current.succesors():
            if ((succ.x, succ.y) in visited):
                continue
            succ.parent = current
            succ.costFromInitial = g(succ)
            open.append(succ)
            open = sorted(open, key=lambda driver: driver.costFromInitial)
    return False