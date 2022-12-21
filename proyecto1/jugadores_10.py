from lista_simplee import ListaJugador

#agregar jugadores a la lista
lista_jugadores = ListaJugador()
lista_jugadores.agregarUltimo("Juan", 564)
lista_jugadores.agregarUltimo("Pedro", 767)
lista_jugadores.agregarUltimo("Maria", 7545)
lista_jugadores.agregarUltimo("Ana", 555)
lista_jugadores.agregarUltimo("Luis", 100)
print("lista sin ordenar")
lista_jugadores.recorrido()
lista_jugadores.ordenar()
print("lista ordenada")
lista_jugadores.recorrido()