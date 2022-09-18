class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if color == image[sr][sc]:
            return image
        
        curColor = image[sr][sc]
        def dfs(r,c):
            
            if image[r][c] == curColor:
                image[r][c] = color
                if r >= 1:
                    dfs(r-1,c)
                if r+1 < len(image):
                    dfs(r+1,c)
                if c >= 1:
                    dfs(r,c-1)
                if c+1 < len(image[0]):
                    dfs(r,c+1)
        
        dfs(sr,sc)
        return image
        
        
        
        
        
        
        