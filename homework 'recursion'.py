# "Функции и произвольное число параметров"

def test(*args):
    print(args)

test('Hello, Python!', "I'm", 28, 'years old', "It's", True )

print()

# Рекурсия

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))