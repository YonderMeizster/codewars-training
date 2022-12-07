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
