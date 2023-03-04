# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую неотрицательную степень B с помощью рекурсии.

'''
Функция проверяет, не является ли степень B нулем (тогда результат равен 1) 
и четным числом (тогда результат равен квадрату возведения числа A в степень B // 2). 
Если это не так, функция возвращает произведение числа A и результата возведения числа A в степень B - 1.
'''


def PowerRangers(A, B):
    if B == 0:
        return 1
    elif B % 2 == 0:
        return PowerRangers(A, B // 2) ** 2
    else:
        return A * PowerRangers(A, B - 1)


A = int(input("Enter A: "))
B = int(input("Enter B: "))
result = PowerRangers(A, B)
print(result)

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.


def sum41(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum41(a - 1, b + 1)


di1 = int(input("Enter first digit: "))
di2 = int(input("Enter second digit: "))
print(sum41(di1, di2))
