from pathlib import Path
from collections import defaultdict

INPUT = "9,12,1,4,17,0,18"


def play_turn(game):
    turn = game["turn"]
    number = game["number"]

    prev_turn = game["memory"][number]

    if prev_turn == 0:
        new_number = 0
    else:
        new_number = turn - prev_turn

    game["memory"][number] = turn

    game["number"] = new_number
    game["turn"] = turn + 1

    return game


def init_game(init_string):
    init_data = init_string.split(",")

    game = {}
    game["memory"] = defaultdict(int)

    for t, n in enumerate(init_data[:-1]):
        game["memory"][int(n)] = t + 1

    game["turn"] = len(init_data)
    game["number"] = int(init_data[-1])

    return game


def play_n_turns(n, game):
    while game["turn"] < n:
        game = play_turn(game)
    return game


def part1():
    game = init_game(INPUT)
    result = play_n_turns(2020, game)

    number = result["number"]
    print(f"The 2020th number is {number}.")


def part2():
    game = init_game(INPUT)
    i = 30_000_000
    result = play_n_turns(i, game)

    number = result["number"]
    print(f"The {i}th number is {number}.")


part1()
part2()
