def main():
    x = int(input('Enter the size of the list: '))

    my_list = []  # Changed variable name to avoid conflicts with built-in names

    for i in range(x):
        num = int(input('Enter an integer: '))
        my_list.append(num)
    return my_list


def a(integer_list):  # Changed function argument name to match the return value of main()
    result = sum(integer_list)  # Sum of all items in the list
    print("The total of all the items in the list: ", result)


def b(integer_list):  # Changed function argument name to match the return value of main()
    last = integer_list[-1]  # Last input in the list
    print("The last input in the list: ", last)


def c(integer_list):  # Changed function argument name to match the return value of main()
    reversed_list = list(reversed(integer_list))  # Reverse the list
    print("This is the reverse order of the list: ", reversed_list)


def d(integer_list):
    if 5 in integer_list:
        print('Yes')
    else:
        print('No')
def e(integer_list):
    numlessthan = sum(1 for num in integer_list if num < 5)

    # Print the count of integers less than 5
    print(f'There are {numlessthan} integers in the list that are less than 5.')


def f(integer_list):
    num = integer_list[1:-1]
    sortednum = sorted(num)
    print("List after removing first and last elements:", sortednum)


while True:
    selection = int(input("Enter your choice (1-6, 0 to exit): "))
    if selection == 0:
        print("Exiting the program.")
        break
    if selection in range(1, 7):
        integer_list = main()
        if selection == 1:
            a(integer_list)
        elif selection == 2:
            b(integer_list)
        elif selection == 3:
            c(integer_list)
        elif selection == 4:
            d(integer_list)
        elif selection == 5:
            e(integer_list)
        elif selection == 6:
            f(integer_list)
    else:
        print("Invalid selection")
