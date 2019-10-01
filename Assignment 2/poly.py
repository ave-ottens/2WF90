def display_poly(mod, f):
    """Return polynomial f as its string representation."""
    terms = [] # list of strings to be concatenated later

    power = len(f) - 1
    for coef in f:
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

def deg_poly(mod, f):
    """Return the degree of polynomial f. (See Section 2.2)"""
    power = len(f) - 1

    # find the first non-zero coefficient (after taking the mod)
    for coef in f:
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
    return # True or False

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
    return False # True or False

def find_irred(mod, deg):
    # generate polynomials recursively, until the right one is found
    def find_irred_recursive(f = []):
        if len(f) < deg - 1:
            for n in range(0, mod):
                result = find_irred_recursive([n] + f)
                if not result == None:
                    return result

        elif len(f) == deg - 1:
            # ensure that the left coefficient isn't zero
            for n in range(1, mod):
                result = find_irred_recursive([n] + f)
                if not result == None:
                    return result

        else:
            if irreducible(mod, f):
                return f
            else:
                return None

    answer = find_irred_recursive()

    if answer:
        return answer
    else:
        return 'ERROR'
