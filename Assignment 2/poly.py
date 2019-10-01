def display_poly(mod, poly):
    """Return poly as its string representation."""
    terms = [] # list of strings to be concatenated later

    power = len(poly) - 1
    for coef in poly:
        # coef is the coefficient
        # power is the power of X the coefficient relates to

        # normalize coef such that 0 <= coef < mod
        coef = coef % mod

        # case distinction: ignore coefficients that are zero
        if coef == 1:
            if power == 0:
                terms.append('1')
            elif power == 1:
                terms.append('X')
            elif power > 1:
                terms.append(f'X^{power}')
        elif coef > 1:
            if power == 0:
                terms.append(str(coef))
            elif power == 1:
                terms.append(f'{coef}X')
            elif power > 1:
                terms.append(f'{coef}X^{power}')

        power = power - 1

    # return terms with '+' symbols inbetween
    return '+'.join(terms)

def deg_poly(mod, poly):
    """Return the degree of poly. (See Section 2.2)"""
    power = len(poly) - 1

    # find the first non-zero coefficient (after taking the mod)
    for coef in poly:
        coef = coef % mod

        if not coef == 0:
            return power # return power related to coefficient

        power = power - 1

    return 0 # non-zero coefficient could not be found

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
    """
    work in progress ;-)
    t = 1
    q = deg_poly(mod, f)

    def generate_divisor():
        poly = [0] *
        return

    while True:
        _, _, gcd = euclid_poly(mod, f, )
    """
    return

def find_irred(mod, deg):
    return
