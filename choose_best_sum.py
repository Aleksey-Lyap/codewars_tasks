from itertools import combinations 

def choose_best_sum(t, k, ls):
    
    list_combinations = [x for x in combinations(ls, k) if sum(x) <= t]

    if not list_combinations:
        return None

    return sum(max(list_combinations, key=lambda x: sum(x)))
