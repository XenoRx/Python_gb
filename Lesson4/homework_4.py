# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 списка. 1 строка - первый список через пробел. 2 строка - второй список через пробел.

a = list(map(int, input("Enter 1st list, each element separated by a space: ").split()))
b = list(map(int, input("Enter 2nd list, each element separated by a space: ").split()))
outputText = "=================Output=================="
# создание множества из первого списка для проверки наличия элементов во втором списке
set_a = set(a)
result = []  # общий пул элементов

for num in b:  # перебор элементов второго списка
    if num in set_a:
        # если встречаем элемент в обоих списках = добавляем
        result.append(num)

result = list(set(result))  # убираем повторы

result.sort()  # asc sort
print(outputText)
for num in result:
    print(num, end=' ')

# Задача 24: TLDR

a = list(map(int, input("Enter the number of berries on the bushes: ").split()))
outputText = "Max berries collected in 1 run: "
n = len(a)  # количество кустов на грядке

max_berries = 0

for i in range(n):
    # суммирование ягод с текущего куста и двух соседних
    berries = a[i] + a[(i-1) % n] + a[(i+1) % n]
    if berries > max_berries:
        max_berries = berries

print(outputText, max_berries)
