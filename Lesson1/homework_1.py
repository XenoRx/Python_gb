import math
# Задача 2: Найдите сумму цифр трехзначного числа.
'''

n = int(input('Enter 3-digit number: '))

a = n // 100
b = (n // 10) % 10
c = n % 10

sum_of_digits = a + b + c
print(f'sum of {n} equals {sum_of_digits}')
'''
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# Calculate the number of cranes each child made
'''
S = int(input("Enter the total number of cranes: "))
Petr_Serega = S // 3
katya = 2 * Petr_Serega

print("Petr and Serega made {} cranes.".format(Petr_Serega))
print("Katya made {} cranes.".format(katya))
'''
# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
'''
ticket_number = input('Please enter a 6-digit ticket number: ')

# Convert the ticket number to a string
ticket_number_str = str(ticket_number)

# Check if the ticket number is 6 digits long
if len(ticket_number_str) != 6:
    print('The ticket number must be 6 digits long.')

# Calculate the sum of the first three digits
first_three_sum = int(
    ticket_number_str[0]) + int(ticket_number_str[1]) + int(ticket_number_str[2])

# Calculate the sum of the last three digits
last_three_sum = int(
    ticket_number_str[3]) + int(ticket_number_str[4]) + int(ticket_number_str[5])

if first_three_sum == last_three_sum:
    print('The ticket is lucky!')
else:
    print('The ticket is not lucky.')
'''
# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
'''
# size of the chocolate bar
n = input("Enter N: ")
m = input("Enter M: ")
n = int(n)
m = int(m)
# number of slices
k = input("Enter K: ")
k = int(k)
# calculate the area of the chocolate bar
area = n * m

# calculate the area of each slice
slice_area = area / k

# check if the area of each slice is a perfect square
if math.sqrt(slice_area).is_integer():
    print("It IS possible to break off {} slices from the chocolate bar".format(k))
else:
    print("It is NOT possible to break off {} slices from the chocolate bar".format(k))
'''


def is_possible(n, m, k):
    if k > n*m:
        return False
    if (k % n == 0 or k % m == 0):
        return True
    return False


# :D
n = input("Enter N : ")
n = int(n)
m = input("Enter M : ")
m = int(m)
k = input("Enter number of slices : ")
k = int(k)

if (is_possible(n, m, k)):
    print("Possible to break off {} slices from chocolate bar".format(k))
else:
    print("It is NOT possible to break off {} slices from chocolate bar".format(k))
