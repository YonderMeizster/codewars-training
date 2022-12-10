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