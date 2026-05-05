# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findnthNode(self, temp, k):
        cnt = 1
        while temp is not None:
            if cnt == k:
                return temp
            cnt += 1
            temp = temp.next

        return temp

        
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        lenn = 1
        tail = head

        while tail.next is not None:
            tail = tail.next
            lenn += 1
            

        if k % lenn == 0:
            return head

        k = k % lenn

        tail.next = head

        newLastNode = self.findnthNode(head, lenn - k)

        head = newLastNode.next
        newLastNode.next = None

        return head