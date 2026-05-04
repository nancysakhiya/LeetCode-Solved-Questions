# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def collisionPoint(self, t1: ListNode, t2: ListNode, d: int):
        while d:
            d -= 1
            t2 = t2.next
            
        while t1 != t2:
            t1 = t1.next
            t2 = t2.next
            
        return t1

    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        t1 = head1
        n1 = 0
        t2 = head2
        n2 = 0
        
        while t1 is not None:
            n1 += 1
            t1 = t1.next
            
        while t2 is not None:
            n2 += 1
            t2 = t2.next
            
        if n1 < n2:
            return self.collisionPoint(head1, head2, n2 - n1)
            
        else:
            return self.collisionPoint(head2, head1, n1 - n2)
            

