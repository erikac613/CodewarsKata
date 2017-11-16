def tower_builder(n_floors):
    floorList = []
    startFloor = 1
    width = 2 * n_floors - 1
    for floor in range(1, n_floors + 1):
        thisFloor = "*" * startFloor
        thisFloor = thisFloor.center(width,' ')
        startFloor += 2
        print(thisFloor)
        floorList.append(thisFloor)
    return floorList
