def pregunta_1(number_init: int, step: int) -> int:
    """
    Hallar la cantidad de numeros abundantes de los 5 numeros generados
    partir del n inicial .
    Parametros :
        number_init ( int): El numero inicial utilizado para generar los 5 numeros
        step (int ): Valor de incremento o disminucion
    Retorna :
        int : Retorna la cantidad de numeros abundantes
    """
    #hallar cuantos numeros divisibles hay para 28
    cont=1
    abundante=0
    while cont<=5:
        sumatoria=0
        div = 1
        while div < number_init:
            if number_init % div == 0:
                sumatoria += div
            div += 1
        if sumatoria > number_init:
            abundante += 1
        number_init += step
        cont += 1
    return abundante


def pregunta_2(number_init: int, step: int) -> int:
    """
    Hallar la cantidad de numeros de Armstrong de los 10 numeros
    generados a partir del n inicial .
    Parametros :
        number_init ( int): El numero inicial utilizado para generar los 10 numeros
        step (int ): Valor de incremento o disminucion
    Retorna :
        int : Retorna la cantidad de numeros de Armstrong
    """
    caunt=1
    armstrongunumbers=0
    longdn=len(str(number_init))

    while caunt<=10:
        longdn = len(str(number_init))
        x = number_init % 10
        xx = (number_init // 10) % 10
        xxx = (number_init // 10 // 10) % 10
        xxxx = (number_init // 10 // 10 // 10) % 10
        if (x ** longdn + xx ** longdn + xxx ** longdn + xxxx ** longdn) == number_init:
            armstrongunumbers += 1
        number_init += step
        caunt += 1

    return armstrongunumbers

def pregunta_3(cantidad: int) -> str:
    """
    Hallar los primeros n numeros de Harshad .
    Parametros :
      cantidad (int): Cantidad de numeros , donde es mayor e igual a 1
    Retorna :
        str : Retorna un str de los primeros n numeros Harshad
    """
    cant = 1
    harshadnumeros=""
    while cant <= cantidad:
        xi = cant % 10
        xii = (cant // 10) % 10
        xiii = (cant // 10 // 10) % 10
        xiv = (cant // 10 // 10 // 10) % 10
        sumadigitos = xi+xii+xiii+xiv
        if cant%sumadigitos == 0:
            harshadnumeros = harshadnumeros+f"-{cant}"
        cant += 1

    return harshadnumeros
pregunta_3(2)

def pregunta_4(number: int) -> int:
    """
    Hallar la suma de los digitos de factorial de un numero , considerando que cuando el digito es par el valor a sumar es 0 caso contrario se suma el valor digito correspondiente .
    Parametros :
        number (int ): numero ingresado para calcular su factorial
    Retorna :
        int : Retorna un la suma de los digitos del factorial de un numero, pero cuando el digito es par se suma 0
    """

    return -1
