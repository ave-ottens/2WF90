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

def mod_poly(mod, f):
    for i in range(0, len(f)):
        f[i] = f[i] % mod

    return f

def pop_zeros(f):
    i = 0
    while i < (len(f) - 1):
        if (f[i] == 0):
            f.pop(0)
            continue
        break

    return f

def add_poly(mod, f, g):
    listFG = f, g    
    maxLen = max(map(len, listFG))
        
    # add digits to make f and g of equal length
    for digits in listFG:
        while len(digits) < maxLen:
            digits.insert(0, 0)

    # add element of f with index i with element of g with index i and do this for all elements
    sumPoly = [sum(x) for x in zip(*listFG)]

    # do modular reduction and then pop all unnecessary zeros 
    sumPolyMod = mod_poly(mod, sumPoly)
    output = pop_zeros(sumPolyMod)

    return output

def subtract_poly(mod, f, g):
    listFG = f, g
    maxLen = max(map(len, listFG))
        
    # add digits to make f and g of equal length
    for digits in listFG:
        while len(digits) < maxLen:
            digits.insert(0, 0) 

    # difference between the digits from f with g according to index in each list
    diffFG = [0] * maxLen
    for i in range(maxLen):
        diffFG[i] = f[i] - g[i]

    # do modular reduction and then pop all unnecessary zeros 
    diffFGMod = mod_poly(mod, diffFG)
    output = pop_zeros(diffFGMod)

    return output

def multiply_poly(mod, f, g):
    listFG = f, g    
    maxLen = max(map(len, listFG))
        
    # add digits to make f and g of equal length
    for digits in listFG:
        while len(digits) < maxLen:
            digits.insert(0, 0)

    # add zero's to make sure that when multiplying it's possible to each element and have room for it in list multFG 
    multFG = [0] * 2 * maxLen

    # do the multiplication 
    for i in range(0, maxLen):
        digit2 = g[-(i + 1)]
        for j in range(0, maxLen):
            digit1 = f[-(j + 1)]
            outputNumber = digit1 * digit2
            multFG[-(1 + i + j)] += outputNumber
  
    # do modular reduction and then pop all unnecessary zeros 
    multFGMod = mod_poly(mod, multFG)
    output = pop_zeros(multFGMod)

    return multFG

def long_div_poly(mod, f, g):
    q = [0]
    r = f

    if g == [0]:
        return 'ERROR' 

    # calculate the degree of r and g 
    degR = deg_poly(mod, r)
    degG = deg_poly(mod, g)

    while degR >= degG:
        coefficient_q = degR - degG

        x_pow_coef_q = [1] + [0] * coefficient_q

        while r[0] / g[0] % 1 != 0:
            r[0] += mod
        
        second_part = multiply_poly(mod,[r[0] // g[0]], x_pow_coef_q)

        # q = q + second_part
        q = add_poly(mod,q, second_part)

        #lc(r)/lc(g) * x^(deg(r) - deg(g)) * g
        second_part_g = multiply_poly(mod,second_part, g)

        # r = r - second_part_g
        r = subtract_poly(mod, r, second_part_g)

        degR = deg_poly(mod, r)
        degG = deg_poly(mod, g)

    # pop the zeros and apply modulo
    q_popped = pop_zeros(q)
    r_popped = pop_zeros(r)
    q = mod_poly(mod, q_popped)
    r = mod_poly(mod, r_popped)

    return q, r

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
