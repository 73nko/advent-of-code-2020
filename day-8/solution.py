import re
import copy


def read_file_to_list(filename):
    list = []
    file = open(filename, "r")
    for line in file:
        order = re.search(r'^([a-z]+)\s+([+-])([0-9]+)', line)
        command = order.group(1).strip()
        sgn = order.group(2).strip()
        argument = int(order.group(3).strip())
        if sgn == '-':
            argument = argument * -1

        list.append({"command": command, "argument": argument})

    file.close()
    return list


def execute_code(data):
    indexes = set()
    index = 0
    acc = 0
    while True:
        if index in indexes:
            return (False, acc)
        if index >= len(data):
            return (True, acc)
        indexes.add(index)
        if data[index]['command'] == "acc":
            acc += data[index]['argument']
            index = index + 1
        else:
            if data[index]['command'] == "nop":
                index = index + 1
            else:
                if data[index]['command'] == "jmp":
                    index = index + data[index]['argument']


def fix_command(data, i):
    data1 = copy.deepcopy(data)
    if(data1[i]['command'] == 'jmp'):
        data1[i]['command'] = 'nop'
    else:
        if(data1[i]['command'] == 'nop'):
            data1[i]['command'] = 'jmp'
    return data1


data = read_file_to_list("code.txt")
_, result = execute_code(data)
print(result)


for i in range(len(data)):
    data1 = fix_command(data, i)
    terminate, result = execute_code(data1)
    if terminate:
        print(result)
        break
