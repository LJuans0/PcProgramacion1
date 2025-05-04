def pregunta_1(filas : int) -> int:
    """
    Contar cuantas casillas negras tiene un tablero cuadrado compuesto por casillas negras y blancas intercaladas, similar al tablero de ajedrez
    Parametros:
        filas (int): El tamaño de filas y columnas del tablero
    Retorna:
        int: La cantidad de casillas negras en el tablero
    """
    otput=filas**2//2
    return otput

def pregunta_2(tamanio: int) -> str:
    """
    Crea un tablero parecido al de ajedrez formado con los caracteres "#" y "0" de acuerdo al tamanio ingresado como parametro
    Parametros:
        tamanio (int): El tamanio del tablero a crear
    Retorna:
        str: Un tablero formado con los caracteres "#" y "0" con el tamanio especificado, si el tamanio es menor que 2 se debe de retornar el texto "No se puede formar un tablero"
    """
    contador=1
    textin=""
    if tamanio<2:
        return "No se puede formar un tablero"
    while contador<=tamanio:
        for i in range(0,tamanio):
            if (i+contador)%2==0:
                textin+="0"
            else:
                textin+="#"
        textin+="\n"

        contador+=1
    return textin

def pregunta_3(numerico: int) -> str:
    """
    Genera un codigo de barras basado en la cantidad de divisores de cada digito del numero ingresado.
    Parametros:
        numerico (int): Numero entero para generar el codigo de barras.
    Retorna:
        str: Una cadena que representa el codigo de barras "|", dependiendo de su cantidad de divisores.
    """
    digitos=numerico
    codigo=""
    divisores=0
    for digito in str(digitos):
        digitor = int(digito)
        for i in range(2,digitor):
            if digitor%i==0:
                divisores+=1
                codigo+="|"
        if divisores==0:
            codigo+=" "
        divisores=0
    return codigo

def pregunta_4(tam: int) -> str:
    """
    Genere un patron de asteriscos "*" en forma de cuadrado hueco
    Parametros:
        tam (int): El tamanio del cuadrado hueco
    Retorna:
        str: Un cuadrado hueco formado con "*" de acuerdo al tamanio ingresado
    """
    cuadrado=""
    columnas=1
    while columnas<=tam:
        if columnas ==1 or columnas==tam:
            for i in range(0, tam):
                cuadrado+="*"

        if 1<columnas<tam:
            cuadrado += "*"
            for i in range(1, tam-1):
                cuadrado += " "
            cuadrado += "*"
        columnas+=1
        cuadrado += "\n"
    return cuadrado
print(pregunta_4(8))