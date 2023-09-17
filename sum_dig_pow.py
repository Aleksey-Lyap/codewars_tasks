def sum_dig_pow(a, b):
    
    list = [str(i) for i in range(a, b+1)]

    result = []

    for number in list:
        count = 1
        sum_digit = 0
        for digit in number:
            sum_digit += int(digit)**count
            count += 1
        if int(number) == sum_digit:
            result.append(sum_digit)
        sum_digit = 0

    return result
