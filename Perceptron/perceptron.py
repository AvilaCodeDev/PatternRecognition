import numpy as np
import matplotlib.pyplot as plt
from os import system
from mpl_toolkits import mplot3d


def fun(x, y):
    return (3/2) * (x - y) + 1


def perceptron_cubo():

    c1 = np.array([[1, 0, 1, 1], [0, 0, 0, 1], [1, 0, 0, 0]])
    c2 = np.array([[0, 0, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]])

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.scatter(c1[0], c1[1], c1[2], 'bo', label='clase1')
    ax.scatter(c2[0], c2[1], c2[2], 'go', label='clase2')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Condiciones iniciales
    ws = np.array([1, 1, 1, 1]).reshape(4, 1)
    r = 1
    additional_input = 1

    iteracion = 0

    while True:
        correcciones = 0
        print(f'Iteracion {iteracion}')

        # Clase 1
        for i in range(len(c1)):
            Xn = np.array([c1[0][i], c1[1][i], c1[2][i],
                          additional_input]).reshape(4, 1)
            f_out = Xn.transpose() @ ws

            if(f_out[0] >= 0):
                ws = ws - (1 * Xn)
                print('Se cumple 1, entonces: \n')
                print([f'w{i} = {ws[i][0]}' for i in range(len(ws))], '\n')
                correcciones += 1

        # Clase2
        for i in range(len(c2)):
            Xn = np.array([c2[0][i], c2[1][i], c2[2][i],
                          additional_input]).reshape(4, 1)
            f_out = Xn.transpose() @ ws

            if(f_out[0] <= 0):
                ws = ws + (1 * Xn)
                print('Se cumple 2, entonces: \n')
                print([f'w{i} = {ws[i][0]}' for i in range(len(ws))], '\n')
                correcciones += 1

        if correcciones == 0:
            break

        iteracion += 1

    print('Ws finales: \n')
    print([f'w{i} = {ws[i][0]}' for i in range(len(ws))])

    x = np.linspace(0, 1, 50)
    y = np.linspace(0, 1, 50)

    X, Y = np.meshgrid(x, y)

    ax.plot_surface(X, Y, fun(X, Y))


def perceptron_and():
    ws = np.array([0,0,0]).reshape(3, 1)
    r = 1
    additional_input = np.array([1])
    c1 = np.array([[5,5,4], [5,6,5]])
    c2 = np.array([[0, 0, 1],  [0, 1, 0]])

    i = 1

    while True:
        correcciones = 0
        print(f'\nIteracion {i}:')

        # Clase 1
        for i in range(len(c1)):
            Xn = np.array([c1[0][i], c1[1][i], additional_input]).reshape(3, 1)
            f_out = Xn.transpose() @ ws

            if(f_out[0] >= 0):
                print('Se cumple 1, entonces:')
                ws = ws - (1 * Xn)
                print([f'w{i} = {ws[i][0]}' for i in range(len(ws))], '\n')
                correcciones += 1

        # Clase2

        for i in range(len(c2)):
            Xn = np.array([c2[0][i], c2[1][i],
                          additional_input]).reshape(3, 1)
            f_out = Xn.transpose() @ ws

            if(f_out[0] <= 0):
                print('Se cumple 2, entonces:')
                ws = ws + (1 * Xn)
                print([f'w{i} = {ws[i][0]}' for i in range(len(ws))], '\n')
                correcciones += 1

        i += 1

        if correcciones == 0:
            break

    print('Ws finales: \n')
    print([f'w{i} = {ws[i][0]}' for i in range(len(ws))])

    y = ws[2][0][0]
    x = ws[0][0]

    punto1 = [ 0, y ]
    punto2 = [ -(x/y) , 0]

    plt.plot(c1[0], c1[1], 'ro', label='Clase1')
    plt.plot(c2[0], c2[1], 'go', label='Clase2')
    plt.plot(punto1, punto2, label='Linea de separabilidad')

    plt.title('Perceptron AND')


while True:
    system('clear')
    ans = input('Eliga una opcion: \n1.and\n2.cubo\n3.Salir\n')

    if ans == '1':
        perceptron_and()
    elif ans == '2':
        perceptron_cubo()
    else:
        break

    plt.legend()
    plt.show()
