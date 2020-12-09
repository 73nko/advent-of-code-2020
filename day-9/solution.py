import re
import copy


def get_numbers(filename):

    list = []
    file = open(filename, "r")
    for line in file:
        list.append(int(line.strip()))
    return list


class NumCach():
    def __init__(self, preambel):
        self._preambel = preambel
        self._sum = []

    def add(self, number):
        if len(self._sum) >= self._preambel:
            self._sum.pop(0)
            for i in range(self._preambel - 1):
                self._sum[i].pop(1)

        sum = [number]
        for i in range(len(self._sum)):
            sum.append(self._sum[i][0] + number)
        self._sum.append(sum)
        return

    def is_valid(self, number):
        for i in range(self._preambel):
            for x in range(1, len(self._sum[i])):
                if self._sum[i][x] == number:
                    return True
        return False


numbers = get_numbers("numbers.txt")

preamble = 50
nc = NumCach(preamble)


for i in range(len(numbers)):

    if i >= preamble:
        if not nc.is_valid(numbers[i]):
            invalid = numbers[i]
    nc.add(numbers[i])

print(invalid)

weak_numbers = []

index = 0
while index < len(numbers):
    s = sum(weak_numbers)
    if s == invalid:
        print(min(weak_numbers) + max(weak_numbers))
        break
    if s < invalid:
        weak_numbers.append(numbers[index])
        index += 1
    if s > invalid:
        weak_numbers.pop(0)
