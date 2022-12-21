from ganador import Ganador
from jugador import Jugador
from premio import Premio

class ListaGanador():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def estaVacia(self):
        return self.primero==None

    def agregarUltimo(self,nombre,puntos):
        nuevo=Ganador(nombre, puntos)

        temp = self.primero

        if temp is None:
            self.primero = self.ultimo = nuevo 
        else:
            temp = self.primero
            while temp.siguiente is not None:
                    temp=temp.siguiente
            temp.siguiente=nuevo
            
        """if self.estaVacia==True:
            self.primero=self.ultimo=nuevo
        else:
            temp = self.primero
            #le agregué desde el if y su contenido hasta "else:" y le metí lo de abajo ahí.
            if temp is None:
                self.primero = nuevo
            else:
                while temp.siguiente is not None:
                    temp=temp.siguiente
                temp.siguiente=nuevo"""
    #si viene de 1 a 10
    def agregarPrimero(self, nombre, puntos):
        nuevo=Ganador(nombre, puntos)
        if self.estaVacia==True:
            self.primero=self.ultimo=nuevo
        else:
            temp=nuevo
            temp.siguiente=self.primero
            self.primero=temp

        """#supongo que igual debería recorrer y luego ordenarlo
        def ordenar(self):
            temp = self.primero
            while temp != None:
                temp2 = temp.siguiente #esto es para que no se compare consigo mismo
                while temp2 != None:
                    if temp.puntos < temp2.puntos:
                        #700 < 900
                        #a, b = b, a
                        #intercambio de valores de puntos
                        """"""menor = temp.puntos
                        mayor = temp2.puntos
                        nombre_menor = temp.nombre
                        nombre_mayor = temp2.nombre
                        temp.puntos = mayor
                        temp2.puntos = menor
                        temp.nombre = nombre_mayor
                        temp2.nombre = nombre_menor""""""
                        temp.puntos, temp2.puntos = temp2.puntos, temp.puntos
                        #intercambio de valores de nombre
                        temp.nombre, temp2.nombre = temp2.nombre, temp.nombre
                    temp2 = temp2.siguiente
                temp = temp.siguiente"""

    def recorrido(self):
        temp=self.primero
        while temp != None:
            print(temp.nombre,temp.puntos)
            temp=temp.siguiente
    
    def env_nombres(self):
        temp=self.primero
        cadena = ""
        while temp != None:
            if temp.siguiente is not None:
                cadena += temp.nombre + "|"
            else:
                cadena += temp.nombre
            temp=temp.siguiente
        return cadena

    def env_medio_nombres(self):
        temp=self.primero
        cadena = ""
        a = 0
        while temp != None and a < 6:
            if temp.siguiente is not None and a < 5:
                cadena += temp.nombre + "|"
            else:
                cadena += temp.nombre
            temp=temp.siguiente 
            a += 1
        return cadena

    def eliminar_primero1(self):
        #funcion para eliminar el ultimo elemento de la lista
        i = 0
        if self.estaVacia==True:
            print("La lista está vacía")
        else:
            while self.primero != None and i < 5:
                temp=self.primero
                self.primero=temp.siguiente
                temp.siguiente=None
                i += 1
                print(i, "sí")
                self.recorrido()
    
    def eliminar_solo_uno(self):
        #funcion para eliminar el ultimo elemento de la lista
        i = 0
        if self.estaVacia==True:
            print("La lista está vacía")
        else:
            while self.primero != None and i < 1:
                print("Entregando a:", self.primero.nombre)
                temp=self.primero
                self.primero=temp.siguiente
                temp.siguiente=None
                #self.recorrido()
                i += 1
    
    def eliminar_primero2(self):
        #funcion para eliminar el ultimo elemento de la lista
        i = 5
        if self.estaVacia==True:
            print("La lista está vacía")
        else:
            while self.primero != None and i < 11:
                temp=self.primero
                self.primero=temp.siguiente
                temp.siguiente=None
                i += 1
                print(i, "sí")
                self.recorrido()
    
    def eliminar_ultimo(self):
        #funcion para eliminar el ultimo elemento de la lista
        if self.estaVacia==True:
            print("La lista está vacía")
        else:
            temp=self.primero
            while temp.siguiente != self.ultimo:
                temp=temp.siguiente
            self.ultimo=temp
            self.ultimo.siguiente=None
        self.recorrido()
    
    def eliminar_ult(self):
        temp = self.primero
        while temp.siguiente != None:
            temp = temp.siguiente
        if temp == self.primero:
            self.primero = None
        else:
            temp2 = self.primero
            while temp2.siguiente != temp:
                temp2 = temp2.siguiente
            temp2.siguiente = None
        self.recorrido()

    def ordenar_menor_mayor(self):
        #función para ordenar la lista de menor a mayor
        temp = self.primero
        while temp != None:
            temp2 = temp.siguiente
            while temp2 != None:
                if temp.puntos > temp2.puntos:
                    temp.puntos, temp2.puntos = temp2.puntos, temp.puntos
                    temp.nombre, temp2.nombre = temp2.nombre, temp.nombre
                temp2 = temp2.siguiente
            temp = temp.siguiente

    def ordenar_mayor_menor(self):
    #función para ordenar la lista de mayor a menor
        temp = self.primero
        while temp != None:
            temp2 = temp.siguiente
            while temp2 != None:
                if temp.puntos < temp2.puntos:
                    temp.puntos, temp2.puntos = temp2.puntos, temp.puntos
                    temp.nombre, temp2.nombre = temp2.nombre, temp.nombre
                temp2 = temp2.siguiente
            temp = temp.siguiente
        print("peppa pig")

    def ordenar_may_men(self):
        #funcion para ordenar la lista de menor a mayor
        temp = self.primero
        while temp != None:
            temp2 = temp.siguiente #esto es para que no se compare consigo mismo    
            while temp2 != None:
                if temp.puntos > temp2.puntos:
                    #700 < 900
                    #a, b = b, a
                    #intercambio de valores de puntos
                    """menor = temp.puntos
                    mayor = temp2.puntos
                    nombre_menor = temp.nombre
                    nombre_mayor = temp2.nombre
                    temp.puntos = mayor
                    temp2.puntos = menor
                    temp.nombre = nombre_mayor
                    temp2.nombre = nombre_menor"""
                    temp.puntos, temp2.puntos = temp2.puntos, temp.puntos
                    #intercambio de valores de nombre
                    temp.nombre, temp2.nombre = temp2.nombre, temp.nombre
                temp2 = temp2.siguiente
        self.recorrido()

    def eliminar_mitad(self):

        #funcion para eliminar el ultimo elemento de la lista
        i = 0
        if self.estaVacia==True:
            print("La lista está vacía")
        else:
            while self.primero.siguiente != None:
                temp=self.primero
                self.primero=temp.siguiente
                temp.siguiente=None
                if i == 4:
                    m = self.env_nombres()
                    return m
                i += 1
                print(i)
            
class ListaRegalos():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def estaVacia(self):
        return self.primero==None

    def eliminar_solo_uno(self):
        #funcion para eliminar el ultimo elemento de la lista
        i = 0
        if self.estaVacia==True:
            print("La lista está vacía")
        else:
            while self.primero != None and i < 1:
                print("Entregando el regalo:", self.primero.regalo)
                temp=self.primero
                self.primero=temp.siguiente
                temp.siguiente=None
                i += 1              
    #si viene de 10 a 1
    def agregarUltimo(self,regalo,lugar):
        nuevo=Premio(regalo,lugar)

        temp = self.primero

        if temp is None:
            self.primero = self.ultimo = nuevo 
        else:
            temp = self.primero
            while temp.siguiente is not None:
                    temp=temp.siguiente
            temp.siguiente=nuevo
    #si viene de 1 a 10
    def agregarPrimero(self, regalo, lugar):
        nuevo=Premio(regalo, lugar)
        if self.estaVacia==True:
            self.primero=self.ultimo=nuevo
        else:
            temp=nuevo
            temp.siguiente=self.primero
            self.primero=temp

    def recorrido(self):
        temp=self.primero
        while temp != None:
            print(temp.regalo,temp.lugar)
            temp=temp.siguiente

    def eliminar_primero1(self):
        #funcion para eliminar el ultimo elemento de la lista
        i = 0
        if self.estaVacia==True:
            print("La lista está vacía")
        else:
            while self.primero != None and i < 5:
                temp=self.primero
                self.primero=temp.siguiente
                temp.siguiente=None
                i += 1
                print(i, "sí")
                self.recorrido()

    def eliminar_primero2(self):
        #funcion para eliminar el ultimo elemento de la lista
        i = 5
        if self.estaVacia==True:
            print("La lista está vacía")
        else:
            while self.primero != None and i < 11:
                temp=self.primero
                self.primero=temp.siguiente
                temp.siguiente=None
                i += 1
                print(i, "sí")
                self.recorrido()

    def env_nombres(self):
        temp=self.primero
        cadena = ""
        while temp != None:
            if temp.siguiente is not None:
                cadena += temp.regalo + "|"
            else:
                cadena += temp.regalo
            temp=temp.siguiente
        return cadena

    def eliminar_ultimo(self):
        #funcion para eliminar el primer elemento de la lista
        #esto creo que en realidad sería eliminar el último
        i = 0
        if self.estaVacia==True:
            print("La lista está vacía")
        else:
            while self.primero.siguiente != None:
                temp=self.primero
                self.primero=temp.siguiente
                temp.siguiente=None
                self.recorrido()
                i += 1
                print(i)

class ListaJugador():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def estaVacia(self):
        return self.primero==None

    def agregarUltimo(self,nombre,puntos, figura, tamaño, movimientos):
        nuevo=Jugador(nombre,puntos, figura, tamaño, movimientos)

        temp = self.primero

        if temp is None:
            self.primero = self.ultimo = nuevo 
        else:
            temp = self.primero
            while temp.siguiente is not None:
                    temp=temp.siguiente
            temp.siguiente=nuevo
        self.recorrido()
            
        """if self.estaVacia==True:
            self.primero=self.ultimo=nuevo
        else:
            temp = self.primero
            #le agregué desde el if y su contenido hasta "else:" y le metí lo de abajo ahí.
            if temp is None:
                self.primero = nuevo
            else:
                while temp.siguiente is not None:
                    temp=temp.siguiente
                temp.siguiente=nuevo"""
    #si viene de 1 a 10
    def agregarPrimero(self, nombre, puntos, figura, tamaño, movimientos):
        nuevo=Jugador(nombre, puntos, figura, tamaño, movimientos)
        if self.estaVacia==True:
            self.primero=self.ultimo=nuevo
        else:
            temp=nuevo
            temp.siguiente=self.primero
            self.primero=temp

    def eliminar_solo_uno(self):
        #funcion para eliminar el ultimo elemento de la lista
        i = 0
        if self.estaVacia==True:
            print("La lista está vacía")
        else:
            while self.primero != None and i < 1:
                print("Entregando a:", self.primero.nombre)
                temp=self.primero
                self.primero=temp.siguiente
                temp.siguiente=None
                #self.recorrido()
                i += 1

    def recorrido(self):
        temp=self.primero
        while temp != None:
            print(temp.nombre,temp.puntos)
            temp=temp.siguiente
    
    def env_nombres(self):
        temp=self.primero
        cadena = ""
        while temp != None:
            if temp.siguiente is not None:
                cadena += temp.nombre + "|"
            else:
                cadena += temp.nombre
            temp=temp.siguiente
        return cadena
    
    def env_primeros10(self):
        ganadores = ListaGanador()
        temp=self.primero
        tada = 0
        while temp != None:
            if tada < 10:
                nombre = temp.nombre
                puntos = temp.puntos
                ganadores.agregarPrimero(nombre, puntos)
                tada += 1
            temp=temp.siguiente
        return ganadores

    def env_medio_nombres(self):
        temp=self.primero
        cadena = ""
        a = 0
        while temp != None:
            if temp.siguiente is not None and a < 6:
                cadena += temp.nombre + "|"
            else:
                cadena += temp.nombre
            temp=temp.siguiente 
            a += 1
        return cadena

    def eliminar_primero(self):
        #funcion para eliminar el ultimo elemento de la lista
        i = 0
        if self.estaVacia==True:
            print("La lista está vacía")
        else:
            while self.primero.siguiente != None:
                temp=self.primero
                self.primero=temp.siguiente
                temp.siguiente=None
                self.recorrido()
                i += 1
                print(i)

    def eliminar_mitad(self):
        #funcion para eliminar el ultimo elemento de la lista
        i = 0
        if self.estaVacia==True:
            print("La lista está vacía")
        else:
            while self.primero.siguiente != None:
                temp=self.primero
                self.primero=temp.siguiente
                temp.siguiente=None
                if i == 4:
                    m = self.env_nombres()
                    return m
                i += 1
                print(i)
    #esta es la que funciona para el caso
    def ordenar_menor_mayor(self):
        #función para ordenar la lista de menor a mayor
        temp = self.primero
        while temp != None:
            temp2 = temp.siguiente
            while temp2 != None:
                if temp.puntos > temp2.puntos:
                    temp.puntos, temp2.puntos = temp2.puntos, temp.puntos
                    temp.nombre, temp2.nombre = temp2.nombre, temp.nombre
                    temp.figura, temp2.figura = temp2.figura, temp.figura
                    temp.tamaño, temp2.tamaño = temp2.tamaño, temp.tamaño
                    temp.movimientos, temp2.movimientos = temp2.movimientos, temp.movimientos
                temp2 = temp2.siguiente
            temp = temp.siguiente
        self.recorrido()
    #supongo que igual debería recorrer y luego ordenarlo
    def ordenar_men_may(self):
        #funcion para ordenar la lista de mayor a menor
        temp = self.primero
        while temp != None:
            temp2 = temp.siguiente #esto es para que no se compare consigo mismo
            while temp2 != None:
                if temp.puntos < temp2.puntos:
                    #700 < 900
                    #a, b = b, a
                    #intercambio de valores de puntos
                    """menor = temp.puntos
                    mayor = temp2.puntos
                    nombre_menor = temp.nombre
                    nombre_mayor = temp2.nombre
                    temp.puntos = mayor
                    temp2.puntos = menor
                    temp.nombre = nombre_mayor
                    temp2.nombre = nombre_menor"""
                    temp.puntos, temp2.puntos = temp2.puntos, temp.puntos
                    #intercambio de valores de nombre
                    temp.nombre, temp2.nombre = temp2.nombre, temp.nombre
                    #intercambio de valores de figura
                    temp.figura, temp2.figura = temp2.figura, temp.figura
                    #intercambio de valores de tamaño
                    temp.tamaño, temp2.tamaño = temp2.tamaño, temp.tamaño
                    #intercambio de valores de movimientos
                    temp.movimientos, temp2.movimientos = temp2.movimientos, temp.movimientos
                temp2 = temp2.siguiente
            temp = temp.siguiente
        self.recorrido()

    def ordenar_mayor_menor(self):
        #función para ordenar la lista de mayor a menor
        temp = self.primero
        while temp != None:
            temp2 = temp.siguiente
            while temp2 != None:
                if temp.puntos < temp2.puntos:
                    temp.puntos, temp2.puntos = temp2.puntos, temp.puntos
                    temp.nombre, temp2.nombre = temp2.nombre, temp.nombre
                    temp.figura, temp2.figura = temp2.figura, temp.figura
                    temp.tamaño, temp2.tamaño = temp2.tamaño, temp.tamaño
                    temp.movimientos, temp2.movimientos = temp2.movimientos, temp.movimientos
                temp2 = temp2.siguiente
            temp = temp.siguiente
        print("peppa pig")
        self.recorrido()

    def ordenar_may_men(self):
        #funcion para ordenar la lista de menor a mayor
        temp = self.primero
        while temp != None:
            temp2 = temp.siguiente #esto es para que no se compare consigo mismo    
            while temp2 != None:
                if temp.puntos > temp2.puntos:
                    #700 < 900
                    #a, b = b, a
                    #intercambio de valores de puntos
                    """menor = temp.puntos
                    mayor = temp2.puntos
                    nombre_menor = temp.nombre
                    nombre_mayor = temp2.nombre
                    temp.puntos = mayor
                    temp2.puntos = menor
                    temp.nombre = nombre_mayor
                    temp2.nombre = nombre_menor"""
                    temp.puntos, temp2.puntos = temp2.puntos, temp.puntos
                    #intercambio de valores de nombre
                    temp.nombre, temp2.nombre = temp2.nombre, temp.nombre
                    #intercambio de valores de figura
                    temp.figura, temp2.figura = temp2.figura, temp.figura
                    #intercambio de valores de tamaño
                    temp.tamaño, temp2.tamaño = temp2.tamaño, temp.tamaño
                    #intercambio de valores de movimientos
                    temp.movimientos, temp2.movimientos = temp2.movimientos, temp.movimientos
                temp2 = temp2.siguiente
        self.recorrido()

    def buscar(self, nombre):
        #funcion para buscar un elemento en la lista
        self.recorrido()
        temp=self.primero
        while temp != None:
            if temp.nombre == nombre:
                print("Jugador:", temp.nombre, "| Puntos:", temp.puntos, "| Figura:", temp.figura, "| Tamaño:", temp.tamaño, "x", temp.tamaño, "| Movimientos:", temp.movimientos)
            temp=temp.siguiente
        return None