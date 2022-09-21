class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        
        if numRows == 1:
            return ans
        else:
            for i in range(numRows-1):
                temp = []
                for j in range(len(ans[i])+1):
                    if(j-1 < 0 or j == len(ans[i])):
                        temp.append(1)
                    else:
                        temp.append(ans[i][j-1] + ans[i][j])
                ans.append(temp)
                        
        return ans
            
        