from Driver import Driver
from algos.utils import h, g, areStatesEqual

def findState(state, space):
    for element in space:
        if areStatesEqual(state, element):
            return element
    return False

def AStarSearch(state):
    open = [(h(state) + g(state), state)]
    state.parent = None
    closed = []
    visited = []

    while len(open) > 0:
        (currentCost, current) = open.pop(0)
        visited.append((current.x, current.y, current.destinationX, current.destinationY))

        if current.goal():
            return current

        closed.append(current)
        for succ in current.succesors():

            if ((succ.x, succ.y, succ.destinationX, succ.destinationY)) in visited:
                continue

            cost = h(succ) + g(succ)

            res = findState(succ, closed + map(lambda x: x[1], open))
            if res != False:
                if g(res) < g(succ):
                    continue
                else:
                    if res in closed:
                        closed.remove(res)
                    if res in map(lambda x: x[1], open):
                        open = filter(lambda x: x[1] != res, open)

            res.parent = succ
            open.append((cost, succ))
            open = sorted(open, key = lambda x: x[0])

    return False
