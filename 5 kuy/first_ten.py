def move_zeros(lst):
    """Return copy of lst in which all zeros moved to end with saving
    other numbers order"""
    without_zeros = [number for number in lst if number != 0]
    return without_zeros + [0] * (len(lst) - len(without_zeros))


def pig_it(text):
    """Return pigged text. First symbol of each word moves to end and
    word concatenates with 'ay'."""
    splited_text = text.split()

    def transform_word(word):
        word = word[1:] + word[0] + 'ay'
        return word

    # If the incoming line of punctuation is not separated by spaces
    # from the words, there is a problem. A check in the generator will
    # return such a word unchanged. I have an idea how to solve this
    # problem, but if you do it, do it well. So to handle erroneous
    # punctuation, such as "word,,," you will have to fill the code
    # with additional functions with a loop and a check,
    # calculating the indexes of the beginning and end of the word in a
    # sequence of characters. This looks really bad and you should use
    # regular expressions for that, in my opinion. So far I haven't
    # dealt with Python regular expressions and sticking to Paretto
    # theory, I'll move on in my learning.

    return ' '.join([transform_word(word) if word.isalpha() else word for
        word in splited_text])


def valid_parentheses(expression):
    """Return true if parentheses are correct in expression"""    
    parentheses = 0

    for symbol in expression:
        if symbol == '(':
            parentheses += 1
        elif symbol == ')':
            if parentheses > 0:
                parentheses += 1
            else:
                return False

    return parentheses == 0


def readable_time(seconds):
    """Return HH:MM:SS time from seconds"""
    hours = seconds // 3600
    minutes = seconds // 60 % 60
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds % 60)


def hexrgb(r, g, b):
    """Return hexadecimal form of RGB"""

    def limit(level):
        if level > 255:
            return 255
        elif level < 0:
            return 0
        else:
            return level

    return '{:02X}{:02X}{:02X}'.format(limit(r), 
    limit(g), limit(b))


def rot13(message):
    """Return an encrypted message with the ROT13 cipher"""
    letters = 'abcdefghijklmnopqrstuvwxyz'

    def make_letter(symbol):
        if symbol.islower():
            return letters[(letters.find(symbol) + 13) % 26]
        else:
            return letters[(letters.find(symbol.lower()) + 13) % 26].upper()

    return ''.join(make_letter(letter) if letter.isalpha() else letter for
        letter in message)


def max_sequence(array):
    """Find first subarray with max sum of elements.

    Returns [subsequence, sum of subsequences elements, start index and end index]
    
    Returns 0 if array consist only of negative integers or empty"""
    if len(array) == 0:
        return 0
    if max(array) < 0:
        return 0

    start = end = 0
    max_sum_start = max_sum_end = start

    current_sum = max_sum = array[start]

    while end < len(array):
        current_sum += array[end]

        if current_sum < 0:
            current_sum = 0
            start = end + 1
            end = start
        elif current_sum > max_sum:
            max_sum = current_sum
            max_sum_start = start
            max_sum_end = end
            end += 1
        else:
            end += 1

    founded_array = array[max_sum_start : max_sum_end + 1]

    return [founded_array, max_sum, max_sum_start, max_sum_end]
