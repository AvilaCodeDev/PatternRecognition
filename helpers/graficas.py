import matplotlib.pyplot as plt
import random

def Grafica( vector, arregloClases ):
    colors = ['bo', 'go', 'ro', 'co', 'mo', 'yo']
    for i in range( 0, arregloClases.shape[0] ):
        color = random.choice( colors )
        plt.plot(arregloClases[i][0,:], arregloClases[i][1,:] , colors[i] , label = "Clase " + str( i + 1 )  )
    plt.plot( vector[0], vector[1], 'ko', label="Vector" )
    plt.legend()
    plt.show()