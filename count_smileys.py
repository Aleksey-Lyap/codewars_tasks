def count_smileys(arr):
    """
    Подсчитывает количество допустимых улыбок в заданном списке.

    :param arr: Список строк, представляющих улыбочные символы.
    :return: Количество допустимых улыбок в списке.
    """
    symbols = {
        "eyes": [':', ';'],
        "nose": ['-', '~'],
        "mouth": [')', 'D']
    }
 
    def acceptable_smile(smile):
        if len(smile) == 2:
            return smile[0] in symbols['eyes'] and smile[1] in symbols['mouth']
        elif len(smile) == 3:
            return all(part in part_type for part, part_type in zip(smile, symbols.values()))
        else:
            return False
        
    return sum(1 for smile in arr if acceptable_smile(smile))
