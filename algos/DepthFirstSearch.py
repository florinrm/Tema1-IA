from Driver import Driver

def DepthFirstSearch(state, budget):
    open = [state]
    state.parent = None
    while len(open) > 0:
        current = open.pop(0)
        if current.goal():
            current.fuel = current.fuel + budget
            return current
        for succ in current.succesors():
            succ.parent = current
            open.insert(0, succ)
    return False