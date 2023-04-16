# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


N = int(int(input("Enter number of elements for list A: ")))
X = int(input("Enter number X to find in the list: "))
count = 0
for i in range(N):
    if num_A[i] == X:
            count += 1
    print(f"I count {X} in list A {count} times")