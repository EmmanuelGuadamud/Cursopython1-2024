



def multiplicacion(**kwargs):
    for k, v in kwargs.items():     #     index, dato   <---enumerate(lista)
        print(f"{k} : {v}") 

# Diccionarios 

diccionarios  = {'1':'True', '2':2.5, '3':3.5, '4':4.5}

multiplicacion(n1=1, n2=2, ab=4, z2=4.6, nombre = 'Emmanuel')       # Se puede poner cualquier nombre de variable 






def multiplicacion(**kwargs):
    multiplicacion = 1
    for key, valor in kwargs.items():     #     index, dato   <---enumerate(lista)
        print(f"{key} : {valor}") 
        multiplicacion *= valor

    print(multiplicacion)


multiplicacion(n1=1, n2=2, numero3 = 3, valor = 4)       # Se puede poner cualquier nombre de variable 