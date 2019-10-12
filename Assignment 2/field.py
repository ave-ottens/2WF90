import poly as p

def add_table(mod, mod_poly):
    return

def mult_table(mod, mod_poly):
    return

def display_field(mod, mod_poly, a):
    return

def add_field(mod, mod_poly, a, b):
    addAB = p.add_poly(mod, a, b)
    output = p.long_div_poly(mod, addAB, mod_poly)[1]
    
    return output 

def subtract_field(mod, mod_poly, a, b):
    subtractAB = p.subtract_poly(mod,a, b)
    output = p.long_div_poly(mod, subtractAB, mod_poly)[1]

    return output 

def multiply_field(mod, mod_poly, a, b):
    multiplyAB = p.multiply_poly(mod,a, b)
    output = p.long_div_poly(mod, multiplyAB, mod_poly)[1]

    return  output

def inverse_field(mod, mod_poly, a):
    return 

def division_field(mod, mod_poly, a, b):
    return 

def equals_field(mod, mod_poly, a, b):
    equals = False
    if (mod != [0]):
        if (a != [0]):
            poly1 = p.long_div_poly(mod, a, mod_poly)[1]

        if (b != [0]):
            poly2 = p.long_div_poly(mod, a, mod_poly)[1]

        if (poly1 == poly2):
            equals = True

    return equals # True or False

def primitive(mod, mod_poly, a):
    return

def find_prim(mod, mod_poly):
    return 