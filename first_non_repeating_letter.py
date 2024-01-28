def first_non_repeating_letter(s):
    """
    Находит и возвращает первый неповторяющийся символ в строке.

    Параметры:
    - s (str): Входная строка.

    Возвращает:
    - str: Первый неповторяющийся символ, если таковой есть. В противном случае возвращает пустую строку ('').

    Пример использования:
    >>> first_non_repeating_letter("stress")
    't'
    """
    s_lower = s.lower()
    for index, letter in enumerate(s_lower):
        if s_lower.count(letter) == 1:
            return s[index]
    return ''
