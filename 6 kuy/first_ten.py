def sum_divisible_by_5_or_3(number):
    """Return sum of all natural numbers divisible by 5 or 3 below number"""
    return sum([i for i in range(number) if i % 5 == 0 or i % 3 == 0])


def find_repeated_odd_number(numbers):
    """Return a number that is repeated odd time in numbers"""
    number = numbers[0]  # numbers always has at least one element

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
    """Return the string wich shows who liked"""
    if len(names) == 0:
        return 'no one likes this'
    if len(names) == 1:
        return f'{names[0]} likes this'
    if len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    if len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


def find_outlier(integers) -> int:
    """Return an integer which differs from the others in evenness
    or oddness"""
    result = None
    for i in range(1, len(integers) - 1):
        if integers[i] % 2 == integers[i - 1] % 2 == integers[i + 1] % 2:
            continue
        first = integers[i - 1]
        second = integers[i]
        third = integers[i + 1]
        break
    if first % 2 == third % 2:
        return second
    if first % 2 == second % 2:
        return third
    return first



print(find_outlier([2, 4, 6, 8, 10, 3]))