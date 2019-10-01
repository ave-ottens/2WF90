import pdb # break into the debugger with pdb.set_trace()

def display_poly(mod, f):
    terms = [] # list of strings to be concatenated later

    for c, i in zip(f, range(len(f) - 1, -1, -1)):
        # c is the coefficient
        # i is the power of X that the coefficient relates to

        # normalize c such that 0 <= c < mod
        c = c % mod

        # we ignore the coefficient if it is zero
        if c > 0:
            if i > 1:
                terms.append(f'{c}X^{i}')
            elif i == 1:
                terms.append(f'{c}X')
            else:
                terms.append(str(c))

    # return terms with '+' symbols inbetween
    return '+'.join(terms)

def add_poly(mod, f, g):
    return # list of coefficients, highest degree first

def subtract_poly(mod, f, g):
    return # list of coefficients, highest degree first

def multiply_poly(mod, f, g):
    return # list of coefficients, highest degree first

def long_div_poly(mod, f, g):
    q = None
    r = None
    return (q, r)

def euclid_poly(mod, f, g):
    a = None
    b = None
    d = None
    return (a, b, d)

def equals_poly_mod(mod, f, g, h):
    return # "TRUE" or "FALSE"

def irreducible(mod, f):
    return # "TRUE" or "FALSE"

def find_irred(mod, deg):
    return
