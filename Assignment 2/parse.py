import sys # used for input/output
import re  # used for removing whitespace
import poly
import field
import pdb

# helper method
def string_to_poly(argument):
    """Convert a string to a coefficient list."""
    # remove '{' and '}' at ends of the string
    without_brackets = argument[1:-1]
    # split into pieces where commas are encountered
    split = without_brackets.split(',')
    # convert strings in the list to numbers and return
    return list(map(int, split))

# parsed variables
mod = None
f   = None
g   = None
h   = None
deg = None
mod_poly = None
method   = None

# start reading from stdin. the contents of a file can be piped into the
# program, and the output can be piped into a file (see report)
for line in sys.stdin:
    if line == '\n' or line == '\r\n':
        # if the line is empty and no method was given, echo the line
        if method == None:
            sys.stdout.write(line)
        # otherwise, perform the method and write the answers to output
        elif method == 'display-poly':
            answer = poly.display_poly(mod, f)
            sys.stdout.write(f'[answer] {answer}\n')

        elif method == 'add-poly':
            answer = poly.add_poly(mod, f, g)
            answer = poly.display_poly(mod, answer)
            sys.stdout.write(f'[answer] {answer}\n')

        elif method == 'subtract-poly':
            answer = poly.subtract_poly(mod, f, g)
            answer = poly.display_poly(mod, answer)
            sys.stdout.write(f'[answer] {answer}\n')

        elif method == 'multiply-poly':
            answer = poly.multiply_poly(mod, f, g)
            answer = poly.display_poly(mod, answer)
            sys.stdout.write(f'[answer] {answer}\n')

        elif method == 'long-div-poly':
            q, r = poly.long_div_poly(mod, f, g)
            q = poly.display_poly(mod, q)
            r = poly.display_poly(mod, r)
            sys.stdout.write(f'[answ-q] {q}\n')
            sys.stdout.write(f'[answ-r] {r}\n')

        elif method == 'euclid-poly':
            a, b, d = poly.euclid_poly(mod, f, g)
            a = poly.display_poly(mod, a)
            b = poly.display_poly(mod, b)
            d = poly.display_poly(mod, d)
            sys.stdout.write(f'[answ-a] {a}\n')
            sys.stdout.write(f'[answ-b] {b}\n')
            sys.stdout.write(f'[answ-d] {d}\n')

        elif method == 'equals-poly-mod':
            answer = poly.equals_poly_mod(mod, f, g, h)
            sys.stdout.write(f'[answer] {answer}\n')

        elif method == 'irreducible':
            answer = poly.irreducible(mod, f)
            sys.stdout.write(f'[answer] {answer}\n')

        elif method == 'find-irred':
            answer = poly.find_irred(mod, deg)
            answer = poly.display_poly(mod, answer)
            sys.stdout.write(f'[answer] {answer}\n')

        elif method == 'add-table':
            pass # placeholder

        elif method == 'mult-table':
            pass # placeholder

        elif method == 'display-field':
            pass # placeholder

        elif method == 'add-field':
            pass # placeholder

        elif method == 'subtract-field':
            pass # placeholder

        elif method == 'multiply-field':
            pass # placeholder

        elif method == 'inverse-field':
            pass # placeholder

        elif method == 'division-field':
            pass # placeholder

        elif method == 'equals-field':
            pass # placeholder

        elif method == 'primitive':
            pass # placeholder

        elif method == 'find-prim':
            pass # placeholder

        # reset the method variable when we're done to avoid duplicate answers
        method = None

        # stop processing the line
        continue

    # if the line contains a comment, echo it
    if line[0] == '#':
        sys.stdout.write(line)

    # the line must be a command!
    # we can ignore whitespace, so remove it
    stripped = re.sub('\s', '', line)

    # find the command name, and argument
    bracket  = stripped.find(']')
    command  = stripped[1:bracket]     # line from '[' to ']'
    argument = stripped[bracket + 1:] # line after ']'

    # set variables based on the command
    if command == 'mod':
        mod = int(argument)
        sys.stdout.write(line) # still echo the command for inspection
    elif command == 'f':
        f = string_to_poly(argument)
        sys.stdout.write(line)
    elif command == 'g':
        g = string_to_poly(argument)
        sys.stdout.write(line)
    elif command == 'h':
        h = string_to_poly(argument)
        sys.stdout.write(line)
    elif command == 'deg':
        deg = int(argument)
        sys.stdout.write(line)
    elif command == 'mod-poly':
        mod_poly = string_to_poly(argument)
        sys.stdout.write(line)

    # no argument is given, so the command tells us what method to execute
    elif argument == '':
        method = command
        sys.stdout.write(line)

    # output commands like [answer] are automatically ignored
