"""Task 13
Виведіть на екран «пісочний годинник», максимальна ширина якого зчитується з клавіатури (число непарне). /
У прикладі ширина дорівнює 5.
*****
 ***
  *
 ***
*****"""
x = int(input('введи целое непарное число: '))
if x % 2:
    y = x
    a = 1
    b = 1
    while x >= a:
        print(x * '*')
        x -= 2

    while b < y:
        print((b + 1) * '*')
        b += 2
else:
    print('введи непарное число')