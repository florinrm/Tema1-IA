from Driver import Driver

def DepthFirstSearch(state):
    open = [state]
    state.parent = None
    visited = []
    while len(open) > 0:
        current = open.pop(0)
        visited.append((current.x, current.y, current.destinationX, current.destinationY))
        if current.goal():
            return current
        for succ in current.succesors():
            if ((succ.x, succ.y, succ.destinationX, succ.destinationY) in visited):
                continue
            succ.parent = current
            open.insert(0, succ)
    return False