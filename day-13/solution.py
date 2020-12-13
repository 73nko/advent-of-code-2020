import re


def process_input(input_line):
    stripped_input = input_line.strip()
    raw_list = re.split(',', stripped_input)
    times = []
    for j, i in enumerate(raw_list):
        if i == 'x':
            pass
        else:
            times.append((int(i), j))
    return times


with open("./day-13/notes.txt", 'r') as code_file:
    earliest_dep = code_file.readline()
    earliest_dep.rstrip()
    earliest_dep = int(earliest_dep)
    schedule = process_input(code_file.readline())

bus_wait = [bus[0] - earliest_dep % bus[0] for bus in schedule]
my_bus = bus_wait.index(min(bus_wait))

print(f'Solution part 1: {schedule[my_bus][0]*bus_wait[my_bus]}')

ref_time = schedule[0][0]
time_fixed = 0
for bus in schedule:
    flag = 1
    i = 0
    while flag == 1:
        if (time_fixed+ref_time*i + bus[1]) % bus[0] == 0:
            flag = 0
        else:
            i += 1
    time_fixed = time_fixed + ref_time*i
    if bus[1] != 0:
        ref_time = ref_time*bus[0]

print(f'Solution part 2: {time_fixed}')
