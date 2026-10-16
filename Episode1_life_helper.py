import numpy as np
import copy

def cn(Z):
    shape = len(Z), len(Z[0])
    N = [[0, ] * (shape[0]) for i in range(shape[1])]
    for x in range(1, shape[0] - 1):
        for y in range(1, shape[1] - 1):
            N[x][y] = Z[x - 1][y - 1] + Z[x][y - 1] + Z[x + 1][y - 1] \
                      + Z[x - 1][y] + Z[x + 1][y] \
                      + Z[x - 1][y + 1] + Z[x][y + 1] + Z[x + 1][y + 1]
    return N


def it(Z):
    N = cn(Z)
    for x in range(len(Z)):
        for y in range(len(Z[0])):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
    return Z


def game_of_life(Z, T):
    try:
        shape = Z.shape
        Zh = np.empty((T, shape[0], shape[1]))
        for t in range(T):
            Zh[t] = Z
            Z = it(Z)
        return Zh
    except:
        pass


def itp(Z, dZ):
    N = cn(Z)
    for x in range(len(Z)):
        for y in range(len(Z[0])):
            if N[x][y] == 8 and Z[x][y] == 1:
                dZ[x][y] = 1 
                Z[x][y] = 0
            elif Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            if Z[x][y] == 1 and dZ[x][y] == 1:
                Z[x][y] = 0
                dZ[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
    return Z, dZ


def game_of_life_plus(Z, T):
    try:
        shape = Z.shape
        dZ = np.zeros_like(Z)
        Zh = np.empty((T, shape[0], shape[1]))
        for t in range(T):
            Zh[t] = Z
            Z, dZ = itp(Z, dZ)
        return Zh
    except:
        pass

def gols(Z, T):
    shape = Z.shape
    dZ = np.zeros_like(Z)
    Zh = np.empty((T, shape[0], shape[1]))
    Zdh = np.empty((T, shape[0], shape[1]))
    for t in range(T):
        Zh[t] = Z
        Zdh[t] = dZ
        Z, dZ = itp(Z, dZ)
    return Zh, Zdh

