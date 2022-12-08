def repeat_str(n, string):
    """Returns string repeated n times."""
    return string * n


def remove_char(s):
    """Removes the first and last characters of a string."""
    return s[1:-1]


def number_to_string(num):
    """Returns str of num."""
    return str(num)


def opposite(num):
    """Returns opposite of num"""
    return(num * -1)


def bool_to_word(boolean):
    """Returns 'Yes' for True and 'No' for False"""
    return 'Yes' if boolean == True else 'No'


def square_sum(numbers):
    """Returns sum of squares of numbers from iteratable numbers"""
    return sum([x ** 2 for x in numbers])


def summation(number):
    """Returns a sum of all pozitive numbers from one to number
    both included"""
    return sum([x for x in range(1, number + 1)])


def no_space(string : str):
    """Returns a string without spaces"""
    return ''.join(string.split(' '))


def find_smallest_int(numbers):
    """Returns the smallest int in numbers"""
    return min(numbers)


def count_sheeps(sheeps):
    """Returns True number in sheeps"""
    return sum(x for x in sheeps if x != None)
