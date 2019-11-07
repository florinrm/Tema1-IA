import moves
from algos.DepthFirstSearch import DepthFirstSearch
from Cell import Cell
from Driver import Driver
import copy
from algos.utils import g, reconstructPath


def RideDepthFirstSearch(clients, driver):
    state = copy.deepcopy(driver)
    total_money = 0
    visited_states = 0

    actions = []

    for client in clients:
        # pick-up client
        state.destinationX = client[0]  # startX client
        state.destinationY = client[1]  # startY client

        print(state)

        budget = client[4]

        result = DepthFirstSearch(state)
        if result == False:
            print('pick-up failed - no fuel')
            return False
        else:
            print('pick-up succeded')
            actions += reconstructPath(result[0])
            visited_states += result[1]
            actions.append(moves.PICKUP)
            print(result)

        # drop client
        print('gotta go to destination')
        result = result[0]
        result.x = state.destinationX
        result.y = state.destinationY

        result.destinationX = client[2]
        result.destinationY = client[3]

        print(result)
        # print('cost ' + str(g(result)))

        final = DepthFirstSearch(result)

        if final == False:
            print('drop failed - no fuel')
            return False
        else:
            actions += reconstructPath(final[0])
            visited_states += final[1]
            actions.append(moves.DROPOFF)
            print(final)

        state = copy.deepcopy(final[0])
        state.x = state.destinationX
        state.y = state.destinationY
        total_money += budget

    return (state, g(state), total_money + state.fuel, actions, visited_states)