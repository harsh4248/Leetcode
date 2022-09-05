"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        q = []
        
        if not root:
            return []
        
        q.append(root)
        ans = []
        while len(q):
            curSize = len(q)
            curLevel = []
            for i in range(curSize):
                temp = q[0]
                curLevel.append(temp.val)
                q.pop(0)
                for c in temp.children:
                    q.append(c)
            
            ans.append(curLevel)
            
        return ans
            
            
            
            
            
            
            
            
            
        
        