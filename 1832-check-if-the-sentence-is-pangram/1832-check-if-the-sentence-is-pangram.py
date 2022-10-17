class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sD = {}
        
        for c in range(97,(97 + 26)):
            sD[chr(c)] = 0
        
        for c in sentence:
            sD[c] += 1
        
        values = sD.values()
        for v in values:
            if(v == 0):
                return False
            
        return True
        
            
            