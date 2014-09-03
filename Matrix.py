#/bin/python

from numpy import *


class Matrix:
    def __init__(self, rows=0, cols=0, verbose=True):
        self.model = zeros((rows, cols))
        self.verbose = verbose
    def swap(self, r1, r2):
        assert r1>=0 and r2>=0
        assert r1 < len(self.model) and r2 < len(self.model[0])
        store = copy(self.model[r1])
        self.model[r1] = copy(self.model[r2])
        self.model[r2] = store
        print(self.model) if self.verbose else None

def randMatrix(row, col, verbose=True, floor=-99, ceiling=99):
    A = Matrix(row,col,verbose)
    for r in range(row):
        for c in range(col):
            A.model[r][c] = random.randint(floor, ceiling)
    return A
    
A = randMatrix(3,4)
print A.model
print "swap 1 and 2"
A.swap(1,2)
