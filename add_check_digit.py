def add_check_digit(number):
    """Функция предназначена для добавления контрольной цифры к числу."""
    count = 2
    sum_digit = 0
    for item in number[::-1]:
        sum_digit += int(item)*count
        count += 1
        if count > 7:
            count = 2

    check_digit = (11 - sum_digit % 11)%11
    return number + 'X' if check_digit == 10 else number + str(check_digit)
