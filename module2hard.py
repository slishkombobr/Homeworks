n = int(input('Введите число от 3 до 20: '))

for i in range(1,21):
    for x in range(i):
        for y in range(i):
            if n % (x+y) == 0:
                print( n, 'это', i)
