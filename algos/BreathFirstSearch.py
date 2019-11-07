from Driver import Driver

def BreathFirstSearch(state):
    open = [state]
    state.parent = None
    visited = []
    while len(open) > 0:
        current = open.pop(0)
        visited.append((current.x, current.y))
        if current.goal():
            return current
        for succ in current.succesors():
            if ((succ.x, succ.y) in visited):
                continue
            succ.parent = current
            open.append(succ)
    return False