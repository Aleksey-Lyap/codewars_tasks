def good_vs_evil(good, evil):

    vim_good = [1, 2, 3, 3, 4, 10]
    vim_evil = [1, 2, 2, 2, 3, 5, 10]

    forces_good = sum([x*int(y) for x, y in zip(vim_good, good.split())])
    forces_evil = sum([x*int(y) for x, y in zip(vim_evil, evil.split())])

    if forces_good > forces_evil:
        return "Battle Result: Good triumphs over Evil"
    elif forces_good < forces_evil:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"
