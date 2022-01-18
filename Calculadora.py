import time
import operator

#VARIABLES globales / Global VARIABLES
power = True

#Funciones INPUT / INPUT Functions
def inputs(operacion): #El usuario entrará aquí cada vez que quiera realizar una operación sencilla / The user will enter here if he wants to do a simple math problem
    while power:
        try:
            numeroUno = float(input(f"Digita el primer valor de la {operacion}: "))
            numeroDos = float(input(f"Digita el segundo valor {operacion}: "))
            return numeroUno, numeroDos
            break
        except:
            continuar = errornum()
            if continuar == False:
                break

#Función calculadora libre (El usuario escribe la operación) / Free calculator function (the user types the operation and the code solves it)
def libre():
    while power:
        try:
            #Le pide al usuario que introdzca una operación / Asks the user for a math problem to solve
            operacion = input("""Introduzca la operación a realizar o escriba 'salir' para salir.\n>> """)
            if operacion.upper() == "SALIR":    break #Si el usuario escribe 'salir' volverá al menú principal / if the user types 'salir', he will go back to the main menu
            else:   
                #print(eval(operacion)) 

                operacion = operacion + "$" 
                #Le sumará un '$' es para indicar cuando termina la lista. Ejemplo: problema = [1, '+', 1, '$']
                #It will add a '$' to indicate when the list is over. Example: problem = [1, '+', 1, '$']

                operadores = ( "+", "-", "*", "/", "$") #Operadores / Operators
                problema = [] #Aquí se seccionará la operación entre números y operadores / Here the operation will be stored divided in numbers and operators
                
                numero = ""
                for val in operacion: #Recorre la operación y verifica si val es número u operador / Iterates the math operation and verifies if the val is a number or a operator
                    if val in operadores:
                        problema.append(int(numero))
                        problema.append(val)
                        numero = ""
                    elif val not in operadores:
                        numero = numero + val

                operacion = 0 #Aquí se irá almacenando el resultado conforme se hagan las operaciones / Here will be stored the final result while the operations are solved
                operador = "" #Aquí se almacenará cada operador en medio de dos valores / Here will be stored every operator in the middle of 2 vals
                primeraPosición = True #El primer número no se puede operar por uno antes de él, ya que él es el primero / The first number can't be operated with other value before him, because he is the first one 
                
                #Este 'for' separa números de operadores, y cuando encuentra un número después de un operador, realizará la operación
                #This 'for' separates numbers from operators, when it finds a number after having finded an operator, it will solve a simple operation
                for val in problema: 
                    if val == '*':  operador = val
                    elif val == '/':    operador = val
                    elif val == '+':    operador = val
                    elif val == '-':    operador = val
                    elif val == '$':    break
                    else:
                        if primeraPosición:
                            operacion = val
                            primeraPosición = False 
                        else:
                            if operador == '*': operacion = operacion * val
                            elif operador == '/':   operacion = operacion / val
                            elif operador == '+':   operacion = operacion + val
                            elif operador == '-':   operacion = operacion - val
                            
                print(f'El resultado es: {operacion}') #Aquí se imprime el resultado final / Here will be printed the final result
                del operacion, operadores, problema, primeraPosición, operador, numero #Se eliminan variables para liberar espacio / Deletes variables to free up memory

        except:
            continuar = errornum()
            if continuar == False:
                break

#Cuando el usuario escribe algo que no es un número en las operaciones esta función es llamada / This function is called when the user types a non-numerical value
def errornum():
    print('Valor no reconocido como número')
    while power:
        opc = input('¿Desea intentar de nuevo? Y/N >')
        if opc == 'Y' or opc == 'y':
            return True
            break
        elif opc == 'N' or opc == 'n':
            return False
            break
        else:
            print('Valor no reconocido, intente de nuevo')

#Menu principal / Main menu
while power:
    print("Escoja una opción")
    print("1.Suma","\n2.Resta","\n3.Multiplicación","\n4.División","\n5.Libre","\n6.Salir")
    try:
        respuesta=int(input("Opción: "))
        if respuesta == 1:    #Suma / sum operation
            numeros = inputs('operacion') #Llama la función inputs y guarda los valores en 'números' / Calls the 'inputs' function and stores the values in 'números'
            suma = numeros[0] + numeros[1]
            print("La respuesta es: ", suma)  
        elif respuesta == 2:    #Resta / Substract operation
            numeros = inputs('operacion') #Lo mismo que en la linea 49 / Same as the line 49
            resta = numeros[0]-[1]
            print("La respuesta es: ", resta)
        elif respuesta == 3:    #Multiplicación / Multiplication
            numeros = inputs('operacion')
            multi = numeros[0]*numeros[1]
            print("La respuesta es: ", multi)
        elif respuesta == 4:    #División / Divide
            numeros = inputs('operacion')
            divi = numeros[0] / numeros[1]
            print("La respuesta es: ", divi)
        elif respuesta == 5:    libre() #Llama la función 'libre', línea 20 / Calls 'libre' function, line 20
        elif respuesta == 6:    power = False #Apaga el programa / Turns off the program
        else:
            print('Opción incorrecta')
            time.sleep(1)
    except:
        time.sleep(1)

print("""
Gracias por probar mi programa
-Keylor, 2022
""")