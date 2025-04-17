def pregunta_1(HH1: int, MM1: int, SS1: int, HH2: int, MM2: int, SS2: int) -> int:
    """
    Parametros:
        HH1 (int) : Hora primer tramo
        MM1 (int) : Minutos primer tramo
        SS1 (int) : Segundos primer tramo
        HH2 (int) : Hora segundo tramo
        MM2 (int) : Minutos segundo tramo
        SS2 (int) : Segundos segundo tramo
    Retorna:
        int : tiempo total de la carrera en segundos
    """
    suma= (HH1*3600)+(HH2*3600)+(MM1*60)+(MM2*60)+SS1+SS2
    return suma

def pregunta_2(h1: int, m1: int, s1: int, h2: int, m2: int, s2: int) -> str:
    """
    Parametros:
        h1 (int) : hora de la primera hora
        m1 (int) : minuto de la primera hora
        s1 (int) : segundo de la primera hora
        h2 (int) : hora de la segunda hora
        m2 (int) : minuto de la segunda hora
        s2 (int) : segundo de la segunda hora
    Retorna:
        str : el mensaje exactamente igual a lo indicado en el enunciado
    """
    if h1==h2 and m1==m2 and s1==s2:
        return "Las dos horas son iguales"
    elif (h1>h2) or (h1==h2 and m1>m2) or (h1==h2 and m1==m2 and s1>s2):
        return "La segunda hora ocurre primero"
    elif (h1<h2) or (h1==h2 and m1<m2) or (h1==h2 and m1==m2 and s1<s2):
        return "La primera hora ocurre primero"

def pregunta_3(numero: int) -> str:
    """
    Parametros:
        numero (int) : Es el numero de 4 digitos
    Retorna:
        str: el mensaje que dice "Es un numero capicua" o "No es un numero capicua"
    """
    x=numero%10
    xx=(numero//10)%10
    xxx=(numero//10//10)%10
    xiv=(numero//10//10//10)%10

    if(x==xiv and xx==xxx):
        return "Es un numero capicua"
    else:
        return "No es un numero capicua"

def pregunta_4(anio: int) -> str:
    """
    Parametros:
        anio (int) : Es el anio ingresado
    Retorno:
        str : la cadena de texto que dice la era de acuerdo a la tabla
    """
    if 1868<=anio<=1911:
        return "Meiji"
    elif 1912<=anio<=1925:
        return "Taisho"
    elif 1926<=anio<=1988:
        return "Showa"
    elif 1989<=anio<=2018:
        return "Heisei"
    elif anio>=2019:
        return "Reiwa"
    else:
        return "No es el Japon moderno"