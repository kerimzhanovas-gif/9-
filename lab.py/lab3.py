data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
numbers.remove(6.13)
numbers.remove(True)
letters.append(True)
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
letters.remove(True)
letters[4] = 't'
letters[7] = 'o'
letters= ['c', 'o', 'd', 'e']
letters = tuple(letters)
numbers = tuple(numbers)
print(letters)
print(numbers)