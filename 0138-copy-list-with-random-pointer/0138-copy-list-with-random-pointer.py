"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        temp = head
        mpp = {}
        while temp:
            newnode = Node(temp.val)

            mpp[temp] = newnode
            temp = temp.next

        temp = head
        while temp:
            copynode = mpp[temp]

            if temp.next:
                copynode.next = mpp[temp.next]
            else:
                copynode.next = None

            if temp.random:
                copynode.random = mpp[temp.random]
            else:
                copynode.random = None

            temp = temp.next

        return mpp[head]

