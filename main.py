from Cell import Cell
from Driver import Driver
from informalSearches.RideAStarSearch import RideAStarSearch
from informalSearches.RideGreedyBestFirstSearch import RideGreedyBestFirstSearch
from informalSearches.RideHillClimbingSearch import RideHillClimbingSearch
from informalSearches.RideRecursiveBestFirstSearch import RideRecursiveBestFirstSearch
from strategy import Strategies

from neinformalSearches.RideDepthFirstSearch import RideDepthFirstSearch
from neinformalSearches.RideBreadthFirstSearch import RideBreadthFirstSearch
from neinformalSearches.RideDepthLimitedSearch import RideDepthLimitedSearch
from neinformalSearches.RideIterativeDeepeningSearch import RideIterativeDeepeningSearch
from neinformalSearches.RideUniformCostSearch import RideUniformCostSearch

import time

def parse_input(filename):
    file = open(filename, "r")
    tokens = list(file.readline().split(" "))

    height = int(tokens[0])
    width = int(tokens[1])
    capacity = int(tokens[2])

    tokens = list(file.readline().split(" "))

    carPositionY = int(tokens[0])
    carPositionX = int(tokens[1])

    tokens = list(file.readline().split(" "))
    n = int(tokens[0])

    clients = []
    for _ in range(n):
        tokens = list(file.readline().split(" "))
        startY = int(tokens[0])
        startX = int(tokens[1])
        destinationY = int(tokens[2])
        destinationX = int(tokens[3])
        budget = int(tokens[4])
        clients.append((startX, startY, destinationX, destinationY, budget))

    matrix = []

    file.readline()
    for i in range(height):
        line = file.readline().strip('\n')
        tokens = list(line.split(" "))
        row = []
        for j in range(width):
            cell = Cell(i, j, False, False)

            if j == 0:
                if tokens[j + 1] == ':':
                    cell.moveRight = True
            elif j == width - 1:
                if tokens[j] == ':':
                    cell.moveLeft = True
            else:
                if tokens[j] == ':':
                    cell.moveLeft = True
                if tokens[j + 1] == ':':
                    cell.moveRight = True

            row.append(cell)
        matrix.append(row)
    file.readline()
    file.close()

    driver = Driver(carPositionX, carPositionY, capacity, matrix)

    return (clients, driver)

def search(clients, driver, option):
    if option == Strategies.DepthFirstSearch:
        result = RideDepthFirstSearch(clients, driver)
        if result != False:
            return result
        else:
            print('failed')
            return False
    elif option == Strategies.BreadthFirstSearch:
        result = RideBreadthFirstSearch(clients, driver)
        if result != False:
            return result
        else:
            print('failed')
            return False
    elif option == Strategies.UniformCostSearch:
        result = RideUniformCostSearch(clients, driver)
        if result != False:
            return result
        else:
            print('failed')
            return False
    elif option == Strategies.IterativeDeepeningSearch:
        result = RideIterativeDeepeningSearch(clients, driver)
        if result != False:
            return result
        else:
            print('failed')
            return False
    elif option == Strategies.DepthLimitedSearch:
        result = RideDepthLimitedSearch(clients, driver, 1000)
        if result != False:
            return result
        else:
            print('failed')
            return False
    elif option == Strategies.AStar:
        result = RideAStarSearch(clients, driver)
        if result != False:
            return result
        else:
            print('failed')
            return False
    elif option == Strategies.GreedyBestFirstSearch:
        result = RideGreedyBestFirstSearch(clients, driver)
        if result != False:
            return result
        else:
            print('failed')
            return False
    elif option == Strategies.HillClimbing:
        result = RideHillClimbingSearch(clients, driver)
        if result != False:
            return result
        else:
            print('failed')
            return False
    elif option == Strategies.RecursiveBestFirstSearch:
        result = RideRecursiveBestFirstSearch(clients, driver)
        if result != False:
            return result
        else:
            print('failed')
            return False


def main():
    for i in range(1, 7):
        test_no = i
        (clients, driver_initial_state) = parse_input('test' + str(test_no) + '.in')
        strategy = Strategies.RecursiveBestFirstSearch
        start = time.time()
        result = search(clients, driver_initial_state, strategy)
        end = time.time()
        #print(result)

        measure_time = end - start

        output = open('euclidian-' + strategy.name + '-test' + str(test_no) + '.out', 'w')
        output.write(strategy.name + '\n')
        output.write(str(measure_time) + '\n')
        output.write(str(result[4]) + '\n')
        output.write(str(result[2]) + '\n')
        output.write(str(result[3]))

if __name__ == '__main__':
    main()
