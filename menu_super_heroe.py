from desafio_stark_1 import *
from data_stark import lista_personajes
from os import system
import time
menu_de_opciones = ["^^^^^^^^^^^^^Menu de opciones^^^^^^^^^^^\n"
                     "1 - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M\n"
                       "2 - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe degénero F\n"
                       "3 -C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n"
                       "4 - Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n"
                       "5- Recorrer la lista y determinar cuál es el superhéroe más bajo de género M\n"
                       "6- Recorrer la lista y determinar cuál es el superhéroe más bajo de género F\n"
                       "7- Recorrer la lista y determinar la altura promedio de los superhéroes de género M\n"
                       "8-Recorrer la lista y determinar la altura promedio de los superhéroes de género F\n"
                       "9-Determinar cuántos superhéroes tienen cada tipo de color de ojos\n"
                       "10-Determinar cuántos superhéroes tienen cada tipo de color de pelo\n"
                       "11-Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’\n"
                       "12-salir"]

def mostrar_menu():
    system("cls")
    for opciones in menu_de_opciones:
        print(opciones)

system("cls")

seguir = True
while seguir==True:
    mostrar_menu()

    respuesta = input("ingrese una opciones por fa")
    match respuesta:
        case "1":
            mostrar_nombre_heroe_masculino(lista_personajes)
        case "2":
            mostrar_nombre_heroe_femenino(lista_personajes)
        case "3":
            mostrar_super_heroe_mas_alto(lista_personajes)
        case "4":
            mostrar_super_heroina_mas_alta(lista_personajes)
        case "5":
            mostrar_super_heroe_mas_bajo(lista_personajes)
        case"6":
            mostrar_heroina_mas_baja(lista_personajes)
        case "7":
            altura_promedio_heroe(lista_personajes)
        case "8":
            altura_promedio_heroina(lista_personajes)
        case "9":
            determinar_color_de_ojos(lista_personajes)
        case "10":
            determinar_color_de_pèlo(lista_personajes)
        case "11":
            determinar_tipo_de_inteligencia(lista_personajes)
        case "12":
            seguir = False
    time.sleep(2)  


