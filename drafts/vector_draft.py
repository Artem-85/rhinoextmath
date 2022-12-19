

from math import *

def vector(a,b=None):
    c = []
    for i in range(3):
        c.append(b[i] - a[i] if b != None else a[i])
    return c

def vectcrossmul(a,b):
    c = []
    c.append(a[1]*b[2] - a[2]*b[1])
    c.append(a[2]*b[0] - a[0]*b[2])
    c.append(a[0]*b[1] - a[1]*b[0])
    return c

def vectdotmul(a,b):
    d = 0.0
    for i in range(3):
        d += b[i] * a[i]
    return d

def vectsum(a,b):
    c = []
    for i in range(3):
        c.append(b[i] + a[i])
    return c

def vectlen(a):
    d = sqrt(a[0]**2 + a[1]**2 + a[2]**2)
    return d

def unitizevect(a):
    d = vectlen(a)
    c = []
    for i in range(3):
        c.append(a[i]/d)
    return c

def vectsub(a,b):
    c = []
    for i in range(3):
        c.append(a[i] - b[i])
    return c

def matrfrom2vect(a,b):
    c = []
    for i in range(3):
        c.append([])
        for j in range(2):
            c[i].append(a[i] if j == 0 else b[i])
    return c

def transposematr(a):
    b = []
    for j in range(len(a[0])):
        b.append([])
        for i in range(len(a)):
            b[j].append(a[i][j])
    return b

def matmul(a, b):
    c = []
    rowsNum = len(a)
    colNum = len(b[0]) if (type(b[0]) is list) else 1
    for i in range(rowsNum):
        c.append([])
        for j in range(colNum):
            c_new = 0.0
            for k in range(rowsNum):
                c_new += a[i][k] * (b[k][j] if colNum > 1 else b[k])
            if colNum == 1:
                c[i] = c_new
            else:
                c[i].append(c_new)
    return c

# def inverse(a):
#     if len(a) != len(a[0]):
#         return None
#     else:
#         N = len(a)
#     copyA = copymatrix(a) 
#     L = identity(N)
#     U = matrix(N, N) 
#     B = matrix(N)
#     D = matrix(N)
#     X = matrix(N)
#     invA = matrix(N, N)
# # STEP 1: FORWARD ELIMINATION
#     for k in range(N - 1):
#         for i in range(k + 1, N):
#             coeff = copyA[i][k]/copyA[k][k]
#             L[i][k] = coeff
#             for j in range(k + 1, N):
#                 copyA[i][j] = copyA[i][j] - coeff*copyA[k][j]
# # STEP 2: PREPARE L AND U MATRICES 
# # L MATRIX IS A MATRIX OF THE ELIMINATION COEFFICIENT 
# # THE DIAGONAL ELEMENTS ARE 1.0
# # U MATRIX IS THE UPPER TRIANGULAR PART OF copyA
#     for j in range(N):
#         for i in range(j + 1):
#             U[i][j] = copyA[i][j]
# # STEP 3: COMPUTE COLUMNS OF THE INVERSE MATRIX OUTAR
#     for k in range(N):
#         B[k] = 1.0
#         D[0] = B[0]
# # STEP 3A: SOLVE LD=B USING THE FORWARD SUBSTITUTION
#         for i in range(1,N):
#             D[i] = B[i]
#             for j in range(i):
#                 D[i] = D[i] - L[i][j]*D[j]
# # STEP 3B: SOLVE UX=D USING THE BACK SUBSTITUTION
#         X[N - 1] = D[N - 1]/U[N - 1][N - 1]
#         for i in range(N - 2, -1, -1):
#             X[i] = D[i]
#             for j in range(N - 1, i, -1):
#                 X[i] = X[i] - U[i][j]*X[j]
#             X[i] = X[i]/U[i][i]
# # STEP 3C: FILL THE SOLUTIONS X(DIM) INTO COLUMN K OF OUTAR
#         for i in range(N):
#             invA[i][k] = X[i]
#         B[k] = 0.0
#     return invA

ptA = [0.2, 12.4, 4.5]

ptB = [4.1, -5.9, 11.5]

ptC = [12.3, -1.0, -4.7]

vectA = vector(ptA)
vectB = vector(ptB)
vectC = vector(ptC)

norm = vectsum(vectcrossmul(vectA,vectB), vectcrossmul(vectB,vectC))
norm = vectsum(norm, vectcrossmul(vectC,vectA))
unit = unitizevect(norm)

vectU = vectcrossmul(vectsub(vectC,vectA),unit)
vectV = vectcrossmul(unit,vectU)

vectU = unitizevect(vectU)
vectV = unitizevect(vectV)

R = matrfrom2vect(vectU,vectV)
Rt = transposematr(R)

vecta = matmul(Rt,vectA)
vectb = matmul(Rt,vectB)
vectc = matmul(Rt,vectC)

#coefMatr = [[],
#    []]

print(ptA)
print(ptB)
print(ptC)

print(norm)


d = vectdotmul(unit,vectA)



print(unit)
print(d)
print(vectU)
print(vectV)
print(R)
print(Rt)
print(vecta)
print(vectb)




