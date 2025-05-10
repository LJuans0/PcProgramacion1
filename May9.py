def pregunta_1(num1: int, num2: int, multiplo: int) ->int:
    """
    Retorna la cantidad de sumas de x y de y que sean multiplos del parametro multiplo
    Parametros:
        num1 (int) : representa el menor valor de x y de y
        num2 (int) : representa el mayor valor de x y de y
        multiplo (int) : representa el multiplo a evaluar
    Retorna:
        int : la cantidad de multiplos que hay
    """
    contador=0
    for x in range(num1,num2+1):
        suma = 0
        for y in range(num1,num2+1):
            suma=x + y
            if suma%multiplo==0:
                contador+=1
    return contador

def pregunta_2(n : int) -> str: 
    """
    Parametros:
        n (int) :  numero entero
    Retorna:
        str : cadena de numeros que no tienen el digito 2
    """
    texto=""
    for num in range(1,n+1):
        if not(num==2):
            texto += f"{num} "

    return texto

def pregunta_3(frase : str) -> tuple[int,int]:
    """
    Parametros:
        frase (string) : Una oracion o frase donde cada palabra esta separada por espacios
    Retorna:
        Tuple[int,int] : El primer valor es la cantidad de palabras en la frase. El segundo valor es la cantidad de letras en la frase.
    """
    palabras=1
    letras=0
    for i in frase:
        if i==" ":
            palabras+=1
        else:
            letras+=1
    return palabras,letras

def pregunta_4(n : int, nota_inicial : int) -> tuple[int, float]:
    """
    Parametros:
        n (int) : Cantidad total de notas a evaluar
        nota_inicial (int) : Valor de la primera nota
    Retorna:
        Tuple[int, float] : El primer valor es la cantidad de notas mayores o iguales a 14. 
                            El segundo valor es el promedio de todas las notas generadas, redondeado a 2 decimales.
    """
    contadordenotas=0

    sumadorero=0
    for i in range(nota_inicial,nota_inicial+n):
        sumadorero+=i
        if i>=14:
            contadordenotas+=1
    promediador=sumadorero/n
    return contadordenotas,promediador