



  #  Listas []  ;  *args


def suma (numero_1, numero_2):
    return numero_1 + numero_2

# Argumentos indeterminados

def suma (*args):   # Lista []
    suma_total = 0
    for arg in args:
        print(f"[{arg}]")
        suma_total += arg
    print(f"suma_total = {suma_total}")

# Invocacion 

suma(1,3,5,7,9,11)  # Creando super funciones, aunque agregues mas, se siguen sumando



# Elevados al cuadrado 

def eleva_al_cuadrado(*args):
    for index,arg in enumerate(args):
        #args[index] *=2   # Los argumentos se guardan en forma tupla siempre
        print(f"{index}  {arg}")

    return args


#bandera:True
#while bandera:
#    print("Ingresa los datos a ser elevados al cuadrado")
#    lista = input("Ingrese los datos separaos por comas: ") # 1,2,3,4,5 
    
lista = eleva_al_cuadrado(1,2,3,4,5,6,6,6,6,6,6,6,7,8,9)
print(type(lista))
print(lista)


