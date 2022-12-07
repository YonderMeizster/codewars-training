def get_count(sentence):
    """Returns number of vowels in sentence. Without 'y'"""
    return len([x for x in sentence if x in 'aeiouAEIOU'])


def is_isogram(string):
    """Returns True if string is isogram and False if is not"""
    return len(set(string.lower())) == len(string.lower())


def filter_list(l):
    """Returns list of int from list l"""
    return [i for i in l if isinstance(i, int)]


def is_square(n):
    """Returns True if n is a square number of some int"""
    return n >= 0 and n ** 0.5 % 1 == 0


def accum2(s):
    """Returns a little bit modified s"""
    return '-'.join([letter.upper() + letter.lower() * index for index, 
        letter in enumerate(s)])
