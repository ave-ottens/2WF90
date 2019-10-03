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
    listFG = f, g    
    maxLen = max(map(len, listFG))
        
    # add digits
    for digits in listFG:
        while len(digits) < maxLen:
            digits.insert(0, 0)

    # add element of f with index i with element of g with index i 
    sumPoly = [sum(x) for x in zip(*listFG)]
    output = sumPoly.copy()

    for i in range(len(output)):
        output[i] = output[i] % mod

    return output

def subtract_poly(mod, f, g):
    listFG = f, g
    maxLen = max(map(len, listFG))
        
    # add digits
    for digits in listFG:
        while len(digits) < maxLen:
            digits.insert(0, 0) 

    # difference between the digits from f with g according to index in each list
    diffFG = [0] * maxLen
    for i in range(maxLen):
        diffFG[i] = f[i] - g[i]
    output = diffFG.copy()

    for i in range(len(output)):
        output[i] = output[i] % mod

    return output

def multiply_poly(mod, f, g):
    listFG = f, g    
    maxLen = max(map(len, listFG))
        
    for digits in listFG:
        while len(digits) < maxLen:
            digits.insert(0, 0)

    multFG = [0]*2*maxLen

    for i in range(0, maxLen):
        digit2 = g[-(i+1)]
        for j in range(0, maxLen):
            digit1 = f[-(j+1)]
            outputNumber = digit1 * digit2
            multFG[-(1+i+j)] += outputNumber

    output = multFG.copy()
  
    for i in range(len(output)):
        output[i] = output[i] % mod

    return output

def long_div_poly(mod, f, g):
    q = [0]
    r = f

    if g == [0]:
        return {
            "answ-q": 'error',
            "answ-r": 'error'
        }

    degR = deg_poly(mod, r)
    degG = deg_poly(mod, g)

    while degR >= degG:

        coefficient_q = degR - degG

        x_pow_coef_q = [1] + [0]*coefficient_q

        while r[0] / g[0] != 0:
            r[0] += mod
        second_part = multiply_poly(mod,[r[0] / g[0]], x_pow_coef_q)

        # q = q + second_part
        q = add_poly(mod, q, second_part)

        #lc(r)/lc(g) * x^(deg(r) - deg(g)) * g
        second_part_g = multiply_poly(mod,second_part, g)

        # r = r - second_part_g
        r = subtract_poly(mod, r, second_part_g)

    # remove preceding zeroes
    while q[0] == 0 and not len(q) == 1:
        q = q[1:]
    while r[0] == 0 and not len(r) == 1:
        r = r[1:]

    # apply modulo
    q = mod_poly(q, m)
    r = mod_poly(r, m)


    return {
        "answ-q": q,
        "answ-r": r
    }

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
