




# Funciones con argumentos indeterminados 
# *args = Representacion de un conjunto de elementos mediante una tupla : '()'

def concatenar_cadenas(*args):  #  'Hola', 'Mundo', 'Python', '2024
    cadena_final = ' '
    print(f"La tupla tiene: {len(args)} argumentos ")
    for arg in args:
        cadena_final += arg + ' '

    return cadena_final

# Invocacion con argumentos indeterminados 

print(f"El resultado de concatenar los strings  : {concatenar_cadenas('Hola', 'Mundo', 'Python', '2024')}")