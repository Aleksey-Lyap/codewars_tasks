from functools import reduce

def lowest_product(num):
    if len(num) < 4:
        return "Number is too small"
    
    int_num = list(map(int, num))

    subset = [int_num[i:i+4] for i in range(len(int_num)-3)]

    return min(reduce(lambda x, y: x * y, item) for item in subset)
