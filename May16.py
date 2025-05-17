from contextlib import nullcontext


def pregunta_1(lista: list) -> list:
    """
    Parametros:
        lista (list) : una lista de numeros enteros
    Retorna:
        list : la lista con el mayor valor al inicio
    """
    maxvalue=max(lista)
    listaaretronar=[]
    listaaretronar.append(maxvalue)
    for i in lista:
        if i!=maxvalue:
            listaaretronar.append(i)
    return listaaretronar

def pregunta_2(categorias: list[str], puntuaciones: list[int]) -> str:
    """
    Parametros:
        categorias (list[str]): La lista de nombres de categorias, los cuales son Frescos, Despensa, Mascotas y Bebidas.
        puntaciones (list[int]): La lista de puntaciones de cada categoria, entre los valores de 0 a 20.
    Retorna:
        str: El nombre de la categoria con la puntuacion mas alta y mas baja con formato categoriaMax_categoriaMin
    """
    maximo=max(puntuaciones)
    minimo=min(puntuaciones)
    maxcat=""
    mincat=""
    contador=0
    for i in range(len(puntuaciones)):
        if puntuaciones[i]==maximo:
            maxcat=categorias[i]
        elif puntuaciones[i]==minimo:
            mincat=categorias[i]
    return f"{maxcat}_{mincat}"

def pregunta_3(polinomio: list, x: float) -> float:
    """
    Parametros:
        polinomio (list): Lista que representa el polinomio, donde el
            primer elemento es el grado máximo y los elementos 
            restantes son los coeficientes en orden ascendente.
        x (float): Número real en el que se evaluará el polinomio.

    Retorna:
        float: Valor del polinomio evaluado en x.
    """
    gradomax=polinomio[0]
    calc=0
    listaatrabajar=polinomio[gradomax+1:0:-1]
    contexp=gradomax
    for i in listaatrabajar:
        calc+=i*(x**contexp)
        contexp-=1
    return round(calc,3)
def pregunta_4(posiciones: list[int]) -> list[int]:
    """
    Parametros:
        posiciones (list[int]): Lista de posiciones con los numeros que deben aparecer.

    Retorno:
        list[int]: Lista extendida con ceros donde no haya datos y numeros donde corresponda.
    """

    listafinal=[]
    unicas = []
    for q in posiciones:
        if q not in unicas:
            unicas.append(q)

    for a in range(max(unicas)+1):
        listafinal.append(0)

    for q in unicas:
        listafinal[q] = q

    return listafinal