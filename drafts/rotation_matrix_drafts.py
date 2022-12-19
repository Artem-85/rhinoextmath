from math import *

PRECISION = 1.e-6

class Matrix:
    def __init__(self,n, m = None, x = 0):
        self.__matrix = [[float(x)] * m for i in range(n)] if m != None else [float(x) for i in range(n)]

    def __str__(self):
        out = ''
        for i in range(len(self.__matrix)):
            out += "| {:0.6f} {:0.6f} {:0.6f} |\n".format(*self.__matrix)
        return out

#     def __setitem__(self, itemNo, data):
#          self.__matrix[itemNo] = data


    def __getitem__(self, itemNo):
        i, j = itemNo
        return self.__matrix[i][j]

def matmul(a, b):
    c = []
    rowsNum = len(a)
    for i in range(rowsNum):
        colNum = len(b[i]) if (type(b[i]) is list) else 1
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

def matrix(n, m = None, x = 0):
    return [[x] * m for i in range(n)] if m != None else [x for i in range(n)]

def identity(n):
    a = []
    for i in range(n):
        a.append([])
        for j in range(n):
            a[i].append(1.0 if i == j else 0.0)
    return a

def rotation(axis='x',angle=0):
    if axis not in 'xyz' and len(axis) > 1:
        return None
    flag = ord(axis) - 120
    r = []
    sign = 1 if flag == 1 else -1
    for i in range(3):
        r.append([])
        for j in range(3):
            if i == j and i == flag:
                val = 1.0
            elif i == flag or j == flag:
                val = 0.0
            elif i == j:
                val = cos(radians(angle)) if abs(cos(radians(angle))) > PRECISION else 0.0
            else:
                val = sign*sin(radians(angle)) if abs(sin(radians(angle))) > PRECISION else 0.0
                sign *= -1
            r[i].append(val)
    return r

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


a = [[1,2],
    [3,4]]

b = [[5,6],
    [7,8]]

b = [5, 7]

c = matmul(a,b)

#m = Matrix(3,x=1)

#d = matmul(a,m)

#print(c)
#
#print(matrix(3,x=1))
#
#print(identity(3))
#
#print(rotation(axis='x',angle=30))

A = 45

C = 30

Rx = rotation('x',A)

Rz = rotation('z',C)

print('Rx:')
for row in Rx:
    print("| {:0.6f} {:0.6f} {:0.6f} |".format(*row))

print('Rz:')
for row in Rz:
    print("| {:0.6f} {:0.6f} {:0.6f} |".format(*row))

R01 = matmul(Rx,Rz)

print('R01:')
for row in R01:
    print("| {:0.6f} {:0.6f} {:0.6f} |".format(*row))

alpha = acos(0.5*(R01[0][0] + R01[1][1] + R01[2][2] - 1))

print('alpha:')
print(degrees(alpha))

#print('Arc length:')
#print(alpha*)

p1 = (R01[2][1] - R01[1][2])/(2*sin(alpha)) if abs(sin(alpha)) > PRECISION else 1.0
p2 = (R01[0][2] - R01[2][0])/(2*sin(alpha)) if abs(sin(alpha)) > PRECISION else 1.0
p3 = (R01[1][0] - R01[0][1])/(2*sin(alpha)) if abs(sin(alpha)) > PRECISION else 1.0

if p1 == p2 == p3 == 1.0:
    p1 = p2 = p3 = 0.0

print('p1 = {:.2f}'.format(p1))
print('p2 = {:.2f}'.format(p2))
print('p3 = {:.2f}'.format(p3))
#print(m[0, 0])