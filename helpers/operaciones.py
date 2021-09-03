import numpy as np

def ObtieneMedia( arregloClases ):
    meanArray = []
    for i in range( 0 , arregloClases.shape[0] ):
        meanArray.append(np.mean( arregloClases[i], axis = 1))
    return np.array(meanArray) 

def ObtieneDistancias( vector , meanArray ):
    distDir = {}
    for i in range( 0 , meanArray.shape[0] ):
        distDir['clase ' + str( i + 1 )] = np.linalg.norm( vector - meanArray[i] )
    return distDir

def CalculaVarianzas( arregloClases, arregloMedias ):
    arregloVarianzas = []
    for i in range( 0 , arregloClases.shape[0] ):
        dato_x = arregloClases[i][0,:] - arregloMedias[i][0]
        dato_y = arregloClases[i][1,:] - arregloMedias[i][1]

        dato1 = np.array([ dato_x, dato_y ])
        dato2 = np.array( np.transpose( dato1 ) )

        varianza = np.array( (1/5)*np.matmul( dato1 , dato2 ) )

        arregloVarianzas.append( varianza )
    
    return np.array( arregloVarianzas )
