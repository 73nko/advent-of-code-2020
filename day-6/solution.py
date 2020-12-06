import copy


def get_responses(filename):
    list = []
    person = []
    file = open(filename, "r")
    for line in file:
        if line.strip() == '':
            list.append(person)
            person = []
        else:
            person.append(set([x for x in line.strip()]))
    if person:
        list.append(person)
    file.close()
    return list


def count_yes(group):
    head, *tail = copy.deepcopy(group)
    for person in tail:
        head.update(person)
    return head


def count_all_yes(group):
    head, *tail = copy.deepcopy(group)
    for person in tail:
        head.intersection_update(person)
    return head


reponses = get_responses("responses.txt")

result = 0
for d in reponses:
    s = count_yes(d)
    result = result + len(s)

print(result)

result = 0
for d in reponses:
    s = count_all_yes(d)
    result = result + len(s)

print(result)
