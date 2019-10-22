from poly import *

def prime_divisors(a):
    output = []

    while a % 2 == 0:
        a = a/2
        if 2 not in output:
            output.append(2)

    i = 3
    while a != 1:
        while a % i == 0:
            a = a/i
            if i not in output:
                output.append(i)
        i += 2

    return output

def exp_field(mod, mod_poly, a, b):
    z, s, p = [1], a, b

    while p > 0:
        if p % 2 == 1:
            z = multiply_poly(mod, z, s)
        p = p//2
        if p > 0:
            s = multiply_poly(mod, s, s)

    z = long_div_poly(mod, z, mod_poly)[1]

    return z

# Produces the addition table of field F
def add_table(mod, mod_poly):
    deg = deg_poly(mod, mod_poly)
    table = [[]]

    for p in generate_polys(mod, deg - 1):
        table[0].append(p)

    for i in range(1, len(table[0])):
        table.append([])
        for p in table[0]:
            table[i].append(add_poly(mod, table[0][i], p))

    table = [[display_field(mod, mod_poly, p) for p in row] for row in table]
    rows  = [', '.join(row) for row in table]
    return '{' + '; '.join(rows) + '}'

# Produces the multiplication table of F
def mult_table(mod, mod_poly):
    deg = deg_poly(mod, mod_poly)
    table = [[]]

    for p in generate_polys(mod, deg - 1):
        table[0].append(p)

    for i in range(1, len(table[0])):
        table.append([])
        for p in table[0]:
            table[i].append(multiply_poly(mod, table[0][i], p))

    table = [[display_field(mod, mod_poly, p) for p in row] for row in table]
    rows  = [', '.join(row) for row in table]
    return '{' + '; '.join(rows) + '}'

# Give a representative of the following field element of F in standard form
def display_field(mod, mod_poly, a):
    deg_mod_poly = deg_poly(mod, mod_poly)
    deg_a        = deg_poly(mod, a)

    if deg_a < deg_mod_poly:
        return display_poly(mod, a)
    elif deg_a == deg_mod_poly:
        residue = subtract_poly(mod, a, mod_poly)
        residue = [x % mod for x in residue]
        return display_poly(mod, residue)
    else:
        return "idk!"

# Apply addution to the following element in F
def add_field(mod, mod_poly, a, b):
    addAB = add_poly(mod, a, b)
    output = long_div_poly(mod, addAB, mod_poly)[1]

    return output

# Apply subtraction to the following elements in F
def subtract_field(mod, mod_poly, a, b):
    subtractAB = subtract_poly(mod,a, b)
    output = long_div_poly(mod, subtractAB, mod_poly)[1]

    return output

# Apply multiplication to the following elements in F
def multiply_field(mod, mod_poly, a, b):
    multiplyAB = multiply_poly(mod,a, b)
    output = long_div_poly(mod, multiplyAB, mod_poly)[1]

    return  output

# Find a multiplicative inverse of the following element of F
def inverse_field(mod, mod_poly, a):
    [x, y, gcd] = euclid_poly(mod, a, mod_poly)

    if gcd == [1]:
        return add_field(mod, mod_poly, x, mod_poly)
    return "ERROR"

# Apply division of the first field element by the second one
def division_field(mod, mod_poly, a, b):
    inverseB = inverse_field(mod, mod_poly, b)
    if inverseB == "ERROR":
        return "ERROR"
    output = multiply_field(mod, mod_poly, a, inverseB)
    return output

# Test whether the following elements of F are equal
def equals_field(mod, mod_poly, a, b):
    equals = False
    if (mod != [0]):
        if (a != [0]):
            poly1 = long_div_poly(mod, a, mod_poly)[1]

        if (b != [0]):
            poly2 = long_div_poly(mod, a, mod_poly)[1]

        if (poly1 == poly2):
            equals = True

    return equals # True or False

# Test whether the following field element is primitive
def primitive(mod, mod_poly, a):
    deg = deg_poly(mod, a)
    q = mod**deg

    primDivs = prime_divisors(q-1)
    #print(primDivs)

    k = len(primDivs)

    i = 0
    while i < k and exp_field(mod, mod_poly, a, (q-1)/primDivs[i]) != [1]:
        i += 1
    return i >= k

# Give a primitive element of F
def find_prim(mod, mod_poly):
    if not irreducible(mod, mod_poly):
        return "ERROR"

    poly = random_poly(mod, deg_poly(mod, mod_poly)-1)

    while not primitive(mod, mod_poly, poly):
        poly = random_poly(mod, deg_poly(mod, mod_poly)-1)

    output = poly
    return output

# print(add_table(2, [1, 1, 1]))
# print(mult_table(2, [1, 1, 1])) THIS IS NOT CORRECT
# print(add_table(7, [1, 0]))
# print(mult_table(7, [1, 0])) THIS IS NOT CORRECT

# print(display_field(5, [1, 0, 2], [1, 1])) THIS IS NOT CORRECT YET
# print(display_field(5, [1, 0, 2], [1, 0, 0])) THIS IS NOT CORRECT YET
# print(display_field(7, [2, -2], [1, 1, 1])) THIS IS NOT CORRECT YET

# print(add_field(2, [1, 1, 1], [1, 1], [1, 0]))
# print(add_field(7, [2, -2], [1, 1, 1], [2]))

# print(subtract_field(3, [1, 0, 2, 1], [1, 1, 2], [2, 0, 1]))

# print(multiply_field(3, [1, 0, 2, 1], [1, 1], [1, 2]))
# print(multiply_field(3, [1, 0, 2, 1], [1, 0, 0], [1, 0]))

# print(inverse_field(2, [1, 1, 1], [1, 0]))
# print(inverse_field(2, [1, 1, 0], [1, 0]))

# print(division_field(2, [1, 1, 1], [1, 0], [1, 0]))
# print(division_field(2, [1, 1, 1], [1], [1, 0]))
# print(division_field(2, [1, 1, 1], [1], [0]))

# print(equals_field(5, [1, 0, 2], [1, 0, 0], [3]))

# print(primitive(7, [1, 0, 0, 2], [1, 0]))
# print(primitive(7, [1, 0, 0, 2], [1, 0, 1]))

# print(find_prim(7, [1, 0, 6]))
# print(find_prim(7, [1, 0, 0, 2]))
# print(find_prim(7, [1, 0, 1]))
