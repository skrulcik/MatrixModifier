#/bin/python

from numpy import *


class Matrix:
    def __init__(self, rows=0, cols=0, verbose=True, baseOne=True):
        """ Instantiates Matrix of size rows x cols
            verbose: True if output should be printed on each line
            baseOne: True if matrix row/column indices should start at index 1
            Both of the default values for the above parameters are "True"
            """
        self.model = zeros((rows, cols), dtype=float)
        self.verbose = verbose
        # BaseOne allows users to refer to the first element in the
        # row or column as '1' rather than '0' as the program sees it
        # accessing the 'model' requires using 0, so we should prevent
        # the user from ever accessing it to avoid confusion
        self.baseOne = baseOne
        
    def swap(self, r1, r2):
        r1 -= self.baseOne
        r2 -= self.baseOne
        assert r1>=0 and r1 < len(self.model)
        assert r2>=0 and r2 < len(self.model)
        store = copy(self.model[r1])
        self.model[r1] = copy(self.model[r2])
        self.model[r2] = store
        print(self.model) if self.verbose else None

    def rowAddOther(self, row, other, co):
        row -= self.baseOne
        other -= self.baseOne
        assert 0 <= row and row <len(self.model)
        assert 0 <= other and other < len(self.model)
        self.model[row] = self.model[row]+self.model[other]*co
        print(self.model) if self.verbose else None
        
    def rowScale(self, row, co):
        row -= self.baseOne
        assert 0 <= row and row <len(self.model)
        self.model[row]*=co
        print(self.model) if self.verbose else None

    def get(self,r,c):
        r -= self.baseOne
        c -= self.baseOne
        assert r>=0 and r < len(self.model)
        assert c>=0 and c < len(self.model[r])
        return self.model[r][c]
    def set(self,r,c,val):
        r -= self.baseOne
        c -= self.baseOne
        assert r>=0 and r < len(self.model)
        assert c>=0 and c < len(self.model[r])
        self.model[r][c] = val
        

def CreateMatrix(mtrx, verbose=True):
    A = Matrix(len(mtrx), len(mtrx[0]), verbose)
    A.model = mtrx
    return A

def randMatrix(row, col, verbose=True, floor=-99, ceiling=99):
    A = Matrix(row,col,verbose)
    for r in range(row):
        for c in range(col):
            A.model[r][c] = random.randint(floor, ceiling)
    return A

