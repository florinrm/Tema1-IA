from Driver import Driver

def DepthFirstSearch(state):
    open = [state]
    while len(open) > 0:
        current = open.pop(0)
        if current.goal():
            return current
        for succ in current.succesors():
            open.insert(0, succ)
    return False