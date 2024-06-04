import math

def divide(first, second):

    try:
        first / second
    except ZeroDivisionError:
        return math.inf
    else:
        return first / second

