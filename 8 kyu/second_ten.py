def century(year):
    """Convert centuary from year"""
    return year // 100 + 1 if year % 100 != 0 else year // 100


def abbrev_name(name):
    """Converts name to initials"""
    return '.'.join([letter[0] for letter in name.upper().split()])


def litres(time):
    """Converts time in hours into rounded litres. 1 hour = 0.5 litres"""
    return time // 2


def is_divisible(n, x, y):
    """Checks if n is divisible by x AND y"""
    return n % x == 0 and n % y == 0


def list_and_reverse(number):
    """Returns a reversed list from number's digits"""
    return [int(digit) for digit in str(number)[::-1]]


def draw_stairs(steps):
    """Return a string looks like a stair-like art in console output"""
    return '\n'.join(['%*s' % (step + 1, 'I') for step in range(steps)])

