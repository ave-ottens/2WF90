import re

from Integer import *
import algorithms

class Context():
    """
    """

    def __init__(self):
        self.reset()

    def reset(self):
        self.x = None
        self.y = None
        self.radix = None
        self.op = None

    def read_line(self, line):
        original_line = line
        line = re.sub('\s', '', line) # Remove all whitespace

        if len(line) == 0:
            if not self.op:
                return '\n'

            # Empty line, which means we should compute a result
            answer = self.op(self.x, self.y)
            op = self.op

            self.reset() # NOTE: neccesary?

            #if (op in (algorithms.add, algorithms.subtract)):
            #    return f'[answer] {answer}\n\n'

            return '[answer] ?\n\n'

        if line[0] == '#':
            # Line is a comment, just return it
            return original_line

        bracket_index = line.find(']')
        command = line[1:bracket_index]     # Extract text between brackets
        argument = line[bracket_index + 1:] # Extract argument after command

        if command == 'radix':
            self.radix = int(argument)

        elif command == 'x':
            self.x = Integer(argument, self.radix)

        elif command == 'y':
            self.y = Integer(argument, self.radix)

        elif command == 'add':
            self.op = algorithms.add

        elif command == 'subtract':
            self.op = algorithms.subtract

        elif command == 'multiply':
            self.op = algorithms.multiply

        elif command == 'karatsuba':
            self.op = algorithms.karatsuba

        elif command in ('answer', 'count-add', 'count-mul'):
            # Ignore and don't write to output
            return ''

        return original_line
