from helpers.graficas import Grafica
import numpy as np

from helpers.arreglos import ObtieneMenor
from helpers.operaciones import ObtieneDistancias
import os

def DistanciaMinima( vector, arregloMedias, arregloClases ):
    distDir = ObtieneDistancias(vector, arregloMedias )
    distanciaMin = ObtieneMenor( distDir )

    print( 'El vector desconocido ', vector, 'pertenece a la clase ', distanciaMin  )
    Grafica( vector, arregloClases )