
import time   # Importando modulos de python
import os

def generar_tablas_multiplicar(numero_tabla):
        
    for num in range(1,13):
        print(f"{numero_tabla} * {num} = {numero_tabla * num}")
        time.sleep(0.15)
        
        

def generar_tablas_multiplicar_defecto(numero_tabla,limite_tabla=12):
        
    for num in range(1,limite_tabla+1):
        print(f"{numero_tabla} * {num} = {numero_tabla * num}")
        time.sleep(0.15)

menu = """
       ****************************************************
       *        MENU PRINCIPAL DE LA APLICACION           * 
       **************************************************** 
       
       Elija la opciòn del reto que desea ejecutar:
       1    :  Tabla de multiplicar
       1000 :  Hello Mundo
       1001 :  Suma Simple
       1002 :  Area Criculo
       1003 :  Suma 2 numeros
       1004 :  Multiplicacion 2 numeros
       1005 :  Promedio 1
       1006 :  Promedio 2
       1007 :  Diferencia
       1008 :  Salario
       1009 :  Salario con Bonus
       1010 :  Calculo simple
       1011 :  Esfera
       1012 :  Area
       1013 :  El mayor
       1014 :  Consumo
       1015 :  Distancia Entre dos puntos
       1016 :  Distancia
       1017 :  Combustible gastado
       1018 :  Billetes
       1019 :  Conversion de Tiempo
       1020 :  Edad en Dias
       1021 :  Billetes y Monedas
       1035 :  Prueba de Seleccion 1
       1036 :  Formula de Bhaskara
       1039 : Intervalo
 
       1037 :   Ejemplo 
       0 :   Salir programa  
"""
bandera = True


while bandera:
    print(menu)
    opcion = int (input("Elija una opción: \n"))
    if opcion == 0:
        print("Hasta pronto!!")
        break
    elif opcion == 1000:
        #Ejercicio 1000
        print("Hello World!") 
    elif opcion == 1001:
        # Ejercicio 1001
        A = int(input("Ingrese #1 de la suma : \n"))
        B = int(input("Ingrese #2 de la suma : \n")) 
        X = A + B
        print(f"X = {X}")
    elif opcion == 1002:
        # Ejercicio 1002
        pi = 3.14159
        radio = float(input("Ingrese el radio de la circunferencia: \n"))
        area = pi * radio**2
    elif opcion == 1003:
        # Ejercicio 1003
        A = int(input("Ingrese el primer valor: \n"))
        B = int(input("Ingrese el segundo valor: \n"))
        C = A + B 
        print(f"SOMA = {C}")
    elif opcion == 1004:
        # Ejercicio 1004
        A = int(input("Ingrese el primer valor: \n"))
        B = int(input("Ingrese el segundo valor: \n"))
        C = A * B
        print(f"PROD = {C}") 
        print(f"A={area:.4f}")
    elif opcion == 1005:
        # Ejercicio 1005
        peso_A = 3.5
        peso_B = 7.5
        A = float(input("Ingrese el valor de A:\n "))
        B = float(input("Ingrese el valor de B:\n "))
        promedio = (A * peso_A + B * peso_B) / (peso_A + peso_B)
        print(f"MEDIA = {promedio:.5f}")
    elif opcion == 1006:
         # Ejercicio 1006
        peso_A = 2
        peso_B = 3
        peso_C = 5
        A = float(input("Ingrese el valor de A: \n"))
        B = float(input("Ingrese el valor de B: \n"))
        C = float(input("Ingrese el valor de C: \n"))
        promedio = (A * peso_A + B * peso_B + C * peso_C) / (peso_A + peso_B + peso_C)
        print(f"MEDIA = {promedio:.1f}")
    elif opcion == 1007:
        # Ejercicio 1007
        A = int(input("Ingrese el valor de A: \n"))
        B = int(input("Ingrese el valor de B: \n"))
        C = int(input("Ingrese el valor de C: \n"))
        D = int(input("Ingrese el valor de D: \n"))
        diferencia = (A*B - C*D)
        print(f"DIFERENCIA = {diferencia}")
    elif opcion == 1008:
        # Ejercicio 1008
        A = int(input("Ingrese el numero de empleados:\n"))
        B = int(input("Ingrese el numero de horas trabajadas:\n"))
        C = float(input("Ingrese el salario:\n"))
        calculo = B * C
        print(f"NUMBER = {A}")
        print(f"SALARY = {calculo:.2f}")     
    elif opcion == 1009:
        # Ejercicio 1009:
        nombre = input("Ingrese el nombre del vendedor:\n")
        salario = float(input("Ingrese el valor del salario:\n"))
        total_vendido = float(input("Ingrese el valor del de las ventas:\n"))
        comision = total_vendido * 0.15
        saldo_total = comision + salario
        print(f"TOTAL = R$ {saldo_total:.2f}") 
    elif opcion == 1010:
        # Ejercicio 1010
        # Ejercicio 1010
        producto_1 = input()
        producto_2 = input()

        valores_1 = producto_1.split(" ")
        valores_2 = producto_2.split(" ")

        suma_total_1 = float(valores_1[0]) * float(valores_1[1])
        suma_total_2 = float(valores_2[0]) * float(valores_2[1])

        suma_total = suma_total_1 + suma_total_2    

        print(f"VALOR A PAGAR: R$ {suma_total:.2f}")
    elif opcion == 1011:
        # Ejercicio 1011
        radio = int(input("Ingrese el valor del radio:\n"))
        pi = 3.14159
        formula = (4.0/3) * pi * radio**3
        print(f"VOLUME = {formula:.3f}")
    elif opcion == 1012:
        # Ejercicio 1012
        A = float(input())
        B = float(input())
        C = float(input())
        area_triangulo = (A * C) / 2
        print(f"TRIANGULO: {area_triangulo:.3f}")
        area_circulo = 3.14159 * C ** 2
        print(f"CIRCULO: {area_circulo:.3f}")
        area_trapecio = ((A + B) * C) / 2
        print(f"TRAPEZIO: {area_trapecio:.3f}")
        area_cuadrado = B ** 2
        print(f"QUADRADO: {area_cuadrado:.3f}")
        area_rectangulo = A * B
        print(f"RETANGULO: {area_rectangulo:.3f}")
    elif opcion == 1013:
        # Ejercicio 1013
        a = int(input("Ingresar el valor de a:\n"))
        b = int(input("Ingresar el valor de b:\n"))
        c = int(input("Ingresar el valor de c:\n"))
        mayor = int((a + b + abs(a - b)) / 2)
        mayor = int((mayor + c + abs(mayor - c)) / 2)  
        print(f"{mayor} eh o maior")
    elif opcion == 1014:
        # Ejercicio 1014
        X = int(input("Ingrese el valor de la distancia recorrida:\n"))
        Y = float(input("Ingrese el valor del total de combustible gastado: \n"))
        Z = X / Y
        print(f"{Z:.3f} km/l")
    elif opcion == 1015:
        # Ejercicio 1015
        punto_1 = input("Ingrese el valor de x1/y1:\n").split(" ")
        punto_2 = input("Ingrese el valor de x2/y2:\n").split(" ")
        x1 = float(punto_1[0])
        x2 = float(punto_2[0])
        y1 = float(punto_1[1])
        y2 = float(punto_1[1])
        promedio = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        print(f"La distancia entre los puntos es:\n{promedio}")
    elif opcion == 1016:
        # Ejercicio 1016
        X = int(input("Ingrese la cantidad de distancia:\n")) 
        Y = X*2
        print(f"{Y} minutos")
    elif opcion == 1017:
        # Ejercicio 1017
        X = int(input("Ingrese el tiempo que duro el viaje:\n"))
        Y = int(input("Ingrese la velocidad media del viaje:\n"))
        Z = X*Y /12
        print(f"{Z:.3f}")
    elif opcion == 1018:
        # Ejercicio 1018
        valor = int(input("Ingrese una cantidad:\n"))
        dinero = [100, 50, 20, 10, 5, 2, 1]
        print(valor)
        for billete in dinero:
            cantidad = valor // billete  
            print(f"{cantidad} nota(s) de R$ {billete},00")
            valor %= billete 
    elif opcion == 1019:
        # Ejercicio 1019
        N = int(input("Ingrese los valores que desea convertir a horas/minutos/segundos:\n"))
        H = N // 3600
        M = (N % 3600)// 60
        S = N % 60
        print(f"{H}:{M}:{S}")
    elif opcion == 1020:
        # Ejercicio 1020
        N = int(input("Ingrese los valores que desea convertir a dias/meses/años:\n"))
        A = N // 365
        M = (N % 365) // 30
        D = (N % 365) % 30
        print(f"{A} ano(s)")
        print(f"{M} mes(es)")
        print(f"{D} dia(s)")
    elif opcion == 1021:
        # Ejercicio 1021
        valor = float(input("Ingrese un valor con dos decimales:\n"))              
        print("NOTAS:")
        for i in [100, 50, 20, 10, 5, 2]:
            print(f"{int(valor/i)} nota(s) de R$ {i}.00")
            valor = float(f"{valor%i:.2f}")                
        print("MOEDAS:")
        for i in [1, 0.50, 0.25, 0.10, 0.05, 0.01]:
            print(f"{int(valor/i)} moeda(s) de R$ {i:.2f}")
            valor = float(f"{valor%i:.2f}")
    elif opcion == 1035:
        # Ejercicio 1035
        punto_1 = input("Ingrese los valores:\n").split(" ")
        A = int(punto_1[0])
        B = int(punto_1[1])
        C = int(punto_1[2])
        D = int(punto_1[3])
        if B > C and D > A and C+D > A+B and C > 0 and D > 0 and A % 2 == 0:
            print("Valores aceitos")
        else:
            print("Valores no aceitos")
    elif opcion == 1036:
        # Ejercicio 1036
        punto_1 = input("Ingrese los valores de a,b,c:\n").split(" ")
        A = float(punto_1[0])
        B = float(punto_1[1])
        C = float(punto_1[2])
        discriminante = B**2 - 4*A*C
        if A == 0 or discriminante < 0:
            print("Impossivel calcular")
        else:
            bhaskara = (-B - discriminante**0.5) / (2*A)
            bhaskara1 = (-B + discriminante**0.5) / (2*A)
            print(f"R1 = {bhaskara:.5f}")
            print(f"R2 = {bhaskara1:.5f}")
    elif opcion == 1037:
        # Ejercicio 1037
        N = float(input("Ingrese el valor del intervalo:\n"))
        if 0 <= N <= 25:
            print("Intervalo [0,25]")
        elif 25 < N <= 50:
            print("Intervalo (25,50]") 
        elif 50 < N <= 75:
            print("Intervalo (50,75]")
        elif 75 < N <= 100:
            print("Intervalo (75,100]")
        else:
            print("Fora de intervalo")
    elif opcion == 1:
        # Ejercicio 1
        num_tabla =  int (input("Ingresa el numero de la tabla que deseas generar: \n"))
        limite_tabla = int (input("Ingresa el limite de la secuencia de la tabla \n"))
        if limite_tabla > 0:        
            generar_tablas_multiplicar_defecto(num_tabla,limite_tabla)
        time.sleep(2) 
        os.system("cls")    
    else:
        print("La opcion seleccionada no existe!!")


    