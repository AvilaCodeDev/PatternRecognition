from Practica2 import MaximaProbabilidad
import numpy as np

from Practica1 import DistanciaMinima
from helpers.operaciones import ObtieneMedia
from helpers.arreglos import CreaArregloClases


cantClases = int(input('¿Cuantas clases quieres?'))
repClase = int(input('¿Cuantos representantes quieres por clase?'))

arregloClases = CreaArregloClases( cantClases, repClase )
# arregloClasesPrueba = [[[ 0 ,0 ,1 ,0 ,2],[0 ,1 ,1 ,1 ,1]],
#                 [[ 5,5,4,6,6 ],[ 5,6,5,5,4]],
#                 [[ 9,10,11,10,9 ],[ 10,11,9,12,12]]]
# arregloClases = np.array( arregloClasesPrueba )
arregloMedias = ObtieneMedia( arregloClases )

while True:
    vx = int( input( 'Ingresa la cordenada x del vector' ) )
    vy = int( input( 'Ingresa la cordenada y del vector' ) )

    vector = np.array([ vx, vy ])

    clasficador = int( input( '¿Con que clasificador lo quieres probar? 1=Distancia Minima | 2=Maxima Probabilidad' ) )
    if( clasficador == 1 ):
        DistanciaMinima( vector, arregloMedias, arregloClases )
    elif( clasficador == 2 ):
        MaximaProbabilidad( vector, arregloMedias, arregloClases )
    
    volverIntentar = int( input( '¿Quieres probar otro vector? 0= No | 1= Si' ) )
    
    if( volverIntentar == 0 ):
        break