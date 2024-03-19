




#  Tuplas son inmutables 
tuplas_1 = (1,2,3,4,5,6,7,8,9,10)  # *args
#tuplas_1 [0] = 100
print(f"La tupla tiene {tuplas_1}")

def triplica(*args):
    for i in args:
        pass

#triplica(1,2,3)
#triplica(tuplas_1)


# Diccionarios:

diccionario_1 = {'1':100, '2':200, '3':300, '4':400, 'A':'LibroA' }

for k in diccionario_1.keys():     # La funcion keys corresponde a 1,2,3,4
    print(f"Key : {k}")

for k in diccionario_1.values():   # La funcion valaues corresponde a 100,200,300,400
    print(f"Key : {k}")

for k,v in diccionario_1.items():
    print(f"{k} <--> {v}")         # La funcion items devuelve la posicion y lo que hay en la posicion