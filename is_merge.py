def is_merge(s, part1, part2):
    """Вам предстоит написать алгоритм, проверяющий, может ли данная строка,
       s быть сформирована из двух других строк, part1и part2.
       Ограничение состоит в том, что символы в part1и part2 должны располагаться в том же порядке, что и в s.
    """
    if not part1:
        return s == part2
    if not part2:
        return s ==part1
    if not s:
        return part1 + part2 == ''
    if s[0] == part1[0] and is_merge(s[1:],part1[1:],part2):
        return True
    if s[0] == part2[0] and is_merge(s[1:],part1,part2[1:]):
        return True
    return False
