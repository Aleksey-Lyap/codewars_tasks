def increment_string(strng):
    body = strng.rstrip('0123456789') 
    tail = strng[len(body):]
    if tail == '': return strng + '1'
    return body + str(int(tail) + 1).zfill(len(tail))
