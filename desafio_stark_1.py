from data_stark import lista_personajes
#A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
#género M
def mostrar_nombre_heroe_masculino(lista_personajes):
    for heroe in (lista_personajes):
        if heroe["genero"] == "M":
            print(heroe["nombre"])

#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
#género F
def mostrar_nombre_heroe_femenino(lista_personajes):
    for heroe in (lista_personajes):
        if heroe["genero"] == "F":
            print(heroe["nombre"])

#C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
def mostrar_super_heroe_mas_alto(lista_personajes):
    heroe_mas_altura = None  
    nombre_heroe_mas_alto = None
    for heroe in lista_personajes:
        if heroe['genero'] == "M":
            if heroe_mas_altura is None or float(heroe['altura']) > heroe_mas_altura:
                heroe_mas_altura = float(heroe['altura'])
                nombre_heroe_mas_alto = heroe['nombre']
    print(f"el hereo mas alto es : {nombre_heroe_mas_alto} y su altura es de {heroe_mas_altura}")
            
#D. Recorrer la lista y determinar cuál es el superhéroe más alto de género Fç
def mostrar_super_heroina_mas_alta(lista_personajes):
    heroina_mas_altura = None  
    nombre_heroina_mas_alta = None
    for heroe in lista_personajes:
        if heroe['genero'] == "F":
            if heroina_mas_altura is None or float(heroe['altura']) > heroina_mas_altura:
                heroina_mas_altura = float(heroe['altura'])
                nombre_heroina_mas_alta = heroe['nombre']
    print(f"la heroina mas alta es : {nombre_heroina_mas_alta} y su altura es de : {heroina_mas_altura}")
            
#E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
def mostrar_super_heroe_mas_bajo(lista_personajes):
    heroe_mas_bajo = None
    nombre_heroe_mas_bajo = None
    for heroe in lista_personajes:
        if heroe['genero'] == "M":
            if heroe_mas_bajo is None or float(heroe['altura']) < heroe_mas_bajo:
                heroe_mas_bajo = float(heroe['altura'])
                nombre_heroe_mas_bajo = heroe['nombre']
    print(f"el heroe mas bajo es {nombre_heroe_mas_bajo} y su altura es de {heroe_mas_bajo}")


#F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
def mostrar_heroina_mas_baja(lista_personajes):
    heroina_mas_bajo = None
    nombre_heroina_mas_bajo = None
    for heroe in lista_personajes:
        if heroe['genero'] == "F":
            if heroina_mas_bajo is None or float(heroe['altura']) < heroina_mas_bajo:
                heroina_mas_bajo = float(heroe['altura'])
                nombre_heroina_mas_bajo = heroe['nombre']
    print(f"el nombre de la heroina mas baja es {nombre_heroina_mas_bajo} y su altura es de {heroina_mas_bajo}")


#G. Recorrer la lista y determinar la altura promedio de los superhéroes de
#género M
def altura_promedio_heroe(lista_personajes):
    suma_alturas_masculinos = 0
    contador_heroe_masculino = 0
    for heroe in lista_personajes:
        if heroe['genero'] == "M":
            suma_alturas_masculinos += float(heroe['altura'])
            contador_heroe_masculino += 1
            promedio_alturas_masculinos = (suma_alturas_masculinos/contador_heroe_masculino)
    print(f"el promedio de las alturas de heroes masculinos es : {promedio_alturas_masculinos}")

#H. Recorrer la lista y determinar la altura promedio de los superhéroes de
#género F
def altura_promedio_heroina(lista_personajes):
    suma_alturas_femeninas = 0
    contador_heroina_femenina = 0
    for heroe in lista_personajes:
        if heroe['genero'] == "F":
            suma_alturas_femeninas += float(heroe['altura'])
            contador_heroina_femenina += 1
            promedio_alturas_femeninas = (suma_alturas_femeninas/contador_heroina_femenina)
    print(f"el promedio de las alturas de heroes femeninos es : {promedio_alturas_femeninas}")
#J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
def determinar_color_de_ojos(lista_personajes):
    lista_color_ojos = []
    conteo_color_ojos = {}
    for heroe in range(len(lista_personajes)):
        lista_color_ojos.append(lista_personajes[heroe]["color_ojos"])
        
    lista_color_ojos_seteada = set(lista_color_ojos)

    for heroe in lista_personajes:
        color_ojos = heroe["color_ojos"]
        if color_ojos in conteo_color_ojos:
            conteo_color_ojos[color_ojos] += 1
        else:
            conteo_color_ojos[color_ojos] = 1

    # Imprimir el conteo de superhéroes por color de ojos
    for color, cantidad in conteo_color_ojos.items():
        print(f"Color de ojos: {color}, Cantidad de superhéroes: {cantidad}")
#print(f"El color de los ojos de los superheroes en genreal son :{lista_color_ojos_seteada}")
#K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
def determinar_color_de_pèlo(lista_personajes):
    lista_color_pelo = []
    for heroe in range(len(lista_personajes)):
        lista_color_pelo.append(lista_personajes[heroe]["color_pelo"])

    lista_color_pelo_seteada = set(lista_color_pelo)
    conteo_color_pelo = {}
    for heroe in lista_personajes:
        color_pelo = heroe["color_pelo"]
        if color_pelo in conteo_color_pelo:
            conteo_color_pelo[color_pelo] += 1
        else:
            conteo_color_pelo[color_pelo] = 1

    # Imprime el color de pelo y su cantidad
    for color, cantidad in conteo_color_pelo.items():
        print(f"Color del pelo: {color}, Cantidad de superhéroes con este pelo: {cantidad}")
#L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
#no tener, Inicializarlo con ‘No Tiene’).
def determinar_tipo_de_inteligencia(lista_personajes):
    lista_tipos_de_inteligencia = []
    for heroe in lista_personajes:
        tipo_inteligencia = heroe.get("inteligencia", "No Tiene")
        lista_tipos_de_inteligencia.append(tipo_inteligencia)

    contador_inteligencia = {tipo: 0 for tipo in lista_tipos_de_inteligencia}

    for heroe in lista_personajes:
        tipo_inteligencia = heroe.get("inteligencia", "No Tiene")
        contador_inteligencia[tipo_inteligencia] += 1

    # Imprimir los resultados
    for tipo, cantidad in contador_inteligencia.items():
        print(f"Superhéroes con tipo de inteligencia '{tipo}': {cantidad}")













