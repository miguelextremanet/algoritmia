
#busqueda linea con dos if 
def search(arr, search_element):
############################################################
 #Ejercicio: analizar el siguiente algoritmo de búsqueda. 
############################################################
# PERSNONALMENTE ME ENCANTA ESTE ALGORITMO, LIMPIO, SIMPLE PERO EFICAZ

# SE TRATA DE RECORRER EL ARRAY A LA VEZ POR AMBOS LADOS, INICIO  Y FINAL
# ES COMO SI HICIERAMOS DOS ITERACIONES GRACIAS A UNA SOLA.
# UNA DESDE EL PRINCIPIO Y YENDO PARA ADELANTE Y ADEMÁS AL MISMO TIEMPO 
# DESDE EL FINAL HACIA EL PRINCIPIO. ENCONTRAR EL VALOR BUSCADO ES BASTANTE RÁPIDO.
############################################################
#Explica el proceso que realiza con los datoS
############################################################
# ES UN TIPO DE ALGORITMO ITERATIVO O LINEAL QUE EN LUGAR DE MOVERSE SEGUN EL VALOR
# DEL DATO TENIENDO EN CUENTA SI EL VALOR ES MAYOR O MENO, NO IMPORTA EL VALOR
# SIMPLEMENTE SE MUEVE EN AMBOS SENTIDOS Y SI EL DATO ES IGUAL DA POR FINALIZADA LA BUSQUEDA
# ADEMÁS NO SE NECESITA ORDENAR LOS DATOS COMO EN LA BUSQUEDA BINARIA 
############################################################
#• ¿Cuál es el coste en tiempo si el elemento buscado está efectivamente 
#en la última posición del array?
############################################################
# EL COSTE DEL TIEMPO ES O(1) ES DECIR UN SOLO PASO
# LA COMPLEJIDAD DEL ALGORIMO ES O(N)

############################################################
# ¿Cómo compara el coste en tiempo respecto el algoritmo de 
# #búsqueda lineal básico visto en clase?
############################################################
# ESTE ALGORIMO NO TIENE EN CUENTA SI EL VALOR COMPARADO ES MAYOR O MENOR
# ESTE SE POSICIONAL AL MISMO TIEMPO EN DOS POSICIONES OPUESTAS DEL VECTOR Y ES CAPAZ 
# DE MOVERSE EN AMBAS DIRECCIONES A LA VEZ CON DOS SIMPLES IF 

# EN ALGORITOS BINARIOS  HABITUAL , AL CONTRARIO DE ESTE SE POSICIONAL SIEMPRE EN LA MITDAD DE LA LISTA INICIALMENTE 
# Y EMPIEZAN A VER SI EL VALOR A BUSCAR ES MAYOR O MENOR. 
# SIN EMBARGO, EN ESTE CASO, SI BUSCASEMOS EL VALOR 3, LO ENCONTRARIAMOS ANTES CON 
#ALGORITMO BINARIO CONVENCIONAL

    left =0
    length = len(arr)
    position = -1
    rigth = length - 1

    for left in range(0,length,1):
        if arr[left] == search_element:
            position = left
            print('encontrado en la posicion'+str(position+1)+' en '+str(left+1)+' pasos')
            break
        if arr[rigth] == search_element:
            position = rigth
            print('encontrado en la posicion'+str(position+1)+' en '+str(length-rigth)+' pasos')
            break
        left = left +1
        rigth = rigth -1
    if position == -1:
        print(' elemento no encontrado')

arr = [1,2,3,4,5]
buscar = 5
search(arr,buscar)



def binarysearch(arr,l,r,x):
# LA BUSQUEDA BINARIA ES UN MÉTODO EFICIENTE PARA ENCONTRAR UN ELEMENTO
# EN UN ARRAY SIEMPRE QUE ÉSTE SE ENCUENTRE ORDENADO PREVIAMENTE.
# CONSISTE EN DIVIDIR CONTINUAMENTE POR 2 EL ARRAY DONDE SE ESTÁ BUSCANDO
# CONOCIENDO DONDE SE PODRÍA ENCONTRAR EL ELEMENTO A BUSCAR 
# SI SABEMOS QUE EL VALOR ACTUAL ES MAYOR O MENOR QUE EL BUSCADO.
# LA COMPLEJIDAD DEL ALGORIMO ES O(log2n)
    pasos = 0
    while l<=r:
        mid = l + ( r - l ) // 2
        pasos = pasos +1
        if arr[mid] == x:
            print('pasos '+ str(pasos))
            return mid
        
        if arr[mid] < x:
            l = mid + 1
            
        else:
            r = mid - 1
    return -1 

arr = [1,2,3,4,5]
x = 5
result = binarysearch(arr,0,len(arr)-1,x)
if result != -1:
    print( ' el numero '+str(x)+' se ha encontrado en la posicion '+str(result))
else:
    print("elemento no encontrado")

        
        
