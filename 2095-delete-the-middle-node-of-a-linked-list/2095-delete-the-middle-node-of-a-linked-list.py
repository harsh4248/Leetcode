# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if(head.next == None):
            return None
        
        temp,slow,fast = None,head,head
        
        while(fast.next != None):
            temp = slow
            slow = slow.next
            fast = fast.next
            if(fast.next):
                fast = fast.next
            else:
                break
            
            
        # print(temp.val,slow.val,fast.val)
        temp.next = slow.next
        return head
            
            
        