class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
                
        sD = {}
        tD = {}
        
        for i in range(0,len(s)):
            if(s[i] in sD):
                if(sD[s[i]] != t[i]):
                    return False
            else:
                if(t[i] in tD):
                    return False
                sD[s[i]] = t[i]
                tD[t[i]] = s[i]
                
        return True