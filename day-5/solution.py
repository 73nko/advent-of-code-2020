import math


def find_row(code, min_row, max_row, lower_code, length):
    if length == 1:
        return min_row
    if code[0] == lower_code:
        return find_row(code[1:], min_row, math.floor((max_row+min_row)/2),
                        lower_code, length // 2)
    else:
        return find_row(code[1:], math.ceil((max_row+min_row)/2),
                        max_row, lower_code, length//2)


def find_missing(seat_list):
    return [seat for seat in range(min(seat_list), max(seat_list)+1)
            if seat not in seat_list]


seat_rows = []
seat_columns = []
seat_code = []

with open("seats.txt", 'r') as seats_file:
    seats = seats_file.readlines()

for seat in seats:
    seat_row = find_row(seat[0:7], 0, 127, 'F', 128)
    seat_rows.append(seat_row)
    seat_column = find_row(seat[7:11], 0, 7, 'L', 8)
    seat_columns.append(seat_column)
    seat_code.append(seat_row*8 + seat_column)

print('Long seat code:', max(seat_code))

print('Empty:', find_missing(seat_code)[0])
