import math


def get_map_list(input):
    map_file = open(input, 'r')
    return map_file.readlines()


def traverse_map(map_list, right, down=1):
    position = 0
    trees_hit = 0
    for row in map_list[::down]:
        if '#' == row[position % len(row.strip())]:
            trees_hit += 1
        position += right
    return trees_hit


paths = [
    {'right': 1, 'down': 1},
    {'right': 3, 'down': 1},
    {'right': 5, 'down': 1},
    {'right': 7, 'down': 1},
    {'right': 1, 'down': 2},
]

map_list = get_map_list('map.txt')
hit_trees = []

for path in paths:
    hit_trees.append(traverse_map(map_list, path['right'], path['down']))
    print(
        f"when going right {path['right']} and down {path['down']} we hit {hit_trees[-1]} trees")

print(f"The answer for star 2 is: {math.prod(hit_trees)}")
