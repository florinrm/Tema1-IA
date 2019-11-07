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
    visited_states = 0

    while len(open) > 0:
        (currentCost, current) = open.pop(0)
        visited_states += 1
        visited.append((current.x, current.y))

        if current.goal():
            return current

        closed.append(current)
        for succ in current.succesors():

            if ((succ.x, succ.y)) in visited:
                continue

            cost = h(succ) + g(succ)

            res = findState(succ, closed + list(map(lambda x: x[1], open)))
            if res != False:
                if g(res) < g(succ):
                    continue
                else:
                    if res in closed:
                        closed.remove(res)
                    if res in list(map(lambda x: x[1], open)):
                        open = list(filter(lambda x: x[1] != res, open))

            succ.parent = current
            open.append((cost, succ))
            open = sorted(open, key = lambda x: x[0])

    return False
