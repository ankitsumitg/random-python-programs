# EMPTY=VACIO
# TREE=ARBOL
# BURNT=QUEMADO

n = 10000  # n trees
n_rep = 50  # years that a population of trees grow
f = 0.025  # probability that a lightning strike
p = 0.025  # another probability

import random
import numpy as np
import matplotlib.pyplot as plt

VACIO = 0
ARBOL = 1
QUEMADO = -1


def generar_bosque_vacio(n):
    bosque = []
    for i in range(n):
        bosque.append(VACIO)
    return bosque


def suceso_aleatorio(p):
    if random.random() < p:
        return True
    else:
        return False


def suceso_aleatorio(prob):
    p = random.random()
    if p <= prob:
        return True
    else:
        return False


def brotes(bosque, p):
    for i in range(len(bosque)):
        if suceso_aleatorio(p) and bosque[i] == VACIO:
            bosque[i] = ARBOL
    return bosque


def cuantos(bosque, tipo_celda):
    cuenta = 0
    for i in range(len(bosque)):
        if bosque[i] == tipo_celda:
            cuenta = cuenta + 1
    return cuenta


def rayos(bosque, p):
    for i in range(len(bosque)):
        if suceso_aleatorio(p) and bosque[i] == ARBOL:
            bosque[i] = QUEMADO
    return bosque


def un_paso(b):
    for i in range(len(b)):
        if b[i] == ARBOL:
            if i > 0 and b[i - 1] == QUEMADO:
                b[i] = QUEMADO
            elif i < (len(b) - 1) and b[i + 1] == QUEMADO:
                b[i] = QUEMADO
    return b


def propagacion(bosque):
    bosque_0 = bosque.copy()
    bosque_1 = un_paso(bosque)
    while bosque_0 != bosque_1:  # Si un_paso no hizo nada, corto el while
        bosque_0 = bosque_1.copy()
        bosque_1 = un_paso(bosque_1)

    return bosque_1


def limpieza(bosque):
    for i in range(len(bosque)):
        if bosque[i] == QUEMADO:
            bosque[i] = VACIO
    return bosque


def ciclo_anual(bosque, p, f):
    bosque = brotes(bosque, p)
    bosque = rayos(bosque, f)
    bosque = propagacion(bosque)
    bosque = limpieza(bosque)

    return cuantos(bosque, ARBOL), bosque


n = 100
n_rep = 50
f = 0.02
p = 0.4

bosque = generar_bosque_vacio(n)


def evolucion(bosque, p, f, n_rep):
    narboles_lista = []
    for t in range(n_rep):
        narboles, bosque = ciclo_anual(bosque, p, f)
        narboles_lista.append(narboles)
    return narboles_lista, bosque


n = 10000
n_rep = 50
f = 0.025
p = 0.025

bosque = generar_bosque_vacio(n)

narboles, bosque = evolucion(bosque, p, f, n_rep)
años = np.array(range(n_rep))
narboles = np.array(narboles)

'''
plt.style.use('ggplot')
plt.xlabel('Número de ciclos (años)')
plt.ylabel('Número de árboles')
plt.title ('Cantidad de sobrevivientes en función de los años')
plt.plot(años, narboles, '-g')
plt.show()

'''
media = np.mean(narboles)
desvio = np.std(narboles)
print(media, desvio)

#Linear -> x vs y

plt.style.use('ggplot')
plt.xlabel('Número de ciclos (años)')
plt.ylabel('Número de árboles')
plt.title('Lineal')
anos2 = años[:21]
plt.plot(anos2, narboles[:len(anos2)])
plt.show()

# SemiLog -> ln(y) vs x

plt.style.use('ggplot')
plt.xlabel('Número de ciclos (años)')
plt.ylabel('Número de árboles')
plt.title ('Semi Logarítimica en y')
anos2 = años[:21]
plt.semilogx(anos2, narboles[:len(anos2)])
plt.show()

# LogLog -> ln(y) vs ln(x)

plt.style.use('ggplot')
plt.xlabel('Número de ciclos (años)')
plt.ylabel('Número de árboles')
plt.title('Ln(y) vs Ln(x)')
anos2 = años[:21]
plt.loglog(anos2, narboles[:len(anos2)])
plt.show()