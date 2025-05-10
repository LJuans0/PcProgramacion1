def pregunta_1( mensaje :  str) -> str: 
    """
    Parametros:
        mensaje (str) : Un mensaje en espaniol sin tildes. Puede tener letras mayusculas.
    Retorna:
    	str : el mensaje codificado segun el idioma alienigena.
    """
    niutext=""
    for i in range(len(mensaje)):
        if 'a' or 'A' == mensaje[i]:
            niutext+="4"
        elif 'e' or 'E' == mensaje[i]:
            niutext += "3"
        elif 'i' or 'I' == mensaje[i]:
            niutext += "1"
        elif 'o' or 'O' == mensaje[i]:
            niutext += "0"
        elif 'u' or 'U' == mensaje[i]:
            niutext += "_"
        else:
            niutext += i
    return niutext
print(pregunta_1("Estamos listos para salir"))

def pregunta_2(cadena: str) -> int:
    """
    Parametros:
        cadena (str): la cadena a analizar
    Retorna:
        int: la cantidad de vocales iguales consecutivas
    """
    return 0


def pregunta_3(cad1 : str , cad2 : str) -> bool:
    """
    Parametros:
        cad1 (str) : cadena  
        cad2 (str) : cadena  
    Retorna:
        bool :  True si ambas cadenas son anagramas y False en caso contrario
    """
    return None 

def pregunta_4(palabra: str) -> int:
    """
    Parametros:
        palabra (str):  Palabra que se va a verificar si es palindroma.
    Retorna:
        (int): Si es palindromo devuelve la cantidad de consonantes, -1 en caso contrario.
    """
    return None