from helpers.graficas import Grafica
from helpers.arreglos import Normalizar
from statistics import mode
import numpy as np

def nearestNeibors( vector, arregloClases ):
    diccionario = {}
    lista = []
    lista_vecinos = []
    for i in range( 0, arregloClases.shape[0] ):
        diccionario['Clase ' + str( i+1 )] = []
        for j in range( 0, arregloClases[i].shape[1] ):
            distancia = np.linalg.norm( vector - arregloClases[i][:,j] , 2 )
            lista.append(distancia)
            diccionario['Clase ' + str( i+1 )].append(distancia)
    lista.sort()
    k = int(input('Ingrese el valor de k: '))
    vecinos = lista[:k]
    for vecino in vecinos:
        print(vecino)
        for k, v in diccionario.items():
            if vecino in v:
                lista_vecinos.append(k)
    

    # print("El vector pertenece a la clase " + clases_vecinos[0])
    # print(diccionario)
    print("El vector pertenece a la clase " + mode(lista_vecinos))
    Grafica( vector, arregloClases )