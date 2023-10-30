def is_leap_year(year):
    '''В этом ката вам нужно просто определить, является ли данный год високосным или нет. Если вы не знаете правил, вот они:
    Годы, кратные 4, являются високосными,
    но годы, кратные 100, не являются високосными,
    но годы, делящиеся на 400, являются високосными.
    Годы испытаний находятся в пределах допустимого 1600 ≤ year ≤ 4000
    '''
    
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 
