# Begin with an empty list
items = [67, 62.9, "hi", False, 8, 67, 'apple', 6.5]
print(items)

print('a')
items.append("banana")
items.append(67)
print(items)


print('b')
items.insert(3, "dog")
print(items)

print('c')
items.insert(0, 909)
print(items)

print('d')
indexfcn = items.index("hi")
print('index of hi: ', indexfcn)

print('e')
countof67 = items.count(67)
print('count  of 67 is: ', countof67)

print('f')
items.remove(67)
print(items)

print('g')
indexoffalse = items.index(False)
items.pop(indexoffalse)
print(items)