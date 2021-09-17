from helpers.arreglos import ObtieneMenor
import math
import numpy as np


def Mahalanobis( vector, arregloMedias, arregloVarianzas ):
    distDiccinario = {}
    for i in range( arregloMedias.shape[0] ):
        ffx = vector[0] - arregloMedias[i][0]
        ffy = vector[1] - arregloMedias[i][1]
        ffz = vector[2] - arregloMedias[i][2]
        
        distancia = np.matmul([ ffx, ffy, ffz] , np.matmul( np.linalg.inv( arregloVarianzas[ i ] ) , [ ffx, ffy, ffz ] ))
        distDiccinario['Clase ' + str(i + 1)] = distancia
    
    valor = ObtieneMenor( distDiccinario )
    print(distDiccinario)

    print( ' El vector desconocido ', vector, ' pertenece a la ', valor )


        

