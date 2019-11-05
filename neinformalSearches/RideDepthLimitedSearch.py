from algos.DepthLimitedSearch import DepthLimitedSearch
from Cell import Cell
from Driver import Driver
import copy
from algos.utils import g

def RideDepthLimitedSearch(clients, driver, k):
    state = copy.deepcopy(driver)
    for client in clients:
        # pick-up client
        state.destinationX = client[0] #startX client
        state.destinationY = client[1] #startY client

        print(state)

        budget = client[4]

        result = DepthLimitedSearch(state, 0, k)
        if result == False:
            print('pick-up failed - no fuel')
            return False
        else:
            print('pick-up succeded')
            print(result)

        #drop client
        print('gotta go to destination')
        result.x = state.destinationX
        result.y = state.destinationY

        result.destinationX = client[2]
        result.destinationY = client[3]

        print(result)
        #print('cost ' + str(g(result)))

        final = DepthLimitedSearch(result, budget, k)

        if final == False:
            print('drop failed - no fuel')
            return False
        else:
            print(final)

        state = copy.deepcopy(final)
        state.x = state.destinationX
        state.y = state.destinationY

    return (state, g(state))