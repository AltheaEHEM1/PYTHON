def factors(n):
    list1 = []
    for i in range(1, n + 1):
        if n % i == 0:
            list1.append(i)
    return list1


num = int(input("Enter an integer: "))
print(f"The factors of {num} are: {factors(num)}")
