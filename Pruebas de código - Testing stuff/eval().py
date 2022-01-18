operacion = input("""Introduzca la operación a realizar o escriba 'salir' para salir.\n>> """)
operacion = operacion + "$"
operadores = ( "+", "-", "*", "/", "$")

problema = []

numero = ""
for val in operacion:
    if val in operadores:
        problema.append(int(numero))
        problema.append(val)
        numero = ""
    elif val not in operadores:
        numero = numero + val
del numero

operacion = 0
operador = ""
primeraPosición = True
for val in problema:
    if val == '*':
        operador = val
    elif val == '/':
        operador = val
    elif val == '+':
        operador = val
    elif val == '-':
        operador = val
    elif val == '$':
        break
    else:
        if primeraPosición:
            operacion = val
            primeraPosición = False 
        else:
            if operador == '*':
                operacion = operacion * val
            elif operador == '/':
                operacion = operacion / val
            elif operador == '+':
                operacion = operacion + val
            elif operador == '-':
                operacion = operacion - val

print(operacion)



"""
numeros = []

for val in problemaLiteral:
    numero = int(val)
    numeros.append(numero)
"""
