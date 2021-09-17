from knn import nearestNeibors
from helpers.graficas import grafica3D
from mahalanobis import Mahalanobis
from Practica2 import MaximaProbabilidad
import numpy as np

from Practica1 import DistanciaMinima
from helpers.operaciones import CalculaVarianzas3D, ObtieneMedia
from helpers.arreglos import CreaArregloClases


while True:

    dimension = int( input( '¿En que dimension deseas trabajar? 0 = 2D | 1 = 3D' ) )
    cantClases = int(input('¿Cuantas clases quieres?'))
    repClase = int(input('¿Cuantos representantes quieres por clase?'))
    if( dimension == 0 ):    
        arregloClases = CreaArregloClases( cantClases, repClase, 2 )
        # arregloClasesPrueba = [[[ 0 ,0 ,1 ,0 ,2],[0 ,1 ,1 ,1 ,1]],
        #                 [[ 5,5,4,6,6 ],[ 5,6,5,5,4]],
        #                 [[ 9,10,11,10,9 ],[ 10,11,9,12,12]]]
        # arregloClases = np.array( arregloClasesPrueba )
        arregloMedias = ObtieneMedia( arregloClases )

        while True:
            vx = float( input( 'Ingresa la cordenada x del vector' ) )
            vy = float( input( 'Ingresa la cordenada y del vector' ) )

            vector = np.array([ vx, vy ])

            clasficador = int( input( '¿Con que clasificador lo quieres probar? 1=Distancia Minima | 2=Maxima Probabilidad | 3=KNN' ) )
            if( clasficador == 1 ):
                DistanciaMinima( vector, arregloMedias, arregloClases )
            elif( clasficador == 2 ):
                MaximaProbabilidad( vector, arregloMedias, arregloClases )
            elif( clasficador == 3 ):
                nearestNeibors( vector, arregloClases )
            
            volverIntentar = int( input( '¿Quieres probar otro vector? 0= No | 1= Si' ) )
            if( volverIntentar == 0 ):
                break
    elif( dimension == 1 ):
        arregloClases = CreaArregloClases( cantClases, repClase, 3 )
        # arregloClases = np.array([
        #     [[0, 0, 1, 0, 2],[ 0, 1, 1, 1, 1]],
        #     [[5, 5, 4, 6, 6], [5, 6, 5, 5, 4]]
        # ])
        arregloMedias =  ObtieneMedia( arregloClases )
        arregloVarianzas = CalculaVarianzas3D( arregloClases, arregloMedias )
        while True:
            vx = float( input( 'Ingresa la coordenada x del vector' ) )
            vy = float( input( 'Ingresa la coordenada y del vector' ) )
            vz = float( input( 'Ingresa la coordenada z del vector' ) )
            vector = np.array([ vx, vy, vz ])
            Mahalanobis( vector, arregloMedias, arregloVarianzas )
            grafica3D( vector, arregloClases )

            volverIntentar = int( input( '¿Quieres probar otro vector? 0= No | 1= Si' ) )
            
            if( volverIntentar == 0 ):
                break

