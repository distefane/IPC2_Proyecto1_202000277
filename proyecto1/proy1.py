from os import system
from lista_simplee import ListaGanador
from lista_simplee import ListaJugador
from lista_simplee import ListaRegalos
from MatrizDispersa import MatrizDispersa

def leer_xml(ruta_xml, ruta2_xml):
    import xml.etree.ElementTree as ET
    try:
        #variable para cada jugador 
        i = 1
        #variables para sumar puntos
        global puntos
        #lectura de ruta_xml (jugadores)
        ruta_xml = ruta_xml
        xml_file = open(ruta_xml, encoding="utf-8-sig")
        global jug
        global jug_comun
        jug = ListaGanador()
        #Esta va a guardarlos todos, pero se van a procesar ganadores y así con la otra lista
        #esta lista va a servir también para hacer búsquedas y eso
        jug_comun = ListaJugador()

        global jug_consultas 
        jug_consultas = ListaJugador()
        if xml_file.readable():
            datos = ET.fromstring(xml_file.read())
            lista_jugadores = datos.findall("jugador")
            print("Total de jugadores:", len(lista_jugadores))
            for jugador in lista_jugadores:
                puntos = 0
                lista_datos = jugador.findall("datospersonales")
                lista_movimientos = jugador.findall("movimientos")
                lista_tamaño = jugador.findall("tamaño")
                lista_figura = jugador.findall("figura")
                lista_puzzle = jugador.findall("puzzle")
                lista_solucion = jugador.findall("solucion")
                for datos in lista_datos:
                    nombre = datos.find("nombre").text
                    edad = datos.find("edad").text
                    print("Nombre del Jugador:", nombre + ".", "Edad:", edad + ".")
                for movimientos in lista_movimientos:
                    #hacer validaciones de movimientos
                    movimientos = movimientos.text
                    if int(movimientos) < 10000:
                        #print("Movimientos:", movimientos + ".")
                        if int(movimientos) < 5:
                            puntos += 100
                        elif int(movimientos) < 10:
                            puntos += 75
                        elif int(movimientos) < 15:
                            puntos += 50
                        elif int(movimientos) <= 20:
                            puntos += 25
                        elif int(movimientos) > 20:
                            puntos += 0
                for tamaño in lista_tamaño:
                    #hacer validaciones de tamaño
                    tamaño = tamaño.text
                    if int(tamaño) > 4 and int(tamaño) < 31:
                        if int(tamaño) == 5 or int(tamaño) == 10 or int(tamaño) == 15 or int(tamaño) == 20 or int(tamaño) == 25 or int(tamaño) == 30:
                            #print("Tamaño:", tamaño + ".")
                            if int(tamaño) == 5:
                                puntos += 25
                            elif int(tamaño) == 10:
                                puntos += 50
                            elif int(tamaño) == 15:
                                puntos += 75
                            elif int(tamaño) == 20:
                                puntos += 100
                            elif int(tamaño) == 25:
                                puntos += 125
                            elif int(tamaño) == 30:
                                puntos += 150
                        else: 
                            print("El tamaño debe ser en múltiplos de 5.")
                            return
                    else:
                        print("El tamaño debe ser igual o mayor a 5 y menor o igual a 30.")
                for figura in lista_figura:
                    #supongo que hay que hacer validaciones para la figura
                    figura = figura.text
                    #print("Figura:", figura + ".")
                    if figura == "Estrella de Belen":
                        puntos += 500
                    elif figura == "Arbol de Navidad":
                        puntos += 250
                    elif figura == "Regalo":
                        puntos += 100
                for puzzle in lista_puzzle:
                    celda = puzzle.iter("celda")
                    for celda in celda:
                        fila = celda.attrib["f"]
                        columna = celda.attrib["c"]
                        #print("Fila:", fila + ".", "Columna:", columna + ".")
                        """puzzle_desordenado.insert(int(fila), int(columna), celda.text)
                        puzzle_desordenado.graficarArbol("arbol")"""

                for solucion in lista_solucion:
                    celda_solucion = solucion.iter("celda")
                    for celda_solucion in celda_solucion:
                        fila_solucion = celda_solucion.attrib["f"]
                        columna_solucion = celda_solucion.attrib["c"]
                        #print("Fila Solución:", fila_solucion + ".", "Columna Solución:", columna_solucion + ".")
                print("--------------------------------------------------")
                print(f"Puntos totales {i}:", puntos)
                i += 1
                
                jug_comun.agregarPrimero(nombre, int(puntos), figura, int(tamaño), int(movimientos))
                jug_consultas.agregarUltimo(nombre, int(puntos), figura, int(tamaño), int(movimientos))

        print("lista inicial de jugadores")
        jug_comun.recorrido()
        print("-------------lista de jugadores ordenada por puntos")
        jug_comun.ordenar_mayor_menor()
        print("Enviando los primeros 10 lugares...")
        global lista_ganadores
        lista_ganadores = jug_comun.env_primeros10()
        global lis_gan
        lis_gan = jug_comun.env_primeros10()
        #lista_ganadores.ordenar_menor_mayor()
        #lista_ganadores.ordenar_mayor_menor()
        #lista_ganadores.recorrido()
        global nombres
        nombres = lista_ganadores.env_nombres()
        #medionombres = lista_ganadores.env_medio_nombres() #verificar orden
        #print("medio nombres:", medionombres)
        #lectura de ruta2_xml (premios)
        ruta2_xml = ruta2_xml
        xml_file2 = open(ruta2_xml, encoding="utf-8-sig")
        global regalosss
        regalosss = ListaRegalos()
        global regalos2
        regalos2 = ListaRegalos()
        if xml_file2.readable():
            datos = ET.fromstring(xml_file2.read())
            lista_premios = datos.findall("premio")
            #print("Total de premios:", len(lista_premios))
            for premio in lista_premios:
                lugar = premio.find("lugar").text
                regalo = premio.find("regalo").text
                regalosss.agregarPrimero(regalo, int(lugar))
                regalos2.agregarPrimero(regalo, int(lugar))
                #print("Lugar del Jugador:", lugar + ".", "Regalo recibido:", regalo + ".")

            print("lista de regalos")
            regalosss.recorrido()
            print("--------------------------------------------------")
        else:
            print("No se puede leer el archivo. ¿Por? No sé.")
    except Exception as error:
        print("Uy, error:", error)

def generar_puzzle2(ruta_xml):
    import xml.etree.ElementTree as ET
    try:

        print("-----------------cola inicial---------------------")
        jug_consultas.recorrido()
        global todos_nombres
        todos_nombres = jug_consultas.env_nombres()
        graphviz_todos()
        ruta_xml = ruta_xml
        xml_file = open(ruta_xml, encoding="utf-8-sig")
        if xml_file.readable():
            datos = ET.fromstring(xml_file.read())
            lis_jug = datos.findall("jugador")
            print("Total de jugadores:", len(lis_jug))
            i = 1
        si_no = input("¿Desea empezar a generar los puzzles? (s/n):")
        if si_no == "s":
            for jugador in lis_jug:
                jug_consultas.eliminar_solo_uno()
                print("--------------------------------------------------")
                print("Cola actualizada")
                jug_consultas.recorrido()
                todos_nombres = jug_consultas.env_nombres()
                graphviz_todos()

                print("--------------------------------------------------")
                print("Generando puzzle...")
                print("--------------------------------------------------")
                #creación de la matriz
                puzzle_desordenado = MatrizDispersa(0)
                puzzle_ordenado = MatrizDispersa(0)
                lista_figura = jugador.findall("figura")
                lista_puzzle = jugador.findall("puzzle")
                lista_solucion = jugador.findall("solucion")

                for figura in lista_figura:
                    #supongo que hay que hacer validaciones para la figura
                    figura = figura.text
                    #eliminar la figura que ya se usó

                for puzzle in lista_puzzle:
                    celda = puzzle.iter("celda")
                    for celda in celda:
                        fila = celda.attrib["f"]
                        columna = celda.attrib["c"]
                        #print("Fila:", fila + ".", "Columna:", columna + ".")
                        if figura == "Arbol de Navidad":
                            puzzle_desordenado.insert(int(fila), int(columna), "a")
                            puzzle_desordenado.graficarArbol("Arbol_navidad")
                        if figura == "Estrella de Belen":
                            puzzle_desordenado.insert(int(fila), int(columna), "e")
                            puzzle_desordenado.graficarEstrella("Estrella_belen")
                        if figura == "Regalo":
                            puzzle_desordenado.insert(int(fila), int(columna), "r")
                            puzzle_desordenado.graficarRegalo("Regalo")
                                    
                for solucion in lista_solucion:
                    celda_solucion = solucion.iter("celda")
                    for celda_solucion in celda_solucion:
                        fila_solucion = celda_solucion.attrib["f"]
                        columna_solucion = celda_solucion.attrib["c"]
                        #print("Fila Solución:", fila_solucion + ".", "Columna Solución:", columna_solucion + ".")
                        if figura == "Arbol de Navidad":
                            puzzle_ordenado.insert(int(fila_solucion), int(columna_solucion), "a")
                            puzzle_ordenado.graficarArbol("solucion_arbol")
                        if figura == "Estrella de Belen":
                            puzzle_ordenado.insert(int(fila_solucion), int(columna_solucion), "e")
                            puzzle_ordenado.graficarEstrella("solucion_estrella")
                        if figura == "Regalo":
                            puzzle_ordenado.insert(int(fila_solucion), int(columna_solucion), "r")
                            puzzle_ordenado.graficarRegalo("solucion_regalo")
                print("--------------------------------------------------")
                print(f"Puzzle {i} generado.")
                i += 1
                print("--------------------------------------------------")
                        
        if si_no == "n":
            print("--------------------------------------------------")
            print("Saliendo...")
            print("--------------------------------------------------")
            return
    except Exception as error:
        print("Uy, error:", error)

def generar_puzzle(ruta_xml):
    import xml.etree.ElementTree as ET
    try:

        print("-----------------cola inicial---------------------")
        jug_consultas.recorrido()
        global todos_nombres
        todos_nombres = jug_consultas.env_nombres()
        graphviz_todos()
        ruta_xml = ruta_xml
        xml_file = open(ruta_xml, encoding="utf-8-sig")
        if xml_file.readable():
            datos = ET.fromstring(xml_file.read())
            lis_jug = datos.findall("jugador")
            print("Total de jugadores:", len(lis_jug))
            i = 1
        while True:
            #lectura para generar el puzzle ordenado y desordenado
            #debo generar sólo de una iteración y preguntar si se desea generar otro
            #si se desea generar otro, se debe generar otro puzzle
            #si no se desea generar otro, se debe salir del programa
            
                #hacer menú
                print("1. Generar puzzle")
                print("2. Salir")
                opcion = input("Ingrese una opción: ")
                if opcion == "1":
                    jug_consultas.eliminar_solo_uno()
                    print("--------------------------------------------------")
                    print("Cola actualizada")
                    jug_consultas.recorrido()
                    todos_nombres = jug_consultas.env_nombres()
                    graphviz_todos()
                    print("--------------------------------------------------")

                    print("--------------------------------------------------")
                    print("Generando puzzle...")
                    print("--------------------------------------------------")
                    

                    for jugador in lis_jug:
                        #creación de la matriz
                        puzzle_desordenado = MatrizDispersa(0)
                        puzzle_ordenado = MatrizDispersa(0)
                        lista_figura = jugador.findall("figura")
                        lista_puzzle = jugador.findall("puzzle")
                        lista_solucion = jugador.findall("solucion")

                        for figura in lista_figura:
                            #supongo que hay que hacer validaciones para la figura
                            figura = figura.text
                            #eliminar la figura que ya se usó

                        for puzzle in lista_puzzle:
                            celda = puzzle.iter("celda")
                            for celda in celda:
                                fila = celda.attrib["f"]
                                columna = celda.attrib["c"]
                                #print("Fila:", fila + ".", "Columna:", columna + ".")
                                if figura == "Arbol de Navidad":
                                    puzzle_desordenado.insert(int(fila), int(columna), "a")
                                    puzzle_desordenado.graficarArbol("Arbol_navidad")
                                if figura == "Estrella de Belen":
                                    puzzle_desordenado.insert(int(fila), int(columna), "e")
                                    puzzle_desordenado.graficarEstrella("Estrella_belen")
                                if figura == "Regalo":
                                    puzzle_desordenado.insert(int(fila), int(columna), "r")
                                    puzzle_desordenado.graficarRegalo("Regalo")
                                
                        for solucion in lista_solucion:
                            celda_solucion = solucion.iter("celda")
                            for celda_solucion in celda_solucion:
                                fila_solucion = celda_solucion.attrib["f"]
                                columna_solucion = celda_solucion.attrib["c"]
                                #print("Fila Solución:", fila_solucion + ".", "Columna Solución:", columna_solucion + ".")
                                if figura == "Arbol de Navidad":
                                    puzzle_ordenado.insert(int(fila_solucion), int(columna_solucion), "a")
                                    puzzle_ordenado.graficarArbol("solucion_arbol")
                                if figura == "Estrella de Belen":
                                    puzzle_ordenado.insert(int(fila_solucion), int(columna_solucion), "e")
                                    puzzle_ordenado.graficarEstrella("solucion_estrella")
                                if figura == "Regalo":
                                    puzzle_ordenado.insert(int(fila_solucion), int(columna_solucion), "r")
                                    puzzle_ordenado.graficarRegalo("solucion_regalo")
                        print("--------------------------------------------------")
                        print(f"Puzzle {i} generado.")
                        i += 1
                        print("--------------------------------------------------")
                        break
                elif opcion == "2":
                    print("--------------------------------------------------")
                    print("Saliendo de esta sección...")
                    print("--------------------------------------------------")
                    break
    except Exception as error:
        print("Uy, error:", error)

def generar_paracomun():
    #esta es la lista con la que puedo hacer la cola y mostrarla
    print("-----------------cola inicial---------------------")
    jug_consultas.recorrido()
    global todos_nombres
    todos_nombres = jug_consultas.env_nombres()
    graphviz_todos()
    while True:
        print("--------------------------------------------------")
        print("1. Generar gráfica.")
        print("---")
        print("   Cada vez que seleccione la opción 1, se generará un")
        print("   nuevo puzzle y se retirará al jugador de la cola.")
        print("---")
        print("2. Salir.")
        print("--------------------------------------------------")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            print("--------------------------------------------------")
            print("Generando la siguiente gráfica...")
            print("--------------------------------------------------")
            jug_consultas.eliminar_solo_uno()
            print("--------------------------------------------------")
            print("Cola actualizada")
            jug_consultas.recorrido()
            todos_nombres = jug_consultas.env_nombres()
            graphviz_todos()
            print("--------------------------------------------------")
        elif opcion == "2":
            print("--------------------------------------------------")
            print("Saliendo...")
            print("--------------------------------------------------")
            break

def graphviz_todos():
    #primera impresión
    para_todos1 = """digraph structs {

    n1 [label=\""""

    para_todos2 = f"""{todos_nombres}"""
    para_todos3 = """\" shape=record];

}"""

    para_todos = para_todos1 + para_todos2 + para_todos3
    print("la cadena de jugadores completos es:",para_todos)
    generar1 = open("cola_jugadores.dot", "w")
    generar1.write(para_todos)
    generar1.close()
    system("dot -Tpng cola_jugadores.dot -o cola_jugadores.png")
    system("cd ./cola_jugadores.png")

def entrega_regalos():
    print("dentro funcion entrega")

    """jug_comun.recorrido()
    #no funciona xd
    lista_ganadores.ordenar_mayor_menor()
    print("lista de ganadores ordenada por puntossss")
    lista_ganadores.recorrido()
    #esto es solo para ver cómo queda la lista inicial (para ver lo de las consultas de usuario)"""
    
    #lo de arriba lo comenté para hacer pruebas

    print("Lista inicial:")
    jug_comun.recorrido()
    global nombres_principio
    lista_ganadores.ordenar_menor_mayor()
    #nombres_mitad = jug.eliminar_mitad()
    #print("le doy a eliminar_mitad")
    #lista_ganadores.eliminar_mitad() #debe eliminar mitad más pequeña
    print("Recorriendo lista de ganadores ordenado de mayor a menor")
    lista_ganadores.recorrido()
    #jug.eliminar_primero()
    print("le doy a eliminar_primero1")
    global nombres_mitad2
    lista_ganadores.eliminar_primero1()
    nombres_mitad2 = lista_ganadores.env_nombres()
    print("así queda luego de eliminar los demás, vacío?")
    lista_ganadores.recorrido()
    lista_ganadores.eliminar_primero2()
    lista_ganadores.recorrido()
    #regalosss.eliminar_ultimo()
    regalosss.recorrido()
    global regalos_completos
    regalos_completos = regalosss.env_nombres()
    regalosss.eliminar_primero1()
    global regalos_mitad
    regalos_mitad = regalosss.env_nombres()
    regalosss.eliminar_primero2()
    regalosss.recorrido()
    
    print("saliendo de la fnción de entrega")
    
def graphviz_cola_completa():
    #primera impresión
    entrega_regalos_gv1 = """digraph structs {

    n1 [label=\""""

    entrega_regalos_gv2 = f"""{nombres}"""
    entrega_regalos_gv3 = """\" shape=record];

}"""

    entrega_regalos_gv = entrega_regalos_gv1 + entrega_regalos_gv2 + entrega_regalos_gv3
    print("la cadena de jugadores completos es:",entrega_regalos_gv)
    generar1 = open("cola_inicial.dot", "w")
    generar1.write(entrega_regalos_gv)
    generar1.close()
    system("dot -Tpng cola_inicial.dot -o cola_inicial.png")
    system("cd ./cola_inicial.png")

def graphviz_cola_media():
    #impresión a la mitad
    entrega_regalos_gv151 = """digraph structs {

    n1 [label=\""""

    entrega_regalos_gv251 = f"""{nombres_mitad2}"""
    entrega_regalos_gv351 = """\" shape=record];

}"""

    entrega_regalos_gv51 = entrega_regalos_gv151 + entrega_regalos_gv251 + entrega_regalos_gv351
    print("la cadena de jugadores media es:",entrega_regalos_gv51)
    generar2 = open("cola_media.dot", "w")
    generar2.write(entrega_regalos_gv51)
    generar2.close()
    system("dot -Tpng cola_media.dot -o cola_media.png")
    system("cd ./cola_media.png")

def graphviz_pila_completa():
    #impresión a la mitad
    entrega_regalos_gv15 = """digraph structs {

    n1 [label=\"{"""

    entrega_regalos_gv25 = f"""{regalos_completos}"""
    entrega_regalos_gv35 = """}\" shape=record];

}"""

    entrega_regalos_gv5 = entrega_regalos_gv15 + entrega_regalos_gv25 + entrega_regalos_gv35
    print("la cadena de regalos completa es:",entrega_regalos_gv5)

    generar3 = open("pila_completa.dot", "w")
    generar3.write(entrega_regalos_gv5)
    generar3.close()
    system("dot -Tpng pila_completa.dot -o pila_completa.png")
    system("cd ./pila_completa.png")

def graphviz_pila_mitad():
    #impresión a la mitad
    entrega_regalos_gv152 = """digraph structs {

    n1 [label=\"{"""

    entrega_regalos_gv252 = f"""{regalos_mitad}"""
    entrega_regalos_gv352 = """}\" shape=record];

}"""

    entrega_regalos_gv52 = entrega_regalos_gv152 + entrega_regalos_gv252 + entrega_regalos_gv352
    print("la cadena de regalos mitad es:",entrega_regalos_gv52)
    generar4 = open("pila_mitad.dot", "w")
    generar4.write(entrega_regalos_gv52)
    generar4.close()
    system("dot -Tpng pila_mitad.dot -o pila_mitad.png")
    system("cd ./pila_mitad.png")

def entrega_oficial():
    a = 1
    b = 1
    while a < 11 and b < 11:
        print(f"---------------Entrega de regalo {a}:----------------")
        #entrega del primer regalo: eliminar el primero de la lista de ganadores y el último de la lista de regalos
        #sólo eliminar el primero de la lista de ganadores
        lis_gan.eliminar_solo_uno()
        a += 1
        regalos2.eliminar_solo_uno()
        b += 1
    print("----------------------------------------------------")

"""
#para puzzles
def insertaTodo():
    with open('Figura3.txt') as archivo:
        l=0
        c=0
        lineas=archivo.readlines()
        for linea in lineas:
            columnas=linea
            l+=1
            for col in columnas:
                if col != '\n':
                    c+=1
                    matriz.insert(l,c,col)
            c=0
            matriz.graficarDibujo('toad')
"""
"""
def insertaSeleccion():
    with open('Figura3.txt') as archivo:
        l=0
        c=0
        lineas=archivo.readlines()
        for linea in lineas:
            columnas=linea
            l+=1
            for col in columnas:
                if col != '\n':
                    c+=1
                    if col=='*':
                        matriz.insert(l,c,col)
            c=0
            matriz.graficarDibujo('toad')
"""

#se usa según el caso
#insertaTodo()
#insertaSeleccion()

print("-----------------¡Bienvenid@ al juego de Puzzle!------------------")
global ruta
ruta = input("--------Por favor, ingrese el nombre del archivo XML de jugadores: ")
ruta2 = input("----------Por favor, ingrese el nombre del archivo XML de premios: ")
a = leer_xml(f"{ruta}", f"{ruta2}")
regalosss.recorrido()
#graphviz_entrega()
while True:
    print("Ingrese el número de la opción que desea ejecutar:")
    print("1. Simular Entrega de Regalos en Consola.") #listo
    print("2. Ver cola de participantes e ir generando su puzzle mientras se retiran de la cola.")
    print("3. Generar gráficos de Entrega de Regalos.") #listo
    print("4. Salir.")
    opcion = input("Opción: ")
    if opcion == "1":
        entrega_oficial()
    elif opcion == "2":
        #este va a ser para que se ejecute la gráfica de cada participante pero también
        #que se retire de la cola de jugadores gráficamente
        """nombre = input("Ingrese el nombre del participante: ")
        jug_comun.buscar(nombre)"""
        #generar_paracomun()
        generar_puzzle2(ruta)
    elif opcion == "3":
        entrega_regalos()
        graphviz_cola_completa() #cola inicial
        graphviz_cola_media()
        graphviz_pila_completa()
        graphviz_pila_mitad()
    elif opcion == "4":
        print("¡Hasta luego!")
        break