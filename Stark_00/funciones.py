from data_stark import lista_personajes

def imprimir_menu():
    print("1/Imprimir nombre de cada superhéroe\n2/Imprimir nombre y altura de cada superhéroe\n3/Informar superhéroe más alto y más bajo\n4/Informar superhéroe más y menos pesado\n5/Nombre de superhéroes de género M\n6/Nombre de superhéroes de género F\n7/Imprimir estadísticas\n8/Determinar cuántos superhéroes tienen cada tipo de color de ojos\n9/Determinar cuántos superhéroes tienen cada tipo de color de pelo\n10/Determinar cuántos superhéroes tienen cada tipo de inteligencia\n11/Listar todos los superhéroes agrupados por color de ojos\n12/Listar todos los superhéroes agrupados por color de pelo\n13/Listar todos los superhéroes agrupados por tipo de inteligencia\n14/Salir")
    
def modificar_diccionario(personaje:dict,altura:float,peso:float,fuerza:int)->dict:
    """Modifica en el diccionario original los valores guardados como strings en valores del tipo int o float dependiendo del caso

    Args:
        personaje (dict): diccionario original a modificar
        altura (float): dato del tipo float, sustituirá al dato de tipo str
        peso (float): dato del tipo float, sustituirá al dato de tipo str
        fuerza (int): dato del tipo int, sustituirá al dato de tipo str

    Returns:
        dict: diccionario modificado con los datos normalizados
    """
    personaje["altura"] = altura
    personaje["peso"] = peso
    personaje["fuerza"] = fuerza
    
    return personaje

def set_altura(str_altura:str)->float:
    """Recibe el dato altura de tipo str, lo setea a tipo float y lo devuelve

    Args:
        str_altura (str): dato altura de tipo str

    Returns:
        float: dato altura de tipo float
    """
    return round(float(str_altura),2)

def set_peso(str_peso:str)->float:
    """Recibe el dato altura de peso str, lo setea a tipo float y lo devuelve

    Args:
        str_peso (str): dato peso de tipo str

    Returns:
        float: dato peso de tipo float
    """
    return round(float(str_peso))

def set_fuerza(str_fuerza:str)->int:
    """Recibe el dato altura de fuerza str, lo setea a tipo int y lo devuelve

    Args:
        str_fuerza (str): dato fuerza de tipo str

    Returns:
        int: dato fuerza de tipo int
    """
    return int(str_fuerza)


def setear_datos(personaje:dict)->dict:
    """Setea los datos a modificar en el diccionario original llamando a la funcion set para cada tipo de dato,
       luego llama a la funcion modificar diccionario y devuelve el diccionario con los datos seteados

    Args:
        personaje (dict): diccionario original a modificar

    Returns:
        dict: diccionario modificadico con los datos normalizados
    """
    altura = set_altura(personaje["altura"])
    peso = set_peso(personaje["peso"])
    fuerza = set_fuerza(personaje["fuerza"])
    
    return modificar_diccionario(personaje,altura,peso,fuerza)

def normalizar_datos(lista:list)->list:
    """Recibe una lista de diccionarios, la recorre y modifica cada diccionario con los datos a seteados,
       guarda cada diccionario modificado en una nueva lista y devuelve la misma.
       
    Args:
        lista ():Lista de diccionarios a normalizar

    Returns:
        list: Lista de diccionarios normalizados
    """
    lista_personajes_normalizados = []
    for personaje in lista:
        personaje = setear_datos(personaje)
        lista_personajes_normalizados.append(personaje)
    return lista_personajes_normalizados

def mostrar_nombre_personaje(personaje:dict):
    """Recibe un diccionario e imprime el nombre del personaje

    Args:
        personaje (dict): diccionario con los datos del personaje
    """
    nombre = personaje.get("nombre")
    print(f"{nombre:<20}")
    
def mostrar_nombre_y_valor(personaje:dict,key:str):
    """Recibe un diccionario y una clave, imprime por consola el nombre del personaje y el dato solicitado

    Args:
        personaje (dict): diccionario con los datos del personaje
        key (str): clave del dato que se quiere imprimir
    """
    key_value = personaje.get(key)
    mostrar_nombre_personaje(personaje)
    print(f"{key.capitalize():<10}: {key_value:>20}")
    

def mostrar_lista_nombres_personajes(lista:list):
    """Recibe una lista de diccionarios, la recorre e imprime el nombre de cada personaje en la lista

    Args:
        lista (list): Lista con los personajes a listar
    """
    for personaje in lista:
        mostrar_nombre_personaje(personaje)
        
def mostrar_lista_nombres_y_valor(lista:list,key:str):
    """Recibe una lista de diccionarios y una clave, recorre la lista e imprime el nombre de cada personaje en la lista y el 
        valor solicitado

    Args:
        lista (list): Lista con los personajes a listar
        key (str): Clave del dato a mostrar además del nombre
    """
    for personaje in lista:
        mostrar_nombre_y_valor(personaje,key)
        
    
def maximo_segun_clave(lista:list,key:str)->list:
    """Recibe una lista de diccionarios y una clave, determina el maximo valor en la lista en relación a
       la clave solicitada, devuelve una lista con los personajes que tengan el máximo valor encontrado.

    Args:
        lista (list): Lista con personajes a analizar
        key (str): Clave en relación a la cuál se desea determinar el máximo

    Returns:
        list: Lista con los personajes que tengan el máximo valor de la clave recibida
    """
    maximo = lista[0][key]
    for i in range(len(lista)):
        valor = lista[i][key]
        if valor > maximo:
            maximo = lista[i][key]
    
    lista_maximos = []
    for i in range(len(lista)):
        personaje = lista[i]
        valor = lista[i][key]  
        if valor == maximo:
            lista_maximos.append(personaje)
    return lista_maximos      

def minimo_segun_clave(lista:list,key:str)->list:
    """Recibe una lista de diccionarios y una clave, determina el mínimo valor en la lista en relación a
       la clave solicitada, devuelve una lista con los personajes que tengan el mínimo valor encontrado.

    Args:
        lista (list): Lista con personajes a analizar
        key (str): Clave en relación a la cuál se desea determinar el mínimo

    Returns:
        list: Lista con los personajes que tengan el míniimo valor de la clave recibida
    """
    minimo = lista[0][key]
    for i in range(len(lista)):
        valor = lista[i][key]
        if valor < minimo:
            minimo = lista[i][key]
    
    lista_minimos = []
    for i in range(len(lista)):
        personaje = lista[i]
        valor = lista[i][key]  
        if valor == minimo:
            lista_minimos.append(personaje)
    return lista_minimos          
                  
def sumar_valor_especificado(lista:list,key:str)->float:
    """Recibe una lista de diccionarios y una clave, recorre la lista sumando todos los valores correspondientes a la clave. Devuelve la suma total

    Args:
        lista (list): Lista de diccionarios a analizar
        key (str): Clave de la cuál se quiere obtener la suma de sus valores

    Returns:
        float: Suma total de los valores en los diccionarios con la clave solicitada
    """
    acumulador = 0
    for personaje in lista:
        acumulador += personaje.get(key)
    return acumulador  

def calcular_promedio_clave(lista:list,key:str)->float:
    """Recibe una lista de diccionarios y una clave en relacion a la cuál hallar el promedio, llama a la funcion sumar_valor_especificado, recibe la suma total y la divide por la cantidad de elementos en la lista. Devuelve el promedio

    Args:
        lista (list): Lista sobre la cuál calcular el promedio
        key (str): Clave de los valores a promediar

    Returns:
        float: el promedio calculado de tipo float, con un sólo número decimal
    """
    promedio = round(sumar_valor_especificado(lista,key) / len(lista),1)  
    return promedio  
       
    
def filtrar_lista_segun_valor(lista:list,key:str,key_value:str)->list:
    """Recibe una lista de diccionarios, una clave y un valor relacionado a esa clave que es el que va a filtrar.
       Recorre la lista recibida y agrega a una nueva lista los diccionarios que contengan dicho valor. Devuelve la nueva lista filtrada

    Args:
        lista (list): Lista original a filtrar
        key (str): Clave de los valores a analizar
        key_value (str): Valor que queremos encontrar los diccionarios de la lista

    Returns:
        list: lista con todos los diccionarios que contengan el valor solicitado
    """
    lista_filtrada = []
    for item in lista:
        if item[key] == key_value:
            lista_filtrada.append(item)
    return lista_filtrada

def imprimir_indicador(lista:list,texto:str):
    """Recibe una lista y un texto que representa el encabezado de la lista a mostrar, imprime el título y luego los nombres en la lista

    Args:
        lista (list): Lista de diccionarios a mostrar
        texto (str): Encabezado o título del listado
    """
    print(texto)
    mostrar_lista_nombres_personajes(lista)
       
def crear_lista_valores(lista:list,clave:str)->list:
    """Recibe una lista de diccionarios y una clave, recorre la lista y guarda los valores relacionados a la clave recibida en una nueva lista. Si la clave no tiene valor en alguno de los diccionarios, el mismo se modifica inicializando la clave con el str: 'No tiene'.
    Devuelve la lista de valores asociada a la clave.

    Args:
        lista (list): lista a analizar
        clave (str): clave de los valores a guardar
    Returns:
        list: Lista con los valores solicitados
    """
    lista_valores = []
    for item in lista:
        if lista_valores.count(item[clave]) == 0 and item[clave] != "":
            lista_valores.append(item[clave])
        elif item[clave] == "":
            item = inicializar_clave_vacía(item,clave)
            if lista_valores.count(item[clave]) == 0:
                lista_valores.append(item[clave])
    return lista_valores

def contar_personajes_segun_valor(lista:list,clave:str)->dict:
    """Recibe una lista de diccionarios y una clave, llama a la funcion crear_lista_valores y guarda la lista con los valores relacionados a la clave recibida. Recorre la lista de valores generada utilizando cada valor de la misma para filtrar la lista recibida según dicho valor. Luego agrega a un diccionario el valor analizado y la cantidad de diccionarios/personajes que contienen el valor solicitado. Devuelve un diccionario con cada valor y la cantidad de ocurrencias del mismo. 

    Args:
        lista (list): Lista recibida a ser analizada
        clave (str): Clave según la cuál contar la ocurrencia de sus valores

    Returns:
        dict: Diccionario con cada valor y la cantidad de ocurrencias del mismo
    """
    diccionario = {}
    lista_valores = crear_lista_valores(lista,clave)
    for valor in lista_valores:
        lista_filtrada =filtrar_lista_segun_valor(lista,clave,valor)
        diccionario[valor] = len(lista_filtrada)
    return diccionario

def inicializar_clave_vacía(diccionario:dict,clave:str)->dict:
    """Recibe un diccionario y una clave cuyo valor asociado está vacío e inicializa dicho valor con el str 'No tiene'.
       Devuelve el diccionario modificado
       
    Args:
        diccionario (dict): Diccionario a modificar
        clave (str): Clave asociada al valor vacío

    Returns:
        dict: Diccionario con el valor inicializado
    """
    diccionario[clave] = "No tiene"
    return diccionario

def listar_personajes_segun_valor(lista:list,clave:str):
    """Recibe una lista de diccionarios y una clave, crea una lista de valores asociada a la clave recibida,
       recorre la lista de valores y filtra la lista recibida según el valor de la iteración. Imprime los nombres de todos los personajes que tienen ese valor.

    Args:
        lista (list): Lista de diccionarios a analizar
        clave (str): Clave asociada a los valores a listar
    """
    lista_valores = crear_lista_valores(lista,clave)
    for valor in lista_valores:
        lista_filtrada = filtrar_lista_segun_valor(lista,clave,valor)
        print(f"----------{valor.capitalize():^15}---------")
        mostrar_lista_nombres_personajes(lista_filtrada)
        print("\n")
        
def mostrar_diccionario(diccionario:dict):
    """Recibe un diccionario lo recorre e imprime sus claves y valores

    Args:
        diccionario (dict): diccionario a imprimir
    """
    for key,value in diccionario.items():
        print(f"{key.capitalize():<25}{value:>10}")
        