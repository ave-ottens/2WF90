import poly as p

# Produces the addition table of field F
def add_table(mod, mod_poly):
    return

# Produces the multiplication table of F
def mult_table(mod, mod_poly):
    return

# Give a representative of the following field element of F in standard form
def display_field(mod, mod_poly, a):
    return

# Apply addution to the following element in F
def add_field(mod, mod_poly, a, b):
    addAB = p.add_poly(mod, a, b)
    output = p.long_div_poly(mod, addAB, mod_poly)[1]
    
    return output 

# Apply subtraction to the following elements in F
def subtract_field(mod, mod_poly, a, b):
    subtractAB = p.subtract_poly(mod,a, b)
    output = p.long_div_poly(mod, subtractAB, mod_poly)[1]

    return output 

# Apply multiplication to the following elements in F
def multiply_field(mod, mod_poly, a, b):
    multiplyAB = p.multiply_poly(mod,a, b)
    output = p.long_div_poly(mod, multiplyAB, mod_poly)[1]

    return  output

# Find a multiplicative inverse of the following element of F
def inverse_field(mod, mod_poly, a):
    return 

# Apply division of the first field element by the second one
def division_field(mod, mod_poly, a, b):
    return 

# Test whether the following elements of F are equal
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

# Test whether the following field element is primitive
def primitive(mod, mod_poly, a):
    return

# Give a primitive element of F
def find_prim(mod, mod_poly):
    return 

# print(add_table(2, [1, 1, 1])) THIS IS NOT CORRECT YET
# print(mult_table(2, [1, 1, 1])) THIS IS NOT CORRECT YET
# print(add_table(7, [1, 0])) THIS IS NOT CORRECT YET
# print(mult_table(7, [1, 0])) THIS IS NOT CORRECT YET

# print(display_field(5, [1, 0, 2], [1, 1])) THIS IS NOT CORRECT YET
# print(display_field(5, [1, 0, 2], [1, 0, 0])) THIS IS NOT CORRECT YET
# print(display_field(7, [2, -2], [1, 1, 1])) THIS IS NOT CORRECT YET

# print(add_field(2, [1, 1, 1], [1, 1], [1, 0])) 
# print(add_field(7, [2, -2], [1, 1, 1], [2]))

# print(subtract_field(3, [1, 0, 2, 1], [1, 1, 2], [2, 0, 1])) 

# print(multiply_field(3, [1, 0, 2, 1], [1, 1], [1, 2]))
# print(multiply_field(3, [1, 0, 2, 1], [1, 0, 0], [1, 0]))

# print(inverse_field(2, [1, 1, 1], [1, 0])) THIS IS NOT CORRECT YET
# print(inverse_field(2, [1, 1, 0], [1, 0])) THIS IS NOT CORRECT YET

# print(division_field(2, [1, 1, 1], [1, 0], [1, 0])) THIS IS NOT CORRECT YET
# print(division_field(2, [1, 1, 1], [1], [1, 0])) THIS IS NOT CORRECT YET 
# print(division_field(2, [1, 1, 1], [1], [0])) THIS IS NOT CORRECT YET 

# print(equals_field(5, [1, 0, 2], [1, 0, 0], [3]))

# print(primitive(7, [1, 0, 0, 2], [1, 0])) THIS IS NOT CORRECT YET 
# print(primitive(7, [1, 0, 0, 2], [1, 0, 1])) THIS IS NOT CORRECT YET 

# print(find_prim(7, [1, 0, 6)) THIS IS NOT CORRECT YET
# print(find_prim(7, [1, 0, 1])) THIS IS NOT CORRECT YET
# print(find_prim(7, [1, 0, 1])) THIS IS NOT CORRECT YET


