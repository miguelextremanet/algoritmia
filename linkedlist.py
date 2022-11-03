# ejemplo lista enlazada con phyon
class Node:
    def __init__(self,data):
        self.data = data ## asignamos el dato
        self.siguiente = None ## puntero al siguiente elemento. 
        
class LinkedList:
    def __init(self):
        self.head = None

         
    def deletenode(self, position):
        if self.head is None:
            return
        # si el elemento a borrar es el 0, movemos hacia atras los elementos de la lista
        if position == 0:
            self.head = self.head.siguiente
            return self.head
        
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        
        while current is not None:
            if index == position:
                temp = current.siguiente
                break
            prev = current
            current = current.siguiente
            index +=1
        prev.next = temp
        return prev



    def imprimirLista(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.siguiente
        
list = LinkedList()
list.head = Node(1)

elemento2 = Node(2)
elemento3 = Node(3)
elemento4 = Node(4)
# insertamos el elemento 4 despues del 1
list.head.siguiente = elemento4
#ahora despues del 4 va el 2 
elemento4.siguiente = elemento2
elemento2.siguiente = elemento3

list.imprimirLista()
print("llamamos al deletenode(2) ")
list.deletenode(2)
list.imprimirLista()
