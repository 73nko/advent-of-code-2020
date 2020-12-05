def parseInput(input):
    passwods_file = open(input, 'r')
    passwords_list = passwods_file.read().splitlines()

    for pos, value in enumerate(passwords_list):
        passwords_list[pos] = value.replace("-", " ").replace(":", "").split()
        passwords_list[pos][0] = int(passwords_list[pos][0])
        passwords_list[pos][1] = int(passwords_list[pos][1])

    return passwords_list


def valid_passwords_part1(passwords):
    valid_passwords_count = 0
    for line in passwords:
        if (line[0] <= line[3].count(line[2]) <= line[1]):
            valid_passwords_count += 1
    return "Result puzzle 1: " + str(valid_passwords_count) + " valid passwords"


def valid_passwords_part2(passwords):
    valid_passwords_count = 0
    for line in passwords:
        if (line[3][line[0]-1] == line[2]) != (line[3][line[1]-1] == line[2]):
            valid_passwords_count += 1
    return "Result puzzle 2: " + str(valid_passwords_count) + " valid passwords"


passwords_list = parseInput('passwords.txt')

print(valid_passwords_part1(passwords_list))
print(valid_passwords_part2(passwords_list))
