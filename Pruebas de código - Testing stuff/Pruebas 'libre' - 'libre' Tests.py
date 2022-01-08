"""
Intenté realizar la función 'libre' sin utilizar 'eval()', aquí están las pruebas
Tried to do the 'libre' function without the 'eval()', here it is the proofs
"""

import operator
from os import replace

power = True
operadores = {
    "+":operator.add, "-":operator.sub, "*": operator.mul, "/": operator.truediv
    }

#inputOperacion = input('>>')
#inputOperador = None

inputOperacion = '1+1'

operacionInt = None

contador = 0
while power:
    try:
        operacionInt.append(inputOperacion[contador])
        contador += 1
        
    except:
        if inputOperacion[contador] == "+":
            operacionInt.append(operator.add)
            contador += 1
            print(operacionInt)

print(operacionInt)