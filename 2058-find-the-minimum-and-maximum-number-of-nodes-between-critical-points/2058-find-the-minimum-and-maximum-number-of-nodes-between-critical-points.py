# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr = head.next
        prev = head
        
        pos = 1 # this is the position of current node

        first = -1
        last = -1
        mindis = float('inf')

        while curr.next:
            next_node = curr.next

            # this is our critical point condition
            if (curr.val < prev.val and curr.val < next_node.val) or (curr.val > prev.val and curr.val > next_node.val):

                if first == -1: # first critical point
                    first = pos
                    last = pos

                else:
                     # we calculate distance from previous critical point and update our last critical point

                    mindis = min(mindis, pos - last)
                    last = pos

            prev = curr
            curr = next_node
            pos += 1

        if first == -1 or first == last:
            return [-1, -1]

        maxdis = last - first

        return [mindis, maxdis]

                
            
