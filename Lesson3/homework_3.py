# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве из случайных чисел.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# Последняя строка содержит число X
'''
N = int(input("Enter array length: "))
# numbers = list(map(int, input("Enter numbers in list: ").split()))
numbers = [i for i in range(N)]  # При N = 5, массив Numbers = [0,1,2,3,4]
X = int(input("Enter X: "))

# Initializing count of X
count = 0

# Counting X
for num in numbers:
    if num == X:
        count += 1

# Printing count of X
print(count)
'''
# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n) самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# Последняя строка содержит число X
'''
N = int(input("Enter array length: "))
numbers = [1, 2, 3, 4, 5]
X = int(input("Enter X: "))

# Initializing closest number
closest_number = 0

# Finding closest number
for num in numbers:
    if abs(X - num) < abs(X - closest_number):
        closest_number = num

# Printing closest number
print(closest_number)
'''
