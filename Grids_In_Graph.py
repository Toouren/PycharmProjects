from queue import Queue


def neighbors(node):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = []
    for dir in dirs:
        x = node[0] + dir[0]
        y = node[1] + dir[1]
        neighbor = (x, y)
        if 0 <= neighbor[0] < 40 and 0 <= neighbor[1] < 50:
            result.append(neighbor)


    return tuple(result)


def create_came_from_dict(towered_positions):

    start_position = (18, 0)

    frontier = Queue()
    frontier.put(start_position)

    came_from = {}
    came_from[start_position] = start_position

    for towered_position in towered_positions:
        came_from[towered_position] = False

    while not frontier.empty():
        current = frontier.get()
        for neighbor in neighbors(current):
            if neighbor not in came_from:
                frontier.put(neighbor)
                came_from[neighbor] = current

    return came_from