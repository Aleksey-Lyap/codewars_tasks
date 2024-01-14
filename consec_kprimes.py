def consec_kprimes(k, arr):
    """
    Функция возвращает сколько раз k-простые чисела
    (число, которое имеет ровно k простых делителей)
    встречаются дважды в массиве arr.
    """

    def prime_factorization(number):
        """Функция раскладывает чило на простые множетели"""
        factors = []
        divisor = 2
        while divisor <= number:
            if number % divisor == 0:
                factors.append(divisor)
                number //= divisor
            else:
                divisor += 1
        return factors
    
    prime_factors_arr = [prime_factorization(num) for num in arr]

    count = 0
    for i in range(len(arr) - 1):
        if len(prime_factors_arr[i]) == k and len(prime_factors_arr[i + 1]) == k:
            count += 1

    return count
