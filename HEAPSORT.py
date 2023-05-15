#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def crear_monticulo(subarbol, n, i):
    
    #  [4, 2, 3, 5, 1, 9]
    ####################################################
    #  ESTA FUNCIÓN CONVIERTE UNA ESTRUCTURA DE ÁRBOL     
    # EN OTRO ARBOL PERO DE MONTICULOS MÁXIMOS DESDE ÍNDICE I CON TAMAÑO N
    ####################################################
    # POR DEFECTO INICIALIZAMOS MAYOR COMO EL RAIZ
    mayor = i  
    
    ####################################################
    print(f" --> Desde elemento {mayor} --> {subarbol[mayor]}")
    no_haya_hijos_mayores = True
    
    # SE SALE DEL BUCLE CUANDO YA NO HAYA HIJOS MAYORES
    ####################################################
    
    while no_haya_hijos_mayores:
        #########################
        #EMPEZAMOS POR LOS HIJOS
        #########################
        
        #cogemos los índices izquiero y derecho         
        hijo_izquierdo = 2 * i + 1  
        hijo_derecho = 2 * i + 2  

        ############################################################
        # COMPROBAR SI EL HIJO IZQUIERDO ES MAS GRANDE QUE EL PADRE
        ############################################################
        if hijo_izquierdo < n and subarbol[i] < subarbol[hijo_izquierdo]:            
            mayor = hijo_izquierdo
            
        ############################################################
        # COMPROBAR SI EL HIJO DERECHO ES MAS GRANDE QUE EL PADRE
        ############################################################
        
        if hijo_derecho < n and subarbol[mayor] < subarbol[hijo_derecho]:
            mayor = hijo_derecho

        

        ###################################################
        # SALE DEL BUCLE CUANDO YA NO HAY HIJOS MÁS GRANDES
        ###################################################
        if mayor == i:
            no_haya_hijos_mayores = False 
        else:
            # Intercambiar el hijo más grande con la raíz
            #subarbol[i], subarbol[mayor] = subarbol[mayor], subarbol[i]
            temp = subarbol[i]
            subarbol[i] = subarbol[mayor]
            subarbol[mayor] = temp
            
            
            ###############################################################
            # AHORA EL MAYOR NÚMERO ES EL NUEVO ÍNDICE 
            # Y PUEDE CONTINUAR HACIA ABAJO EN EL ARBOL
            ###############################################################
            i = mayor
    
    print (" --> Monticulo ahora queda así: ",subarbol)
    return subarbol


# In[ ]:



def heapSort(lista_que_queremos_ordenar):
    
    
    print("#######################################################")
    print("                    1 PARTE ")
    print("              CREAR MONTICULO INICIAL ")
    print("#######################################################")
    #######################################################
    #                    1 PARTE 
    #######################################################    
    #           CREA EL MONTICULO DE MÁXIMOS
    
    #######
    # coste de la primera parte  --> O(n) 
    #######
    
    #######################################################
    # porque necesita recorrer elementoS e intercambiar nodos hacia abajo 
    # convertirlo si hicera falta en un montículo máximo
    #######################################################
    
    n = len(lista_que_queremos_ordenar)
    
    
    for i in range(n // 2, -1,-1):
        monticulo = crear_monticulo(lista_que_queremos_ordenar, n, i)  
    print("Monticulo inicial creado coste O(n) porque recorre todos los elementos")
    print (monticulo)
    
    
    
    #######################################################
    #                    2ª PARTE 
    #######################################################
    #   extre los elementos del árbol y los inserta en la lista
    #######################################################
    
    #############
    # coste de la segunda parte  --> O(log n) 
    #############
    print("\n#######################################################")
    print("                    2ªPARTE ")
    print("                   INTERACIÓN  ")
    print("#######################################################")
    # lista que se devolverá 
    lista_ya_ordenada = []
    
    for i in range(n - 1, 0, -1):
        
        print("\nIteracion:" ,n+(-1*i))
        # primero intercambiamos el elemento raiz por el último  (posición i)
        # con el hijo más grande
        # Esto ayuda a mantener la propiedad del montículo 
        # y así nos aseguramos que el elemento más grande se coloque en la posición correcta en cada iteración.
        elemento = monticulo[i]
        monticulo[i] = monticulo[0]
        monticulo[0] = elemento        
        #print (monticulo)
        
        # insertar en 
        # En este caso, el elemento en la posición i es el elemento máximo que hemos extraído del montículo.
        lista_ya_ordenada.insert(0, monticulo.pop(i)) 
        print(" --> Insertamos el elemento mayor en la lista ordenada " ,lista_ya_ordenada)
       
        # volvemos a reorganizar el monticulo pero ya reducido 
        crear_monticulo(monticulo, i, 0)
        

    # ULTIMO ELEMENTO QUE QUEDA EN EL MONTICULO 
    lista_ya_ordenada.insert(0, monticulo.pop())  

    
    #############
    # coste total O(n log n) 
    #############

    
    return lista_ya_ordenada



# In[19]:


# LISTA QUE QUEREMOS ORDENAR 
lista = [4, 2, 3, 5, 1, 9]
print(f" La lista SIN ordenar es :{lista}")


# In[20]:


# aplicamos ordenación 
lista_ordenada = heapSort(lista)
print(f" La lista ya ordenada es :{lista_ordenada}")


# In[22]:


import datetime
import random
import tqdm
import time

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

linear_worst_time = list()  
linear_avg_time_t = list()  
linear_avg_time_r = list()  
linear_best_time = list()

ticks = list()
for n in tqdm.tqdm(range(10, 100, 10)):
    ticks.append(n)
    n = 100    
    
    random_list = random.sample(range(1, n+1), n)
    
    #MEJOR CASO 
    random_list.sort()           
    inicio = datetime.datetime.now()
    lista_ordenada = heapSort(random_list)
    fin = datetime.datetime.now()     
    tiempo = fin - inicio
    linear_best_time.append(tiempo.microseconds)
    
    #PEOR CASO    
    random_list = random.sample(range(1, n+1), n)
    fin = datetime.datetime.now()     
    tiempo = fin - inicio
    linear_worst_time.append(tiempo.microseconds)
    
# Configurar el ancho y el alto de la figura en pixeles
ancho_px = 500
alto_px = 300
dpi = 80
fig = plt.figure(figsize=(ancho_px/dpi, alto_px/dpi), dpi=dpi)
ax = plt.axes()

plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo en ms")
plt.xticks([])
#ax.plot(linear_avg_time_r)
#ax.plot(linear_avg_time_t)
ax.plot(linear_best_time)
ax.plot(linear_worst_time)


# In[ ]:




