# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Введите число: "))
x = 2
stepen = 2
while stepen < N:
    print(stepen)
    stepen *= x