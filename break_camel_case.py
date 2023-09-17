def solution(string):
    
    return ''.join(' ' + i if i.isupper() else i for i in string)
