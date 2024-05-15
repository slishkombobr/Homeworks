result = ''

n = int(input('Введите число от 3 до 20: '))

for x in range(1, 21):
    for y in range(1, 21):
        if n % (x + y) == 0 and (x + y) <= n and x < y:
            result += str(x) + str(y)


print(n, '-', result)
