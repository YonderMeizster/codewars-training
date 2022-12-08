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


def is_onumber_equal_xnumber(string):
    """Returns True if the number of 'o' in the string is equal to the
    number of 'x'"""
    return sum([1 for letter in string.lower() if
        letter ==  'o']) == sum([1 for letter in string.lower() if
        letter ==  'x'])


def to_jaden_case(string : str):
    """Return inputed string but in Jaden case. Its better to see the
    result by yourself"""

    if len(string) == 0:
        return ''

    def make_first_letter_up(word):
        return word[0].upper() + ''.join([letter for letter in
            word[1:].lower()])

    return(' '.join([make_first_letter_up(procecced_word) for
        procecced_word in string.split()]))
    # After this I have got known about str.capitalize() method
    # return (' '.join([word.capitalize() for word in string.split()]))


def find_shortest_length(string):
    """Returns a length of the shortest word(s)"""
    return min([len(word) for word in string.split()])


def maskify(string):
    """Returns a string in which all symbols besides last 4 are
    masked"""
    return '#' * (len(string) - 4) +  string[-4:]


def sum_two_smallest_numbers(numbers):
    """Returns sum of 2 smallest numbers in numbers"""
    numbers.sort()
    return numbers[0] + numbers[1]
