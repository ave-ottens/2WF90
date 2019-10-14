from poly import *

def add_table(mod, mod_poly):
    if not irreducible(mod_poly):
        return 'ERROR'

    deg = deg_poly(mod, mod_poly)
    table = [[]]

    for p in generate_polys(mod, deg - 1):
        table[0].append(p)

    for i in range(1, len(table[0])):
        table.append([])
        for p in table[0]:
            table[i].append(add_poly(mod, table[0][i], p))

    table = [[display_poly(mod, p) for p in row] for row in table]
    rows  = [', '.join(row) for row in table]
    return '{' + '; '.join(rows) + '}'


def mult_table(mod, mod_poly):
    deg = deg_poly(mod, mod_poly)
    table = [[]]

    for p in generate_polys(mod, deg - 1):
        table[0].append(p)

    for i in range(1, len(table[0])):
        table.append([])
        for p in table[0]:
            table[i].append(multiply_poly(mod, table[0][i], p))

    table = [[display_poly(mod, p) for p in row] for row in table]
    rows  = [', '.join(row) for row in table]
    return '{' + '; '.join(rows) + '}'

def display_field(mod, mod_poly, a):
    return

def add_field(mod, mod_poly, a, b):
    return

def subtract_field(mod, mod_poly, a, b):
    return

def multiply_field(mod, mod_poly, a, b):
    return

def inverse_field(mod, mod_poly, a):
    return

def division_field(mod, mod_poly, a, b):
    return

def equals_field(mod, mod_poly, a, b):
    return

def primitive(mod, mod_poly, a):
    return

def find_prim(mod, mod_poly):
    return
