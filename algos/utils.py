from Driver import Driver

def g(state):
    cost = 0
    while state.parent != None:
        cost = cost + 1
        state = state.parent
    return cost