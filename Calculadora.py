import time
print("Escoja una operación")
print("1.Suma","\n2.Resta","\n3.Multiplicación","\n4.División")

respuesta=int(input("Opción: "))

if respuesta==1:
    numeroUno=int(input("Digita el primer valor: "))
    numeroDos=int(input("Digita el segundo valor: "))
    suma=numeroUno+numeroDos
    print("La respuesta es: ",suma)

if respuesta==2:
    numeroUno=int(input("Digite el primer valor: "))
    numeroDos=int(input("Digite el segundo valor: "))
    resta=numeroUno-numeroDos
    print("La respuesta es: ",resta)

if respuesta==3:
    numeroUno=int(input("Digite el primer valor: "))
    numeroDos=int(input("Digite el segundo valor: "))
    multi=numeroUno*numeroDos
    print("La respuesta es: ",multi)

if respuesta==4:
    numeroUno=int(input("Digite el primer valor: "))
    numeroDos=int(input("Digite el segundo valor: "))
    divi=numeroUno/numeroDos
    print("La respuesta es: ",divi)

time.sleep(1)
print("Facilito el tuto")

