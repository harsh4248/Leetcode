class Solution:
        
    def makeRowZero(self,i,matrix):
        for ir in range(len(matrix[i])):
            matrix[i][ir] = 0
    def makeColZero(self,j,matrix):
        for ij in range(len(matrix)):
            matrix[ij][j] = 0
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = 0
        col = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j] == 0):
                    if(i == 0):
                        row = 1
                    if(j == 0):
                        col = 1
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,len(matrix)):
            if(matrix[i][0] == 0):
                self.makeRowZero(i,matrix)
        for j in range(1,len(matrix[0])):
            if(matrix[0][j] == 0):
                self.makeColZero(j,matrix)
        
        if(row == 1):
            self.makeRowZero(0,matrix)
        if(col == 1):
            self.makeColZero(0,matrix)
        
        
        