# For general purpose functions that might be useful. Actual algorithms
# should go in seperate files.

def char_to_number(character):
    """
    """
    character = character.upper()
    index = '0123456789ABCDEF'.find(character)

    if index == -1:
        raise ValueError('Character must be hexadecimal notation.')

    return index

def number_to_char(number):
    """
    """
    return '0123456789ABCDEF'[number] # ;)
