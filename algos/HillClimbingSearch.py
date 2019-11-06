from algos.utils import g, h


def HillClimbingSearch(state):
    current = state
    state.parent = None
    done = False
    currentCost = g(current) + h(current)
    maxim = currentCost

    while done == False:
        maxim = currentCost
        nextState = None

        for succ in current.succesors():
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