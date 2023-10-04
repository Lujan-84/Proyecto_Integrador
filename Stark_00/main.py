import os
from data_stark import lista_personajes
from funciones import *


lista = normalizar_datos(lista_personajes)
while True:
    os.system("cls")
    
    imprimir_menu()
    opcion = input("Ingrese la opción deseada: ")
    
    if opcion == "1":
        mostrar_lista_nombres_personajes(lista)
        
    elif opcion == "2":
        mostrar_lista_nombres_y_valor(lista,"altura")
        
    elif opcion == "3":
        maxima_altura = maximo_segun_clave(lista,"altura")
        imprimir_indicador(maxima_altura,"Superhéroe más bajo:")
        
        minima_altura = minimo_segun_clave(lista,"altura")
        imprimir_indicador(minima_altura,"Superhéroe más alto:")
        
    elif opcion == "4":
        maximo_peso = maximo_segun_clave(lista,"peso")
        imprimir_indicador(maximo_peso,"Superhéroe más pesado:")
        
        minimo_peso = minimo_segun_clave(lista,"peso")
        imprimir_indicador(minimo_peso,"Superhéroe menos pesado:")
        
    elif opcion == "5":
        personajes_masculinos = filtrar_lista_segun_valor(lista,"genero","M")
        imprimir_indicador(personajes_masculinos,"Nombres de superhéroes de género M:")
        
    elif opcion == "6":
        personajes_femeninos = filtrar_lista_segun_valor(lista,"genero","F")
        imprimir_indicador(personajes_femeninos,"Nombres de superhéroes de género F:")
        
    elif opcion == "7":
        personajes_masculinos = filtrar_lista_segun_valor(lista,"genero","M")
        mas_alto_masculino = maximo_segun_clave(personajes_masculinos,"altura")
        imprimir_indicador(mas_alto_masculino,"Superhéroe más alto de género M:")
        
        personajes_femeninos = filtrar_lista_segun_valor(lista,"genero","F")
        mas_alto_femenino = maximo_segun_clave(personajes_femeninos,"altura")
        imprimir_indicador(mas_alto_femenino,"Superhéroe más alto de género F:")
        
        mas_bajo_masculino = minimo_segun_clave(personajes_masculinos,"altura")
        imprimir_indicador(mas_bajo_masculino,"Superhéroe más bajo de género M:")
        
        mas_bajo_femenino = minimo_segun_clave(personajes_femeninos,"altura")
        imprimir_indicador(mas_bajo_femenino,"Superhéroe más bajo de género F:")
        
        altura_promedio_masculinos = calcular_promedio_clave(personajes_masculinos,"altura")
        print(f"Altura promedio de superhéroes de género M: {altura_promedio_masculinos}")
        
        altura_promedio_femeninos = calcular_promedio_clave(personajes_femeninos,"altura")
        print(f"Altura promedio de superhéroes de género F: {altura_promedio_femeninos}")
        
    elif opcion == "8":
        cantidad_personajes_segun_color_ojos = contar_personajes_segun_valor(lista_personajes,"color_ojos")
        mostrar_diccionario(cantidad_personajes_segun_color_ojos)
        
    elif opcion == "9":
        cantidad_personajes_segun_color_pelo = contar_personajes_segun_valor(lista_personajes,"color_pelo")
        mostrar_diccionario(cantidad_personajes_segun_color_pelo)
        
    elif opcion == "10":
        cantidad_personajes_segun_inteligencia = contar_personajes_segun_valor(lista_personajes,"inteligencia")
        mostrar_diccionario(cantidad_personajes_segun_inteligencia)
        
    elif opcion == "11":
        listar_personajes_segun_valor(lista_personajes,"color_ojos")
        
    elif opcion == "12":
        listar_personajes_segun_valor(lista_personajes,"color_pelo")
        
    elif opcion == "13":
        listar_personajes_segun_valor(lista_personajes,"inteligencia")
    
    elif opcion == "14":
        break
    
    else:
        print("Ingrese una opción válida")
        
    os.system("pause")


    


