from pathlib import Path
from functools import reduce
from itertools import chain
from collections import Counter


OCCUPIED = "#"
EMPTY = "L"
FLOOR = "."

MAX_SEATS = 4


def get_seats_grid(filename):
    file = open(filename, "r")
    lines = []
    for line in file:
        lines.append(line)

    return list(map(lambda r: list(r.strip()), lines))


def is_out_of_grid(pos, grid):
    x_size = len(grid)
    y_size = len(grid[0])

    return pos[0] >= 0 and pos[1] >= 0 and \
        pos[0] < x_size and pos[1] < y_size


def check_line_of_sight(index, pos, grid):
    delta_x = index[0] - pos[0]
    delta_y = index[1] - pos[1]

    state = grid[index[0]][index[1]]
    pos_in_sight = (index[0] + delta_x, index[1] + delta_y)

    while state not in [OCCUPIED, EMPTY] and is_out_of_grid(pos_in_sight, grid):
        index = pos_in_sight
        state = grid[index[0]][index[1]]
        pos_in_sight = (index[0] + delta_x, index[1] + delta_y)

    return index


def adjacents_positions(pos, grid, check_sight):
    positions = [(x, y) for x in range(pos[0]-1, pos[0]+2)
                 for y in range(pos[1]-1, pos[1]+2)]

    positions = list(filter(lambda p: is_out_of_grid(p, grid), positions))

    positions.remove(pos)

    if check_sight:
        positions = map(lambda i: check_line_of_sight(i, pos, grid), positions)

    return positions


def occuped_adjacents(pos, grid, check_sight):
    neighbors = adjacents_positions(pos, grid, check_sight)
    return reduce(
        lambda a, n: a + 1 if grid[n[0]][n[1]] == OCCUPIED else a,
        neighbors, 0)


def next_state(pos, grid, max_seats, check_sight):
    current_position = grid[pos[0]][pos[1]]

    if current_position == FLOOR:
        return FLOOR

    elif current_position == OCCUPIED and occuped_adjacents(pos, grid, check_sight) >= max_seats:
        return EMPTY

    elif current_position == EMPTY and occuped_adjacents(pos, grid, check_sight) == 0:
        return OCCUPIED
    else:
        return current_position


def simulate_step(grid, max_seats=MAX_SEATS, check_sight=False):
    next_grid = []
    for x in range(len(grid)):
        row = []
        for y in range(len(grid[0])):
            row.append(next_state((x, y), grid, max_seats, check_sight))

        next_grid.append(row)

    return next_grid


def get_occuped_seats(input_file):
    prev_grid = []
    grid = get_seats_grid(input_file)

    while grid != prev_grid:
        prev_grid = grid
        grid = simulate_step(grid)

    counter = Counter(chain.from_iterable(grid))

    print(f"Occuped Seats: {counter[OCCUPIED]}")


def get_occuped_seats_2(input_file):
    prev_grid = []
    grid = get_seats_grid(input_file)

    while grid != prev_grid:
        prev_grid = grid
        grid = simulate_step(grid, 5, True)

    counter = Counter(chain.from_iterable(grid))

    print(f"Occuped Seats 2 {counter[OCCUPIED]}")


get_occuped_seats("./day-11/seats.txt")
get_occuped_seats_2("./day-11/seats.txt")
