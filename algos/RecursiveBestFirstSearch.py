from Driver import Driver
from algos.utils import h, g, areStatesEqual

visited = []
actionsList = []

def RecursiveBestFirstSearch(state):
    state.parent = None
    return RecursiveBestFirstSearchHelper(state, 1000)

def RecursiveBestFirstSearchHelper(state, k):
    visited.append((state.x, state.y))
    if (state.lastMove != None):
        actionsList.append(state.lastMove)

    if state.goal():
        visited_states = len(visited)
        visited.clear()
        return (state, visited_states)

    succesors = state.succesors()
    succesors = list(filter(lambda succ: ((succ.x, succ.y)) not in visited, succesors))

    if len(succesors) == 0:
        return (False, 1000)

    for i in range(len(succesors)):
        succesors[i].f = max(g(succesors[i]) + h(succesors[i]), state.f)

    while True:
        print((state.x, state.y))
        succesors = sorted(succesors, key=lambda succ: succ.f)
        best = succesors[0]
        if best.f > k:
            return (False, best.f)

        value = k
        if (len(succesors) > 1):
            alternative = succesors[1].f
            value = min(k, alternative)

        (result, best.f) = RecursiveBestFirstSearchHelper(best, value)

        if result != False:
            return (result, len(visited))