# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxSum = 0
        l = r = mid = head

        while r and r.next:
            r = r.next.next
            mid = mid.next
        
        # reverse
        curr = mid
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        while prev:
            maxSum = max(maxSum, (head.val + prev.val))
            head = head.next
            prev=prev.next
        return maxSum



