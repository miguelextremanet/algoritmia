import numpy as np
from time import time


###############################################
## MIGUEL ANGEL GARCÍA 2º BATXELOR INFORMATICA
###############################################

    
        
def MULTIPLICA_2MATRICES(F, M):    
    # ESTA FUNCIÓN PODRÍA HACERSE CON VARIOS BLUCLES FOR UNO DENTRO DE OTRO
    
    fila = 0;        
    a = (F[fila][0] * M[0][0] + F[fila][1] * M[1][0] + F[fila][2] * M[2][0])    
    b = (F[fila][0] * M[0][1] + F[fila][1] * M[1][1] + F[fila][2] * M[2][1])    
    c = (F[fila][0] * M[0][2] + F[fila][1] * M[1][2] + F[fila][2] * M[2][2])
    
    fila = 1;        
    d = (F[fila][0] * M[0][0] + F[fila][1] * M[1][0] + F[fila][2] * M[2][0])    
    e = (F[fila][0] * M[0][1] + F[fila][1] * M[1][1] + F[fila][2] * M[2][1])    
    f = (F[fila][0] * M[0][2] + F[fila][1] * M[1][2] + F[fila][2] * M[2][2])
    
    
    fila = 2;        
    g = (F[fila][0] * M[0][0] + F[fila][1] * M[1][0] + F[fila][2] * M[2][0])    
    h = (F[fila][0] * M[0][1] + F[fila][1] * M[1][1] + F[fila][2] * M[2][1])    
    i = (F[fila][0] * M[0][2] + F[fila][1] * M[1][2] + F[fila][2] * M[2][2])
    
    #ASIGNAMOS EL RESULTADO DE LAS OPERACIONES
              
    F[0][0] = a
    F[0][1] = b
    F[0][2] = c
    
    F[1][0] = d
    F[1][1] = e
    F[1][2] = f

    F[2][0] = g
    F[2][1] = h
    F[2][2] = i

            
def POTENCIA(F, n):
 
 
    M = [
            [0, 1, 1], 
            [1, 0, 0], 
            [0, 1, 0]
        ]; 

    if (n <= 3):
        return;
        
    
    # PRIMERO SACAMOS LA PONTENCIA NORMAL     
    POTENCIA(F, n/2);     
    MULTIPLICA_2MATRICES(F, F);
    
    if (n % 2 != 0):        
        MULTIPLICA_2MATRICES(F, M);
        
    
    #El truco consiste en dividirlo, 
    #utilizando el exponente de 2 previo 
    #Y multiplicar esta matriz dos vec5e
    
    #Si la división por 2 no es entera 
    #(no es un múltiplo de 2), 
    #nos falta multiplicar 
    #la potencia de 2 previa por la matrix (una vez)
    #EN TÉRMINOS DE ESPACIO EL COSTE ES CONSTANTE
  

def PADOVAN_MEDIANTE_MATRICES(n):
      ## SECUENCIA PADOVAN ES : P(n) = P(n-2) + P(n-3)
      ## se incialzan los primeros valores a 1 
      ## P(0) = P(1) = P(2) = 1 
  
    momento_inicio = time()
    print ('*****************************')
    print ('INICIO PADOVAN USANDO MATRICES')
    print ('*****************************')
    F = [
            [0, 1, 1], 
            [1, 0, 0], 
            [0, 1, 0]
        ]; 

    POTENCIA(F, n-2);

   #MULTIPLICAMOS POR LA MATRIZ 1,1,1
    F1 = [[1, 0, 0],[1, 0, 0], [1, 0, 0]]; 
    
    MULTIPLICA_2MATRICES(F, F1);
    
        
    
    print ('VECTOR RESULTADO')
    for i in range(3):
        contenido_fila="FILA "+str(i)+" [";
        for j in range(3):
            contenido_fila+=str(F[i][j]) 
            if j<2:
                contenido_fila+=","                
        contenido_fila+="]";                    
        print(contenido_fila) 
        
    
    valor  = F[0][0]+ F[1][0] + F[2][0];

    
    momento_fin = time()    
    tiempo_que_tarda = (momento_fin - momento_inicio) 
    
    print ('*****************************')
    print(f"TÉRMINO PADOVAN ES :{valor}"); 
    print ('FIN DE PADOVAN MEDIANTE MATRICES')
    print(f"Tiempo que tarda mediante MATRICES: {tiempo_que_tarda}")
    print ('*****************************')
        



  

def PADOVAN_MEDIANTE_ARRAYS(n):
    ## ESTE ALGORITMO RESUELVE MEDIANTE ARRAYS LA SECUENCIA PADOVAN
    
    ## ES MAS COSTOSO EN TERMINOS DE ESPACIO Y TIEMPO 
    print ('*****************************')
    print ('INICIO PADOVAN USANDO ARRAYS')
    print ('*****************************')
    momento_inicio = time()
    F=[1,1,1]
    
    for i in range(3,n):
        F.append(F[i-2] + F[i-3])        
    
    for j in range(0,len(F)):
        print(F[j])
    momento_fin = time()
    
    tiempo_que_tarda = (momento_fin - momento_inicio)
    print ('*****************************')
    print ('FIN DE PADOVAN MEDIANTE ARRAYS')
    print(f"Tiempo que tarda mediante ARRAY: {tiempo_que_tarda}")
    print ('*****************************')


##############################################
## 2º FORMA DE HACERLO MEDIANTE BUCLE SIMPLE
##############################################
def PADOVAN_MEDIANTE_BUCLE(n):
    momento_inicio = time()
    print ('*****************************')
    print ('INICIO PADOVAN MEDIANTE BUCLE')
    print ('*****************************')
    ## Aqui solo almacenamos 4 variables simples y la i para la iteración
    ## ES MENOS COSOTO EN TÉRMINOS DE ESPACIO
    # El tiempo es O(n)
    
    P1 = 1
    print (P1)     
    P2 = 1
    print (P2)     
    P3 = 1
    print (P3)     
    
    PNUEVO_VALOR = 1
    for i in range(3, n):
        PNUEVO_VALOR = P1 + P2
        P1 = P2
        P2 = P3
        P3 = PNUEVO_VALOR 
        print (PNUEVO_VALOR)     
    momento_fin = time()
    tiempo_que_tarda = (momento_fin - momento_inicio)
    print ('*****************************')
    print ('FIN DE PADOVAN MEDIANTE BUCLE')
    print(f"Tiempo que tarda mediante bucle for: {tiempo_que_tarda}")
    print ('*****************************')
    
    
N =int(input('Introduce un número positivo:'))
PADOVAN_MEDIANTE_BUCLE(N)
PADOVAN_MEDIANTE_ARRAYS(N)
PADOVAN_MEDIANTE_MATRICES(N)

