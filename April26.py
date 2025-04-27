#historial de abajo para arriba
#problema de gorinkis
gorinkinum=int(input("Numero de gorinkis-->"))
while 3>gorinkinum:
    print("Input invalido")
    gorinkinum = int(input("Numero de gorinkis-->"))

contador=1
contadorero=1
sumador=0
while contador<=gorinkinum:
    while contadorero<=5:
        presion = int(input(f"Presión {contadorero} sistólica del gornki {contador}:"))
        contadorero+=1
        sumador += presion
        promedio = sumador / 5
    if 90<=promedio<=130:
        print(f"El gorinki {contador} no es hipertenso, puesto que su promedio es:{promedio}")
    else:
        print(f"El gorinki {contador} es hipertenso, puesto que su promedio es:{promedio}")

    contador+=1
    contadorero=1
    sumador=0

#programa que lea como dato un número entero "n", cuyo valor puede ser desde 1 al 9 y haga las tablas del 1 al 10 dependiendo
n=int(input("Numero desde 1 a 9-->"))
while 1>=n>=9:
    print("Input invalido")
    n = int(input("Numero desde 1 a 9-->"))
count=1
counter2=1
if n%2==0:
    counter2 = 2
    while counter2 <= n:
        while count <= 10:
            print(counter2, "x", count, "=", count * counter2)
            count += 1
        counter2 += 2
        count = 1
        print()
else:
    counter2 = 1
    while counter2 <= n:
        while count <= 10:
            print(counter2, "x", count, "=", count * counter2)
            count += 1
        counter2 += 2
        count = 1
        print()