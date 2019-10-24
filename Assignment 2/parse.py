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
    output = sys.stdout

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
    command  = stripped[1:bracket]    # line from '[' to ']'
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
        a = string_to_poly(argument)
        output.write(line)

    elif command == 'b':
        b = string_to_poly(argument)
        output.write(line)

    # output commands like [answer] are automatically ignored
    if method == 'display-poly' and mod and not f == None:
        answer = poly.display_poly(mod, f)
        output.write(f'[answer]\t{answer}\n')
        mod = None
        f   = None
        method = None

    elif method == 'add-poly' and mod and not f == None and not g == None:
        answer = poly.add_poly(mod, f, g)
        answer = poly.display_poly(mod, answer)
        output.write(f'[answer]\t{answer}\n')
        mod = None
        f   = None
        g   = None
        method = None

    elif method == 'subtract-poly' and mod and not f == None and not g == None:
        answer = poly.subtract_poly(mod, f, g)
        answer = poly.display_poly(mod, answer)
        output.write(f'[answer]\t{answer}\n')
        mod = None
        f   = None
        g   = None
        method = None

    elif method == 'multiply-poly' and mod and not f == None and not g == None:
        answer = poly.multiply_poly(mod, f, g)
        answer = poly.display_poly(mod, answer)
        output.write(f'[answer]\t{answer}\n')
        mod = None
        f   = None
        g   = None
        method = None

    elif method == 'long-div-poly' and mod and not f == None and not g == None:
        #pdb.set_trace()
        q, r = poly.long_div_poly(mod, f, g)
        if q != 'ERROR': q = poly.display_poly(mod, q)
        if r != 'ERROR': r = poly.display_poly(mod, r)
        output.write(f'[answ-q]\t{q}\n')
        output.write(f'[answ-r]\t{r}\n')
        mod = None
        f   = None
        g   = None
        method = None

    elif method == 'euclid-poly' and mod and not f == None and not g == None:
        answer = poly.euclid_poly(mod, f, g)
        if answer == "ERROR":
            output.write('[answer]\tERROR\n')
        else:
            answ_a, answ_b, answ_d = answer
            answ_a = poly.display_poly(mod, answ_a)
            answ_b = poly.display_poly(mod, answ_b)
            answ_d = poly.display_poly(mod, answ_d)
            output.write(f'[answ-a]\t{answ_a}\n')
            output.write(f'[answ-b]\t{answ_b}\n')
            output.write(f'[answ-d]\t{answ_d}\n')
        mod = None
        f   = None
        g   = None
        method = None

    elif method == 'equals-poly-mod' and mod and not f == None and not g == None and not h == None:
        if poly.equals_poly_mod(mod, f, g, h):
            output.write(f'[answer]\tTRUE\n')
        else:
            output.write(f'[answer]\tFALSE\n')
        mod = None
        f   = None
        g   = None
        h   = None
        method = None

    elif method == 'irreducible' and mod and not f == None:
        if poly.irreducible(mod, f):
            output.write(f'[answer]\tTRUE\n')
        else:
            output.write(f'[answer]\tFALSE\n')
        mod = None
        f   = None
        method = None

    elif method == 'find-irred' and mod and deg:
        answer = poly.find_irred(mod, deg)
        answer = poly.display_poly(mod, answer)
        output.write(f'[answer]\t{answer}\n')
        mod = None
        deg = None
        method = None

    elif method == 'add-table' and mod and not mod_poly == None:
        answer = field.add_table(mod, mod_poly)
        output.write(f'[answer]\t{answer}\n')
        mod = None
        mod_poly = None
        method = None

    elif method == 'mult-table' and mod and not mod_poly == None:
        answer = field.mult_table(mod, mod_poly)
        output.write(f'[answer]\t{answer}\n')
        mod = None
        mod_poly = None
        method = None

    elif method == 'display-field' and mod and not mod_poly == None and not a == None:
        answer = field.display_field(mod, mod_poly, a)
        output.write(f'[answer]\t{answer}\n')
        mod = None
        mod_poly = None
        a = None
        method = None

    elif method == 'add-field' and mod and not mod_poly == None and not a == None and not b == None:
        answer = field.add_field(mod, mod_poly, a, b)
        if answer != 'ERROR': answer = field.display_field(mod, mod_poly, answer)
        output.write(f'[answer]\t{answer}\n')
        mod = None
        mod_poly = None
        a = None
        b = None
        method = None

    elif method == 'subtract-field' and mod and not mod_poly == None and not a == None and not b == None:
        answer = field.subtract_field(mod, mod_poly, a, b)
        if answer != 'ERROR': answer = field.display_field(mod, mod_poly, answer)
        output.write(f'[answer]\t{answer}\n')
        mod = None
        mod_poly = None
        a = None
        b = None
        method = None

    elif method == 'multiply-field' and mod and not mod_poly == None and not a == None and not b == None:
        answer = field.multiply_field(mod, mod_poly, a, b)
        if answer != 'ERROR': answer = field.display_field(mod, mod_poly, answer)
        output.write(f'[answer]\t{answer}\n')
        mod = None
        mod_poly = None
        a = None
        b = None
        method = None

    elif method == 'inverse-field' and mod and not mod_poly == None and not a == None:
        answer = field.inverse_field(mod, mod_poly, a)
        if answer != 'ERROR': answer = field.display_field(mod, mod_poly, answer)
        output.write(f'[answer]\t{answer}\n')
        mod = None
        mod_poly = None
        a = None
        method = None

    elif method == 'division-field' and mod and not mod_poly == None and not a == None and not b == None:
        answer = field.division_field(mod, mod_poly, a, b)
        if answer != 'ERROR': answer = field.display_field(mod, mod_poly, answer)
        output.write(f'[answer]\t{answer}\n')
        mod = None
        mod_poly = None
        a = None
        b = None
        method = None

    elif method == 'equals-field' and mod and not mod_poly == None and not a == None and not b == None:
        if field.equals_field(mod, mod_poly, a, b):
            output.write('[answer]\tTRUE\n')
        else:
            output.write('[answer]\tFALSE\n')
        mod = None
        mod_poly = None
        a = None
        b = None
        method = None

    elif method == 'primitive' and mod and not mod_poly == None and not a == None:
        if field.primitive(mod, mod_poly, a):
            output.write('[answer]\tTRUE\n')
        else:
            output.write('[answer]\tFALSE\n')
        mod = None
        mod_poly = None
        a = None
        method = None

    elif method == 'find-prim' and mod and not mod_poly == None:
        answer = field.find_prim(mod, mod_poly)
        if answer != 'ERROR': answer = field.display_field(mod, mod_poly, answer)
        output.write(f'[answer]\t{answer}\n')
        mod = None
        mod_poly = None
        method = None

    #print(f'LINE: {repr(line)}')
    #print(f'COMMAND: {repr(command)}')
    #print(f'ARGUMENT: {repr(argument)}')
    #print(f'METHOD: {repr(method)}')
    #print(f'MOD: {repr(mod)}')
    #print(f'MOD_POLY: {repr(mod_poly)}')
    #print(f'A: {repr(a)}')
    #print('')
