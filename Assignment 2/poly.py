from random import randint

# Give the standard representative of the following polynomial
def display_poly(mod, f):
    """Return polynomial f as its string representation."""
    terms = [] # list of strings to be concatenated later

    power = len(f) - 1
    for coef in f:
        # coef is the coefficient
        # power is the power of X the coefficient relates to

        # normalize chew such that 0 <= coef < mod
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
    if len(terms) == 0:
        return '0'
    else:
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

    return -1 # non-zero coefficient could not be found

# An irreducible polynomial
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

def modular_inversion(mod, f):
    r = f % mod
    i = 1
    while r != 1 and i <= mod:
        i += 1
        r = i * f % mod

    if r == 1:
        return i
    else:
        return "NO INV"

# Apply addition to the following two polynomials
def add_poly(mod, f, g):
    listFG = f, g
    maxLen = max(map(len, listFG))

    # add digits to make f and g of equal length
    for digits in listFG:
        while len(digits) < maxLen:
            digits.insert(0, 0)

    # add element of f with index i with element of g with index i and do this for all elements
    sumFG = [sum(x) for x in zip(*listFG)]

    # do modular reduction and then pop all unnecessary zeros
    sumFGMod = mod_poly(mod, sumFG)
    output = pop_zeros(sumFGMod)

    return output

# Apply subtraction to the following two polynomials
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

# Apply multiplication to the following two polynomials
def multiply_poly(mod, f, g):
    numberF, numberG = f.copy(), g.copy()
    listFG = numberF, numberG
    maxLen = max(map(len, listFG))

    # add digits to make f and g of equal length
    for digits in listFG:
        while len(digits) < maxLen:
            digits.insert(0, 0)

    # add zero's to make sure that when multiplying it's possible to each element and have room for it in list multFG
    multFG = [0] * 2 * maxLen

    # do the multiplication
    for i in range(0, maxLen):
        digit2 = numberG[-(i + 1)]
        for j in range(0, maxLen):
            digit1 = numberF[-(j + 1)]
            outputNumber = digit1 * digit2
            multFG[-(1 + i + j)] += outputNumber

    # do modular reduction and then pop all unnecessary zeros
    multFGMod = mod_poly(mod, multFG)
    output = pop_zeros(multFGMod)

    return output

# Apply long division of the first polynomials by the second
def long_div_poly(mod, f, g):
    q = [0]
    rem = [0]
    r = f

    if g == [0]:
        return 'ERROR', 'ERROR'

    # calculate the degree of r and g
    degR = deg_poly(mod, r)
    degG = deg_poly(mod, g)
    while degR >= degG:
        coefficient_q = degR - degG
        x_pow_coef_q = [1] + [0] * coefficient_q
        bestR = mod
        rem_part = [0]
        tempQ = r[0] // g[0]
        while r[0] % g[0] != 0:
            r[0] += mod
            bestR = min(bestR, r[0] % g[0])
            tempQ = r[0] // g[0]
            if r[0] >= g[0] * mod and r[0] % g[0] == bestR:
                tempQ = r[0] // g[0] % mod
            else:
                continue
            break
        second_part = multiply_poly(mod,[tempQ], x_pow_coef_q)

        # q = q + second_part
        q = add_poly(mod, q, second_part)

        #lc(r)/lc(g) * x^(deg(r) - deg(g)) * g
        second_part_g = multiply_poly(mod, second_part, g)

        # r = r - second_part_g
        r = subtract_poly(mod, r, second_part_g)

        rem_part = [bestR] + [0] * (degR)
        rem = add_poly(mod, rem, rem_part)

        r = subtract_poly(mod, r, rem_part)

        pop_zeros(r)
        pop_zeros(g)

        degR = deg_poly(mod, r)
        degG = deg_poly(mod, g)

    r = add_poly(mod, r, rem)

    # pop the zeros and apply modulo
    q_popped = pop_zeros(q)
    r_popped = pop_zeros(r)
    q = mod_poly(mod, q_popped)
    r = mod_poly(mod, r_popped)

    return q, r

# Euclid's Extended Algorithm
def euclid_poly(mod, f, g):
    x, u = [1], [0]
    y, v = [0], [1]
    a, b = f.copy(), g.copy()
    eqZero = b[0] == 0

    while not eqZero:
        [q, r] = long_div_poly(mod, a, b)
        if q == "ERROR":
            return "ERROR"
        a = b
        b = r
        xPrime = x
        yPrime = y
        x = u
        y = v
        qu = multiply_poly(mod, u, q)
        qv = multiply_poly(mod, v, q)
        u = subtract_poly(mod, xPrime, qu)
        v = subtract_poly(mod, yPrime, qv)
        pop_zeros(a)
        pop_zeros(b)
        if (b[0] == 0):
            eqZero = True

    d = a
    if a[0] != 1:
        invA = modular_inversion(mod, a[0])
        d = multiply_poly(mod, d, [invA])
    else:
        invA = a[0]

    a = multiply_poly(mod, x, [invA])
    b = multiply_poly(mod, y, [invA])
    return a, b, d

# Test whether the following two polynomials are equal
def equals_poly_mod(mod, f, g, h):
    if h == [] or h == [0]:
        return False
    remF = long_div_poly(mod, f, h)[1]
    remG = long_div_poly(mod, g, h)[1]
    if remF == remG:
        return True
    return False

# Test whether the following polynomial is irreducible
def irreducible(mod, f):

    def construct_poly(deg):
        poly = [1] + [0] * deg
        poly[deg - 1] = -1 # -1 because you need to do X^q^t - X
        return poly

    t = 1
    g = construct_poly(pow(mod, t)) # create polynomial X^q^t
    gcd = euclid_poly(mod, f, g)[2] # get gcd

    while gcd == [1]:
        t = t + 1
        g = construct_poly(pow(mod, t))
        gcd = euclid_poly(mod, f, g)[2]
        n = deg_poly(mod, f)

        if t <= n:
            continue
        break

    # If t = deg(f) return true else false
    b = False
    if t == deg_poly(mod, f):
        b = True

    return b # True or False

# Give an irreducible polynomial of degree [deg]
def find_irred(mod, deg):
    for p in generate_polys(mod, deg):
        if not deg_poly(mod, p) == deg:
            continue
        if irreducible(mod, p):
            return p

    return 'ERROR'

def generate_polys(mod, deg, current = []):
    if len(current) >= deg + 1:
        yield current
    else:
        for n in range(mod):
            yield from generate_polys(mod, deg, current.copy() + [n])

def random_poly(mod, deg):
    output = []

    for i in range(deg+1):
        output.append(randint(0, mod-1))

    if pop_zeros(output) == [0]:
        output = random_poly(mod, deg)

    return output

# print(display_poly(7, [1, 2, 6]))
# print(display_poly(5, [1, 2, 6]))
# print(display_poly(7, [1, 2, 0]))
# print(display_poly(7, [1, 2, 7]))
# print(display_poly(7, [0, 1, 2, 0]))
# print(display_poly(7, [-1, 0, 1, 3]))
# print(display_poly(7, [0, 1, 10, -1, 0, 2, 3]))
# print(display_poly(7, [0]))
# print(display_poly(7, [0, 0]))

# print(add_poly(7, [5, 2, 3], [2, 3, 4, 0]))

# print(subtract_poly(7, [1, 2, 3], [2, 3, 4, 0]))

# print(multiply_poly(7, [6], [5]))
# print(multiply_poly(7, [27], [33]))
# print(multiply_poly(7, [1, 1, 1], [1, -1]))

# print(long_div_poly(7, [6], [5]))
# print(long_div_poly(7, [1, 1, 1], [2, -2]))
# print(long_div_poly(7, [1, 1, 1], [0]))

#print(euclid_poly(7, [1, 1, 1], [2, -2]))
#print(euclid_poly(7, [1, 0, 1], [1, 0, 0, 1]))
#print(euclid_poly(2, [1, 0, 1], [1, 0, 0, 1]))
#print(euclid_poly(7, [1, 1, 1], [0]))
#print(euclid_poly(7, [2, 2, 2], [0]))

# print(equals_poly_mod(7, [1, 1, 1], [10], [1, -1]))
# print(equals_poly_mod(5, [1, 1, 1], [10], [1, -1]))
# print(equals_poly_mod(7, [1, 1, 1], [3], [0]))

# print(irreducible(2, [1, 1, 1]))
# print(irreducible(3, [1, 1, 1]))

# print(find_irred(2, 3))
# print(find_irred(2, 4))
