import sys # used for input/output
import re  # used for removing whitespace
import poly
import field
import pdb

# read from a file if names are given on the command line
# if not given, read from terminal input and write to terminal output
# ( pipes are also possible )
if len(sys.argv) == 3:
    input  = open(sys.argv[1], 'r')
    output = open(sys.argv[2], 'w', encoding='utf-8')
else:
    input  = sys.stdin
    output = output

# parsed variables
mod = None
f   = None
g   = None
h   = None
deg = None
a   = None
b   = None
mod_poly = None
method   = None

def string_to_poly(argument):
    """Convert a string to a coefficient list."""
    if argument == '{}':
        return []
    # remove '{' and '}' at ends of the string
    without_brackets = argument[1:-1]
    # split into pieces where commas are encountered
    split = without_brackets.split(',')
    # convert strings in the list to numbers and return
    return list(map(int, split))

# start reading from stdin. the contents of a file can be piped into the
# program, and the output can be piped into a file (see report)
for line in input:
    # standardize line ends: Windows tends to be inconsistent
    line = re.sub('\r\n', '\n', line)

    # if the line is empty, echo the line
    if line == '\n':
        output.write(line)
        continue # stop processing this line

    # if the line contains a comment, echo it
    if line[0] == '#':
        output.write(line)
        continue

    # the line must be a command!
    # we can ignore whitespace, so remove it
    stripped = re.sub('\s', '', line)

    # find the command name, and argument
    bracket  = stripped.find(']')
    command  = stripped[1:bracket]     # line from '[' to ']'
    argument = stripped[bracket + 1:] # line after ']'

    # no argument is given, so the command tells us what method to execute
    if argument == '':
        method = command
        output.write(line)

    # set variables based on the command
    elif command == 'mod':
        mod = int(argument)
        output.write(line) # still echo the command for inspection

    elif command == 'f':
        f = string_to_poly(argument)
        output.write(line)

    elif command == 'g':
        g = string_to_poly(argument)
        output.write(line)

    elif command == 'h':
        h = string_to_poly(argument)
        output.write(line)

    elif command == 'deg':
        deg = int(argument)
        output.write(line)

    elif command == 'mod-poly':
        mod_poly = string_to_poly(argument)
        output.write(line)

    elif command == 'a':
        a = None # placeholder
        output.write(line)

    elif command == 'b':
        b = None # placeholder
        output.write(line)

    # output commands like [answer] are automatically ignored
    if method == 'display-poly' and mod and not f == None:
        answer = poly.display_poly(mod, f)
        output.write(f'[answer] {answer}\n')
        mod = None
        f   = None

    elif method == 'add-poly' and mod and not f == None and not g == None:
        answer = poly.add_poly(mod, f, g)
        answer = poly.display_poly(mod, answer)
        output.write(f'[answer] {answer}\n')
        mod = None
        f   = None
        g   = None

    elif method == 'subtract-poly' and mod and not f == None and not g == None:
        answer = poly.subtract_poly(mod, f, g)
        answer = poly.display_poly(mod, answer)
        output.write(f'[answer] {answer}\n')
        mod = None
        f   = None
        g   = None

    elif method == 'multiply-poly' and mod and not f == None and not g == None:
        answer = poly.multiply_poly(mod, f, g)
        answer = poly.display_poly(mod, answer)
        output.write(f'[answer] {answer}\n')
        mod = None
        f   = None
        g   = None

    elif method == 'long-div-poly' and mod and not f == None and not g == None:
        q, r = poly.long_div_poly(mod, f, g)
        q = poly.display_poly(mod, q)
        r = poly.display_poly(mod, r)
        output.write(f'[answ-q] {q}\n')
        output.write(f'[answ-r] {r}\n')
        mod = None
        f   = None
        g   = None

    elif method == 'euclid-poly' and mod and not f == None and not g == None:
        a, b, d = poly.euclid_poly(mod, f, g)
        a = poly.display_poly(mod, a)
        b = poly.display_poly(mod, b)
        d = poly.display_poly(mod, d)
        output.write(f'[answ-a] {a}\n')
        output.write(f'[answ-b] {b}\n')
        output.write(f'[answ-d] {d}\n')
        mod = None
        f   = None
        g   = None

    elif method == 'equals-poly-mod' and mod and not f == None and not g == None and not h == None:
        answer = poly.equals_poly_mod(mod, f, g, h)
        output.write(f'[answer] {answer}\n')
        mod = None
        f   = None
        g   = None
        h   = None

    elif method == 'irreducible' and mod and not f == None:
        answer = poly.irreducible(mod, f)
        output.write(f'[answer] {answer}\n')
        mod = None
        f   = None

    elif method == 'find-irred' and mod and deg:
        answer = poly.find_irred(mod, deg)
        answer = poly.display_poly(mod, answer)
        output.write(f'[answer] {answer}\n')
        mod = None
        deg = None

    elif method == 'add-table' and mod and not mod_poly == None:
        pass # placeholder

    elif method == 'mult-table' and mod and not mod_poly == None:
        pass # placeholder

    elif method == 'display-field' and mod and not mod_poly == None and not a == None:
        pass # placeholder

    elif method == 'add-field' and mod and not mod_poly == None and not a == None and not b == None:
        pass # placeholder

    elif method == 'subtract-field' and mod and not mod_poly == None and not a == None and not b == None:
        pass # placeholder

    elif method == 'multiply-field' and mod and not mod_poly == None and not a == None and not b == None:
        pass # placeholder

    elif method == 'inverse-field' and mod and not mod_poly == None and not a == None:
        pass # placeholder

    elif method == 'division-field' and mod and not mod_poly == None and not a == None and not b == None:
        pass # placeholder

    elif method == 'equals-field' and mod and not mod_poly == None and not a == None and not b == None:
        pass # placeholder

    elif method == 'primitive' and mod and not mod_poly == None and not a == None:
        pass # placeholder

    elif method == 'find-prim' and mod and not mod_poly == None:
        pass # placeholder
