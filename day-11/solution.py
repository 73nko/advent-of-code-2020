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


def adjacents_positions(pos, grid):
    indices = [(x, y) for x in range(pos[0]-1, pos[0]+2)
               for y in range(pos[1]-1, pos[1]+2)]

    indices = list(filter(lambda p: is_out_of_grid(p, grid), indices))

    indices.remove(pos)

    return indices


def occuped_adjacents(pos, grid):
    neighbors = adjacents_positions(pos, grid)
    return reduce(
        lambda a, n: a + 1 if grid[n[0]][n[1]] == OCCUPIED else a,
        neighbors, 0)


def next_state(pos, grid):
    current_position = grid[pos[0]][pos[1]]

    if current_position == FLOOR:
        return FLOOR

    elif current_position == OCCUPIED and occuped_adjacents(pos, grid) >= MAX_SEATS:
        return EMPTY

    elif current_position == EMPTY and occuped_adjacents(pos, grid) == 0:
        return OCCUPIED
    else:
        return current_position


def simulate_step(grid):
    next_grid = []
    for x in range(len(grid)):
        row = []
        for y in range(len(grid[0])):
            row.append(next_state((x, y), grid))

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


get_occuped_seats("./day-11/seats.txt")
