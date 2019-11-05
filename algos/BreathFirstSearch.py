from Driver import Driver

def BreathFirstSearch(state):
    open = [state]
    while len(open) > 0:
        current = open.pop(0)
        if current.goal():
            return current
        for succ in current.succesors():
            open.append(succ)
    return False