# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        count = 0
        if(head.next == None):
            return None
        p = head
        while(p):
            count += 1
            p = p.next
            
        count = count // 2
        
        p = None
        q = head
        while(count and q):
            p = q
            q = q.next
            count -= 1
        
        p.next = q.next
        return head
        
            
        