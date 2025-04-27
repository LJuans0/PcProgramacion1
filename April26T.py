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
    sumadigitos=0
    encontrados = 0

    while encontrados < cantidad:
        sumadigitos = 0
        cantactual=cant
        while cantactual > 0:
            digito = cantactual % 10
            sumadigitos += digito
            cantactual = cantactual // 10

        if cant%sumadigitos == 0:
            if encontrados == 0:
                harshadnumeros = harshadnumeros + f"{cant}"
            else:
                harshadnumeros = harshadnumeros+f"-{cant}"
            encontrados +=1
        cant += 1
    return harshadnumeros

def pregunta_4(number: int) -> int:
    """
    Hallar la suma de los digitos de factorial de un numero , considerando que cuando el digito es par el valor a sumar es 0 caso contrario se suma el valor digito correspondiente .
    Parametros :
        number (int ): numero ingresado para calcular su factorial
    Retorna :
        int : Retorna un la suma de los digitos del factorial de un numero, pero cuando el digito es par se suma 0
    """
    contadorsito=1
    ultimodigit=0
    digitselector=0
    sumadedigitos=0
    almacenador=1
    while contadorsito <= number:
        almacenador = almacenador*contadorsito
        contadorsito += 1
    while almacenador > 0:
        ultimodigit = almacenador % 10
        if not(ultimodigit%2==0):
            sumadedigitos += ultimodigit
        almacenador = almacenador // 10
    return sumadedigitos
