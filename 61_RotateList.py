# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        # Create a cycle, have current last element point back to the head
        curr = head
        n = 0
        while curr.next:
            curr = curr.next
            n += 1
        n += 1
        curr.next = head
        last = curr

        # Moving the head to node.next is a left rotation
        # x left rotations = n - x right rotations
        # Note: n rotations essentially does nothing
        num_rotations = (n - k) % n
        # Set head accordingly, then remove link from prev to head
        curr = head
        prev = last
        for i in range(num_rotations):
            curr = curr.next
            prev = prev.next

        # Now, curr is the head of rotated linked list
        # Remove link from prev to curr
        prev.next = None
        return curr
