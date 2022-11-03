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
        # si el elemento a borrar es el 0, movemos hacia atras
        if position == 0:
            self.head = self.head.siguiente
            return self.head
        
        # guardamos el inicio de la lista
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        
         # mientras haya elementos 
        while current is not None:
             # si el elemento buscado es el actual 
            if index == position:
                 # guardamos temporalmente el elemento siguiente , por ejemplo si quieremos borrar el 5, el temporal ahora es el 6
                temp = current.siguiente
                break
            # si hemos encontrado en el loop el elemento 
            # el anterior es el actual, por ejemplo el 5
            prev = current
            
            #y el actual es el el de cabecera  
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
