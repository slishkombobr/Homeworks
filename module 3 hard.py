def calculate_structure_sum(data_structure):
    total_sum = 0 # начинаем считать с 0

    for i in data_structure: # начинаем перебирать всё из data_structure
        if isinstance(i, int):
            total_sum += i # просто складываем, если у нас числа
        elif isinstance(i, dict):
            for key, value in i.items():
                total_sum += len(str(key))  # складываем длину ключа
                total_sum += calculate_structure_sum([value])  # складываем длину значения ключа
        elif isinstance(i, str):
            total_sum += len(i) # просто складываем длину, если у нас строка
        elif isinstance(i, list):
            total_sum += calculate_structure_sum(i)
        elif isinstance(i, tuple):
            total_sum += calculate_structure_sum(i)
        elif isinstance(i, set):
            total_sum += calculate_structure_sum(i)
    return total_sum




data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

