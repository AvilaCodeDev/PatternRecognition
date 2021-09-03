from helpers.graficas import Grafica
from helpers.arreglos import ObtieneMayor
import math
import numpy as np

from helpers.operaciones import CalculaVarianzas


def MaximaProbabilidad( vector, arregloMedias, arregloClases ):
    arregloVarianzas = CalculaVarianzas( arregloClases, arregloMedias )
    proDir = {}
    for i in range( 0, arregloClases.shape[0] ):
        dato1 = ( 1 / ( 2 * math.pi ) ) * pow( np.linalg.det( arregloVarianzas[i] ), (-0.5) )
        h = vector - arregloMedias[i]
        h1 = np.transpose( h )
        inv_varianza = np.linalg.inv( arregloVarianzas[i] )
        dato2 = math.exp(-0.5*np.matmul( h, np.matmul(inv_varianza, h1) ))
        prob = dato1 * dato2
        proDir['clase ' + str( i + 1 )] = prob * 100

        print( prob )
    
    mayor_prob = ObtieneMayor( proDir )
    if( mayor_prob == 0.0 ):
        print( 'El vector ', vector, ' esta my alejado de las clases.' )
    else:
        print( 'El vector desconocido ', vector, 'pertenece a la clase ', mayor_prob  )
        Grafica( vector, arregloClases )

        