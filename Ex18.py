# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from collections import Counter


N = abs(int(input(f"Enter number of elements for list A: ")))
input(f"Enter list elements divided by space: ").split()
A_num = list(map(int))
if len(A_num) != N or N == 0:
    print(f"Wrong number of elements!")
else:
    X = int(input(f"Enter X to add for comparison: "))
    min - abs(X - A_num(0))
    index = 0
for i in range(1, N):
    Counter - abs(X - A_num[i])
    if Counter < min:
        min = Counter
        index = i
print(f"Number {A_num[index]} in the list is close to {X}, difference is {abs(X - A_num[index])}")