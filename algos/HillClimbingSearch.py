from algos.utils import g, h


def HillClimbingSearch(state):
    current = state
    state.parent = None
    done = False
    currentCost = g(current) + h(current)
    maxim = currentCost
    visited = []

    while done == False:
        visited.append((current.x, current.y))
        maxim = currentCost
        nextState = None

        for succ in current.succesors():
            if ((succ.x, succ.y) in visited):
                continue
            cost = g(succ) + h(succ)
            if cost >= maxim:
                maxim = cost
                nextState = succ

        if nextState == None:
            done = True
        else:
            nextState.parent = current
            current = nextState
            currentCost = maxim

    return current