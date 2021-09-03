import numpy as np
import random

# arregloClasesPrueba = [[[ 0 ,0 ,1 ,0 ,2],[0 ,1 ,1 ,1 ,1]],
#                 [[ 5,5,4,6,6 ],[ 5,6,5,5,4]],
#                 [[ 9,10,11,10,9 ],[ 10,11,9,12,12]]]

def CreaArregloClases( numeroClases, numeroRepClase ):
    arregloClases = []
    for i in range( 0, numeroClases ):
        centroide = int(input( 'Dame el centroide de la clase ' + str( i + 1 ) + ' : ' ))
        dispersion = int(input( 'Ingrese la dispersion de la clase' + str( i + 1 ) + ' : ' ))
        arregloClases.append( np.random.normal( centroide , dispersion , (2, numeroRepClase)) )
    return np.array(arregloClases)

def ObtieneMenor( distDir ):
    return min( distDir , key = distDir.get )

def ObtieneMayor( arreglo ):
    return max( arreglo , key = arreglo.get )