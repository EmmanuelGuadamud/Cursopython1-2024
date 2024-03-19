



# Tipos compuestos: Lista '[]', Tuplas '()' y Diccionarios '{}'


def suma(lista_numeros):

    suma_total = 0
    for element in lista_numeros:
        suma_total += element * 3

    return suma_total


lista = [1.0, 2.0, 3.0, 4.0]  # Lista original
print(f"La suma total de los valores = {suma(lista_numeros=lista)}")
print(f" Lista final : {lista}")



def suma(lista_numeros):

    suma_total = 0
    for index,dato in enumerate(lista_numeros):
        suma_total += dato 
        lista_numeros[index] *= 4

    return suma_total


lista = [1.0, 2.0, 3.0, 4.0]  # Lista original
print(f"La suma total de los valores = {suma(lista_numeros=lista)}")
print(f" Lista final : {lista}")



def suma(lista_numeros):

    suma_total = 0
    lista_numeros_1 = []
    lista_numeros_1.copy()  #Respaldar información  ---->   Referencia en memoria es distinta 
    lista_aux2 = lista_numeros_1[:]

    for index,dato in enumerate(lista_numeros):
        suma_total += dato 
        lista_numeros[index] *= 4

    return suma_total


lista = [1.0, 2.0, 3.0, 4.0]  # Lista original
print(f"Lista original: {lista}")
print(f"La suma total de los valores = {suma(lista_numeros=lista)}")
print(f" Lista final : {lista}")