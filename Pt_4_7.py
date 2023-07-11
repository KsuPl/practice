from itertools import permutations
lst = []
for i in input("Введите список элементов через пробел: ").split():
    lst.append(i)
for i in permutations(lst):
    print(*i)
