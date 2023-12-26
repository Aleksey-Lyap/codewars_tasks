from itertools import permutations


def late_clock(a, b, c, d):
    '''Функция возвращает крайнее(позднее) время и заданых цыфр a,b,c,d.'''
    all_permutations = permutations([a, b, c, d])
    time_result = '00:00'

    for item in all_permutations:
        hour = item[0]*10 + item[1]
        minutes = item[2]*10 + item[3]

        if (0 <= hour <= 23) and 0 <= minutes <= 59:
            current_time = f"{hour:02d}:{minutes:02d}"
            time_result = max(time_result, current_time)

    return time_result
