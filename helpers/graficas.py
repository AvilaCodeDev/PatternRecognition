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

def grafica3D( vector, arreClases ):
    fig = plt.figure()
    ax = fig.add_subplot( projection = '3d' )

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    colors = ['bo', 'go', 'ro', 'co', 'mo', 'yo']
    for i in range( 0, arreClases.shape[0]):
        ax.scatter( arreClases[i][0,:], arreClases[i][1,:], arreClases[i][2,:], colors[i], label= "Clase " + str( i + 1 ) )
    
    ax.scatter( vector[0], vector[1], vector[2], 'bo' , label="Vector" )
    plt.legend()
    plt.show()