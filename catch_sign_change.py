def catch_sign_change(lst):
    """
    Подсчитывает количество изменений знака в списке чисел.

    Аргументы:
    lst (list): Список чисел.

    Возвращает:
    int: Количество изменений знака в списке.

    Пример использования:
    >>> numbers = [1, -2, 3, 0, -4, 5]
    >>> catch_sign_change(numbers)
    4
    """
    return  sum((value >= 0) != (next_value >=0) for value, next_value in zip(lst, lst[1:]))