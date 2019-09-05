# Necessary classes. Use like this: "from classes import Integer".

from util import char_to_number
from util import number_to_char

class Integer:
    """
    Class used to store massive integers. This gets passed to arithmetic
    algorithms.

    Example:
        i = Integer('6A', 16, False)
        i.digits   -> [6, 10]
        i.base     -> 16
        i.positive -> False
    """
    def __init__(self, digits, base = 10, positive = True):
        """
        Arguments:
            digits:
                A list of numbers - they should all be lower than the base.
                The most significant numbers are at the beginning of this list.
                A string can be used as well, e.g. "13AF".
            base:
                Base of the number. Decimal by default.
            positive:
                True if the number has a positive sign, False if negative.
                Positive by default.

        Examples:
            Integer([1, 0, 14, 2], 16)  -> +10E2   (base 16)
            Integer('100101', 2, False) -> -100101 (base 2)
            Integer([1, 2, 3])          -> +123    (base 10)
        """

        if base > 16:
            raise ValueError(f'Base is {base}. Bases beyond 16 are not supported.')

        if base < 1:
            raise ValueError(f'Base is {base}. Base must be positive.')

        if len(digits) == 0:
            raise ValueError('Digit list cannot be empty.')

        # Sanity checks when digits are given as a list.
        if type(digits) is list:
            for digit in digits:
                if digit >= base:
                    raise ValueError(f'Digit {digit} is not allowed in base {base}.')

                if (digit < 0):
                    raise ValueError(f'Digit {digit} may not be negative.')

        # Sanity checks when digits are given as a string.
        # Also transforms string into its list representation.
        if type(digits) is str:
            new_digits = []

            for digit in digits:
                num = char_to_number(digit)
                if num >= base:
                    raise ValueError(f'Digit {digit} is not allowed in base {base}.')
                new_digits.append(num)

            digits = new_digits

        self.digits = digits
        self.base = base
        self.positive = positive

        # We could remove leading zeroes here using self.strip(), but for
        # assignment 1 that shouldn't be neccesary.

    def __str__(self):
        """
        Represent integer as a string. The base is not given, and a minus sign
        is added if negative. This is the same as notation found in input.

        Examples:
            str(Integer('6A', 16, False)) -> -6A
        """
        return ('' if self.positive else '-') + f'{self.get_digit_string()}'

    def __repr__(self):
        """
        Represent as string, but with more information. Useful for debugging.
        The digit list is always printed, along with the sign and base.

        Examples:
            repr(Integer('6A', 16, False)) -> -[6, 10] (base 16)
        """
        return ('+' if self.positive else '-') + f'{self.digits} (base {self.base})'

    def pad(self, size):
        """
        Add leading zeroes to the digit list to ensure it becomes a certain size.
        Returns a new copy of the Integer, so that the original one isn't modified.

        Example:
            i = Integer([1])
            i = i.pad(4)
            i.digits -> [0, 0, 0, 1]
        """
        original_size = len(self.digits)

        if size < original_size:
            raise ValueError(f'New size {size} is below original size {original_size}')

        new_int = self.copy()
        new_int.digits = [0] * (size - original_size) + new_int.digits
        return new_int

    def strip(self):
        """
        Remove trailing zeroes from the digit list. Undoes Integer.pad().
        Also called in the constructor.
        """
        new_int = self.copy()
        while new_int.digits[0] == 0 and len(new_int.digits) > 1:
            new_int.digits = new_int.digits[1:]
        return new_int

    def get_digit_string(self):
        """
        Returns this integers digits as a string, not a list. It converts digits
        above 9 to the hexadecimal counterparts.
        """
        s = ''
        for digit in self.digits:
            s = s + number_to_char(digit)
        return s

    def copy(self):
        """
        Returns a distinct copy of itself. Used in Integer.pad().
        """
        digits_copy = self.digits.copy()
        return Integer(digits_copy, self.base, self.positive)
