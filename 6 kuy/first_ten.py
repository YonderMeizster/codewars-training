def sum_divisible_by_5_or_3(number):
    """Returns sum of all natural numbers divisible by 5 or 3 below number"""
    return sum([i for i in range(number) if i % 5 == 0 or i % 3 ==0])


def find_repeated_odd_number(numbers):
    """Returns a number that is repeated odd time in numbers"""
    number = numbers[0] # numbers always has at least one element

    for i in numbers:
        if numbers.count(i) % 2 != 0:
            return i
    

def spin_words(sentence):
    """Reverse all 5+ words in sentece and return it"""
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])


def digital_root(number):
    """Return digital_root of number"""
    processed_number = sum([int(i) for i in str(number)])
    
    if processed_number > 9:
        return digital_root(processed_number)
    else:
        return processed_number


def likes(names):
    """Returns the string wich shows who liked"""
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1: 
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this' 
