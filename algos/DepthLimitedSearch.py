from Driver import Driver

def DepthLimitedSearch(state, k):
    open = [state]
    state.parent = None
    visited = []
    while len(open) > 0:
        current = open.pop(0)
        visited.append((current.x, current.y))

        if current.goal():
            return (current, len(visited))

        if current.depth >= k:
            continue

        for succ in current.succesors():
            if ((succ.x, succ.y) in visited):
                continue
            succ.parent = current
            open.insert(0, succ)
    return False