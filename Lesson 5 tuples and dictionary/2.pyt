input_tuples = input("Enter a 2 integer  separated by commas: ")

tuples_list = []
tuple_strings = input_tuples.split(',')
for tup_str in tuple_strings:
    
    tup = tuple(map(int, tup_str.strip('()').split(',')))
    tuples_list.append(tup)


K = int(input("Enter an integer value K: "))


divisible_tuples = []
for tup in tuples_list:
    divisible = all(num % K == 0 for num in tup)
    if divisible:
        divisible_tuples.append(tup)

print("Tuples divisible by", K, "are:")
for tup in divisible_tuples:
    print(tup)
