from Driver import Driver

def g(state):
    cost = 0
    while state.parent != None:
        cost = cost + 1
        state = state.parent
    return cost

def h(state):
    if state.goal():
        return 0
    cost = 0
    return 0