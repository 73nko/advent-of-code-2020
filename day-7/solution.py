
import re


def read_file_to_list(filename):
    definitions = {}

    file = open(filename, "r")
    for line in file:
        keybag, defbags = line.strip().split('contain')
        rules = defbags.split(',')
        m = re.search("^([a-z\s]+)bag", keybag)
        bag = m.group(1).strip()
        definitions[bag] = []
        for rule in rules:
            if "no other bag" in rule:
                continue
            m = re.search("([0-9]+)([a-z\s]+)bag", rule)
            if not m:
                raise Exception(rule)
            nr = int(m.group(1))
            color = m.group(2).strip()
            definitions[bag].append({"color": color, "nr": nr})

    file.close()
    return definitions


def has_shiny(definitions, key):

    if key == "shiny gold":
        return True

    for rule in definitions[key]:
        if has_shiny(definitions, rule["color"]):
            return True
    return False


def count_bags(definitions, key):
    result = 1
    for rule in definitions[key]:
        result += rule["nr"] * count_bags(definitions, rule["color"])
    return result


result = 0
data = read_file_to_list("rules.txt")
for key in data:
    if key == "shiny gold":
        continue
    if has_shiny(data, key):
        result = result + 1
print(result)

result = count_bags(data, "shiny gold") - 1
print(result)
