x = [1, 2, 3, 4, 5]
y = [11, 12, 13, 14, 15]
z = (21, 22, 23, 24, 25)

print('a')
print(3*x)


print('b')
print(x + y)


print('c')
result = [a - b for a, b in zip(x, y)]
print(result)


print('d')
print(x[1])


print('e')
print(x[0])


print('f')
print(x[-1])


print('g')
print(x[:])


print('h')
print(x[2:4])


print('i')
print(x[1:4:2])


print('j')
print(x[:2])


print('k')
print(x[::2])


print('l')
x[3] = 8
print(x)
