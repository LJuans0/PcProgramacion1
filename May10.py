def pregunta_1( mensaje :  str) -> str: 
    """
    Parametros:
        mensaje (str) : Un mensaje en espaniol sin tildes. Puede tener letras mayusculas.
    Retorna:
    	str : el mensaje codificado segun el idioma alienigena.
    """
    niutext=""
    for i in range(len(mensaje)):
        if  mensaje[i]=='A' or mensaje[i] == 'a':
            niutext += '4'
        elif mensaje[i]=='E' or mensaje[i] == 'e':
            niutext += '3'
        elif mensaje[i]=='I' or mensaje[i] == 'i':
            niutext += '1'
        elif mensaje[i]=='O' or mensaje[i] == 'o':
            niutext += '0'
        elif mensaje[i]=='U' or mensaje[i] == 'u':
            niutext += '_'
        else:
            niutext += mensaje[i]
    return niutext

def pregunta_2(cadena: str) -> int:
    """
    Parametros:
        cadena (str): la cadena a analizar
    Retorna:
        int: la cantidad de vocales iguales consecutivas
    """
    cuentapares=0
    ultimavocal=""
    for i in range(len(cadena) - 1):
        if cadena[i] in 'aeiou' and cadena[i] == cadena[i + 1]:
            cuentapares += 1
    return cuentapares

def pregunta_3(cad1 : str , cad2 : str) -> bool:
    """
    Parametros:
        cad1 (str) : cadena  
        cad2 (str) : cadena  
    Retorna:
        bool :  True si ambas cadenas son anagramas y False en caso contrario
    """
    cad11=cad1.replace(" ","").lower()
    cad22=cad2.replace(" ", "").lower()

    for lettar in cad1:
        if cad1.count(lettar)!=cad2.count(lettar):
            return False
    return True


def pregunta_4(palabra: str) -> int:
    """
    Parametros:
        palabra (str):  Palabra que se va a verificar si es palindroma.
    Retorna:
        (int): Si es palindromo devuelve la cantidad de consonantes, -1 en caso contrario.
    """
    textasocopia=palabra.lower()
    contadorsoteperrote=0
    textasoinv=textasocopia[::-1]

    if textasocopia==textasoinv:
        for i in textasocopia:
            if i not in 'aeiou ':
                contadorsoteperrote += 1
        return contadorsoteperrote
    else:
        return -1
