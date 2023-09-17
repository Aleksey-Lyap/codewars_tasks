def alphabet_position(text):

    return ' '.join(str(ord(sumbul) - 96) for sumbul in text.lower() if sumbul.isalpha())
