#Write a Python program to create a list of
# tuples having first element as the number and second
# element as the square of the number.
# Input: list = [1, 2, 3] Output: [(1, 1), (2, 4), (3, 9)]

def create_tuple(numbers):
    tuple_list = [(num, num ** 2) for num in numbers]
    return tuple_list


input_tuple = [1,2,3]
output_tuple = create_tuple(input_tuple)
print(output_tuple)



