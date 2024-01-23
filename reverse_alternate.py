def reverse_alternate(st):
    """
    Инвертирует каждое второе слово в строке.

    Параметры:
    st (str): Исходная строка.

    Возвращает:
    str: Строка, в которой каждое второе слово инвертировано.

    Пример:
    >>> reverse_alternate('Hello World')
    'Hello dlroW'
    """
    return ' '.join(word[::-1] if index % 2 != 0 else word for index, word in enumerate(st.split()))
