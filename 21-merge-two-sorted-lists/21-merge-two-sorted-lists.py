# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        p = list1
        q = list2
        tHead,t = None,None
        
        while p and q:
            
            if(p.val < q.val):
                temp = ListNode(p.val,None)
                p = p.next
                
            else:
                temp = ListNode(q.val,None)
                q = q.next
            
            if(tHead == None):
                tHead = temp
                t = tHead
            else:
                t.next = temp
                t = t.next
        
        while p:
            temp = ListNode(p.val,None)
            t.next = temp
            t = t.next
            p = p.next
            
        while q:
            temp = ListNode(q.val,None)
            t.next = temp
            t = t.next
            q = q.next
        
        return tHead
            
                    
                
                
        
        
        