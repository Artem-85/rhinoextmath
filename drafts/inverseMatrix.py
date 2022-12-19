import numpy
class Matrix:

    def __init__(self):
        pass

def identity(n):
    a = []
    for i in range(n):
        a.append([])
        for j in range(n):
            a[i].append(1.0 if i == j else 0.0)
    return a

def matrix(n, m = None, x = 0.0):
    return [[x] * m for i in range(n)] if m != None else [x for i in range(n)]

def copymatrix(a):
    b = []
    for i in range(len(a)):
        if type(a[0]) is list:
            b.append([])
            for j in range(len(a[0])):
                b[i].append(a[i][j])
        else:
            b.append(a[i])
    return b

# This is based on the Fortran code found somewhere on the net.
# I don't remember the author's name, please contact me if it's your code and you'd like to be credited here
def inverse(a):
    if len(a) != len(a[0]):
        return None
    else:
        N = len(a)
    copyA = copymatrix(a) 
    L = identity(N)
    U = matrix(N, N) 
    B = matrix(N)
    D = matrix(N)
    X = matrix(N)
    invA = matrix(N, N)
# STEP 1: FORWARD ELIMINATION
    for k in range(N - 1):
        for i in range(k + 1, N):
            coeff = copyA[i][k]/copyA[k][k]
            L[i][k] = coeff
            for j in range(k + 1, N):
                copyA[i][j] = copyA[i][j] - coeff*copyA[k][j]
# STEP 2: PREPARE L AND U MATRICES 
# L MATRIX IS A MATRIX OF THE ELIMINATION COEFFICIENT 
# THE DIAGONAL ELEMENTS ARE 1.0
# U MATRIX IS THE UPPER TRIANGULAR PART OF copyA
    for j in range(N):
        for i in range(j + 1):
            U[i][j] = copyA[i][j]
# STEP 3: COMPUTE COLUMNS OF THE INVERSE MATRIX OUTAR
    for k in range(N):
        B[k] = 1.0
        D[0] = B[0]
# STEP 3A: SOLVE LD=B USING THE FORWARD SUBSTITUTION
        for i in range(1,N):
            D[i] = B[i]
            for j in range(i):
                D[i] = D[i] - L[i][j]*D[j]
# STEP 3B: SOLVE UX=D USING THE BACK SUBSTITUTION
        X[N - 1] = D[N - 1]/U[N - 1][N - 1]
        for i in range(N - 2, -1, -1):
            X[i] = D[i]
            for j in range(N - 1, i, -1):
                X[i] = X[i] - U[i][j]*X[j]
            X[i] = X[i]/U[i][i]
# STEP 3C: FILL THE SOLUTIONS X(DIM) INTO COLUMN K OF OUTAR
        for i in range(N):
            invA[i][k] = X[i]
        B[k] = 0.0
    return invA


test = matrix(3, 3, 1)
test[0][1] = 2.6
test[2][1] = -1.23
test[0][0] = -8.3
test[0][0] =  1.50000
test[0][1] =  3.20000
test[0][2] =  4.50000    
test[1][0] = 7.6
test[1][1] = -1.20
test[1][2] = 2.5000000000000000
test[2][0] = -1.5000000000000000        
test[2][1] = 3.9000
test[2][2] = -9.10

# nar = numpy.array(test)
# nar_1 = numpy.linalg.inv(nar)
# print(nar)
# print(nar_1)

test2 = copymatrix(test)
print(test)
print(test2)
print(test is test2)

test = [[2.5, 6.7],[-1.2, 0.8]]

nar = numpy.array(test)
nar_1 = numpy.linalg.inv(nar)
print(nar)
print(nar_1)

test_1 = inverse(test)
print('test_1',test_1)

# print(repr(test))
# print(str(test))