def numbers_of_letters(n):
    """Генерирует последовательность текстовых представлений чисел, начиная с заданного числа.

    Args:
        n (int): Исходное число.

    Returns:
        list: Список текстовых представлений чисел, в котором каждый элемент формируется
              путем преобразования предыдущего элемента в количество его символов, 
              пока не достигнется текстовое представление числа "four".
    """
    numbers_dict = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "0": "zero"
    }

    def get_text_representation(number):
        """Преобразует число в текстовое представление, используя словарь numbers_dict."""
        return ''.join(numbers_dict[digit] for digit in str(number))
    
    result = [get_text_representation(n)]
    
    while result[-1] != "four":
        result.append(get_text_representation(len(result[-1])))

    return result
