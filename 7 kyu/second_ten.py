def get_sum(a, b):
    """Sum all integers between a and b. Both included"""
    return sum(range(min(a, b), max(a, b) + 1))


def longest_distinct(firstword, secondword):
    """Return a string of unique letters from firstword and secondword"""
    return ''.join(sorted(list(set(firstword + secondword))))


def filterfriend(friends):
    """If friend's name contains exactly 4 letters so he is friend"""
    return [friend for friend in friends if len(friend) == 4]


def open_or_senior(members):
    """Return memebers statuses: Open or Senior"""
    def checkout_memeber(age, handicap):
        return 'Senior' if (age > 54 and handicap > 7) else 'Open'

    return [checkout_memeber(member[0], member[1]) for member in members]


def find_next_square(number):
    """Returns next square if number is a square of some int. Otherwise -1"""
    return (number ** 0.5 + 1) ** 2 if (number ** 0.5).is_integer() else -1