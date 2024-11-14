from mpmath.libmp import isprime
"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    [1, 4, 25, 49]
    """
    result = []
    for i in args:
        result.append(i ** 2)
    return result


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def my_is_prime(number):
    if isprime(number):
        return number

def filter_numbers(list_numbers, type_filter):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    [2, 4]
    """
    if type_filter == EVEN:
        return list(filter(lambda i: i % 2 == 0, list_numbers))
    elif type_filter == ODD:
        return list(filter(lambda i: i % 2 != 0, list_numbers))
    elif type_filter == PRIME:
        return list(filter(my_is_prime, list_numbers))