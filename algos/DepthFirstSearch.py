from Driver import Driver

def DepthFirstSearch(state):
    open = [state]
    state.parent = None
    visited = []
    while len(open) > 0:
        current = open.pop(0)
        #print('Current state is: ' + str(current))
        visited.append((current.x, current.y))
        if current.goal():
            return current
        for succ in current.succesors():
            succ.parent = current
            if ((succ.x, succ.y) in visited):
                continue
            #print('Succesor ' + str(succ))

            open.insert(0, succ)
    return False