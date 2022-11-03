# ejemplo lista enlazada con phyon
class Node:
    def __init__(self,data):
        self.data = data ## asignamos el dato
        self.siguiente = None ## puntero al siguiente elemento. 
        
class LinkedList:
    def __init(self):
        self.cabeza = None
    def imprimirLista(self):
        temp = self.cabeza
        while (temp):
            print(temp.data)
            temp = temp.siguiente
        
list = LinkedList()
list.cabeza = Node(1)

elemento2 = Node(2)
elemento3 = Node(3)
elemento4 = Node(4)
# insertamos el elemento 4 despues del 1
list.cabeza.siguiente = elemento4
#ahora despues del 4 va el 2 
elemento4.siguiente = elemento2
elemento2.siguiente = elemento3
list.imprimirLista()
