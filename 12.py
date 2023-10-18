"""Task 12
За допомогою циклів вивести на екран усі прості числа від 1 до 100."""
for x in range(2, 100):
    number = True
    for y in range(2, ((x//2) + 1)):
        if not x % y:
            number = False
            break
    if number:
        print(x)

