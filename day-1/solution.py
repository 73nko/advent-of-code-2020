
def search_expenses(expenses):
    match_of_two_found = False
    match_of_three_found = False
    for first_index, first_expense in enumerate(expenses):
        for second_index, second_expense in enumerate(expenses[first_index+1:]):
            sum_of_two = int(first_expense) + int(second_expense)

            if sum_of_two == 2020:
                product = int(first_expense) * int(second_expense)
                print(
                    f"Match of two:\n {first_expense} * {second_expense} = {product}")
                match_of_two_found = True

            for third_expense in expenses[second_index+1:]:
                sum_of_three = int(first_expense) + \
                    int(second_expense) + int(third_expense)

                if sum_of_three == 2020:
                    product = int(first_expense) * \
                        int(second_expense) * int(third_expense)
                    print(
                        f"Match of three:\n {first_expense} * {second_expense} * {third_expense} = {product}")
                    match_of_three_found = True

        if match_of_two_found & match_of_three_found:
            return
    print("No matches")


with open('expenses.txt', 'r') as input_file:
    expenses = []
    for line in input_file:
        expenses.append(int(line.strip('\n')))


search_expenses(expenses)
