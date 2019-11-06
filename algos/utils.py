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
    return abs(state.x - state.destinationX) + (state.y - state.destinationY)

def areStatesEqual(state1, state2):
    return state1.x == state2.x and state2.y == state1.y \
           and state1.destinationX == state2.destinationX \
           and state1.destinationY == state2.destinationY

def reconstructPath(state):
    path = []
    while state.parent != None:
        path.append(state.lastMove)
        state = state.parent
    return reversed(path)