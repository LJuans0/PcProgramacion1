import math
def pregunta_1(numerico: int) -> str:
    """
    Genera un codigo de barras basado en la cantidad de 
    divisores de cada digito del numero ingresado.
    
    Parametros:
    	numerico (int): Numero entero para generar el codigo de barras.
    Retorna:
    	str: Una cadena que representa el codigo de barras '|'
            dependiendo de su cantidad de divisores.
    """
    waaaaa = str(numerico)
    zaaaaa = ""
    for aaaa in waaaaa:
        aaaa = int(aaaa)
        cont = 0
        for j in range(2, aaaa):
            if aaaa % j == 0:
                cont += 1
        if cont == 0:
            zaaaaa += " "
        else:
            zaaaaa += "|" * cont
    return zaaaaa


def pregunta_2(radio: float, altura: float) -> float:
    return area(radio,altura)*volume(radio,altura)

def area(radio: float, altura: float) -> float:
    return  (2 * math.pi * radio * altura) + (2 * math.pi * (radio**2))

def volume(radio: float, altura: float) -> float:
    return math.pi * (radio**2) * altura


def pregunta_3(cad:str)->float:
    minus = 0
    mayus = 0
    digit = 0
    for i in cad:
        if i.isupper():
            mayus+=1
        if i.islower():
            minus+=1
        if i.isnumeric():
            digit+=1
    longitud = len(cad)
    if (mayus>=2) and (minus>=2) and (digit>=2) and (longitud>=8):
        fortaleza = min(minus,mayus)*longitud/digit
    else:
        fortaleza = 0
    return round(fortaleza,2)


def pregunta_4(vector: list) -> float:
    suma = 0
    for i in vector:
        suma+=i**2
    modulo = suma**0.5
    return round(modulo,3)