"""Task 11
Написати код для дзеркального перевороту списку [7,2,9,4] -> [4,9,2,7].
Список може бути довільною довжиною."""
import random
a = int(input('введи длину списка: '))
x = [random.randint(1, 100) for i in range(a)]
print(x)
#можно отзеркалить и при этом создать новый список
y = x[::-1]
print(y)
#можно изменить текущий
x.reverse()
print(x)

