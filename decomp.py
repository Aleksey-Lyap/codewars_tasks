def decomp(n):
    """Функция раскладыает факториал(n!) на простые множетели"""

    def is_prime(number):
        """Функция проверяет является ли число n простым"""

        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True
    
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

    factor_prime_numbers = {}
    decomp_factorial = [i for i in range(2,n+1)]
    for item in decomp_factorial:
        if is_prime(item):
            factor_prime_numbers[item] = 1
        else:
            for i in prime_factorization(item):
                if i not in factor_prime_numbers:
                    factor_prime_numbers[i] = 1
                else:
                    factor_prime_numbers[i] += 1
    
    return " * ".join([
        "{}^{}".format(prime, power) if power > 1 else str(prime)
        for prime, power in factor_prime_numbers.items()
    ])
