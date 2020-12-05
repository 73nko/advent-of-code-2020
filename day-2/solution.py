def parseInput(input):
    passwodsFile = open(input, 'r')
    passwordsList = passwodsFile.read().splitlines()

    for pos, value in enumerate(passwordsList):
        passwordsList[pos] = value.replace("-", " ").replace(":", "").split()
        passwordsList[pos][0] = int(passwordsList[pos][0])
        passwordsList[pos][1] = int(passwordsList[pos][1])

    return passwordsList


def validPasswordsPart1(passwords):
    validPasswordsCounts = 0
    for line in passwords:
        if (line[0] <= line[3].count(line[2]) <= line[1]):
            validPasswordsCounts += 1
    return "Result puzzle 1: " + str(validPasswordsCounts) + " valid passwords"


def validPasswordsPart2(passwords):
    validPasswordsCounts = 0
    for line in passwords:
        if (line[3][line[0]-1] == line[2]) != (line[3][line[1]-1] == line[2]):
            validPasswordsCounts += 1
    return "Result puzzle 2: " + str(validPasswordsCounts) + " valid passwords"


passwordList = parseInput('passwords.txt')

print(validPasswordsPart1(passwordList))
print(validPasswordsPart2(passwordList))
