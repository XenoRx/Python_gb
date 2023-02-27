# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
'''
# Define the number of coins to be flipped
coins = int(input("Enter number of coins to flip: "))

# Define the array with the initial coins orientation
orientation = [0, 1, 1, 1]

# Define the variable to store the minimum coins to flip
min_coins_flip = 0

# Iterate over the coins
for coin in range(coins):
    #Check if the coin needs to be flipped
    if orientation[coin] == 0:
        min_coins_flip += 1

# Print the solution
print("The minimum number of coins to be flipped is", min_coins_flip)
'''
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
'''
# Setting the upper limit
limit = 1000

# Taking input as Sum(S) and Product(P)
S = int(input('Enter the sum: '))
P = int(input('Enter the product: '))

# Solving using brute force
for x in range(1, limit + 1):
    for y in range(1, limit + 1):
        if x + y == S and x * y == P:
            print(x, y)
'''
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.

# Setting upper limit
N = int(input('Enter the limit N: '))

# Printing all integers of degree two
for number in range(1, N+1):
    if number & (number - 1) == 0:
        print(number)
