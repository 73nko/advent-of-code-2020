from collections import Counter, defaultdict
from functools import reduce
import copy


def sort_adapters(adapters):
    adapters.append(0)
    sorted_adapters = sorted(adapters)
    sorted_adapters.append(max(sorted_adapters)+3)
    return sorted_adapters


def get_joltages(filename):
    list = []
    file = open(filename, "r")
    for line in file:
        list.append(int(line.strip()))
    return sort_adapters(list)


def count_joltages(adapters):
    differences = map(
        lambda e: e[1] - adapters[e[0] - 1],
        enumerate(adapters[1:], 1))

    return Counter(differences)


def calc_combinations(adapters):
    combination_product = defaultdict(int)

    combination_product[0] = 1

    for i in adapters[1:]:
        combination_product[i] = combination_product[i-1] + \
            combination_product[i-2] + combination_product[i-3]

    return combination_product[max(adapters)]


adapters = get_joltages("./day-10/adapters.txt")

jolt_differences = count_joltages(adapters)
print(f"part 1: {jolt_differences[1] * jolt_differences[3]}")

combinations = calc_combinations(adapters)
print(f"Part 2: {combinations}")
