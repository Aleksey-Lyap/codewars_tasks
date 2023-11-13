def is_prime_number (number):
    '''Проверяет, является ли число простым.'''
    if number == 0 or number == 1:
        return False
    if number == 2:
        return True
    for i in range (2,number):
        if number % i == 0:
            return False
    return True

def have_prime_digit (number):
    '''Проверяет число на наличие простых цифр.'''
    number = str (number)
    if '2' in number or '3' in number or '5' in number or '7' in number:
        return True
    return False

def solve(index):
    '''Ищет число n, по индексу.
    В массиве, в котором нет простых чисел и ни один из его элементов не имеет простых цифр.
    '''
    my_list = []
    num = 1
    while len(my_list) != (index+1):
        if have_prime_digit(num):
            num += 1
            continue
        if is_prime_number(num):
            num += 1
            continue
        my_list.append(num)
        num += 1
    return my_list[index]
