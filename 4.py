"""Task 4
Напишіть скрипт, який обчислює за допомогою циклу факторіал числа n (n вводиться з клавіатури)."""
n = int(input('n = '))
res = 1
if n < 0:
    res = 'введи положительное число'

elif n == 1 or not n:
    res = 1

elif n > 1:
    i = 1
    while i <= n:
        res *= i
        i += 1
print(res)