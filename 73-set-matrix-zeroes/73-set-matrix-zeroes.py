class Solution:
    
    def makeRowZero(self,i,matrix):
        for ir in range(len(matrix[i])):
            matrix[i][ir] = 0
    def makeColZero(self,j,matrix):
        for ij in range(len(matrix)):
            matrix[ij][j] = 0
        pass
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Step 1: copy matrix
        cpyMat = []
        for row in matrix:
            temp = []
            for colVal in row:
                temp.append(colVal)
            
            cpyMat.append(temp)
        
        # cpyMat[0][0] = 100
        # print(cpyMat,matrix)
            
        # Step 2: and solve question
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(cpyMat[i][j] == 0):
                    self.makeRowZero(i,matrix)
                    self.makeColZero(j,matrix)
                
        
        
        

 
        """
        Do not return anything, modify matrix in-place instead.
        """
        