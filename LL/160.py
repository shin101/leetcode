# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=headA
        b=headB
        a_len=0
        b_len=0

        while a:
            a_len+=1
            a = a.next
        
        while b:
            b_len +=1
            b=b.next
        
        if a_len>b_len:
            diff = a_len-b_len
            long = headA
            short = headB

        else:
            diff= b_len-a_len
            long = headB
            short = headA
        
        i = 0
        while i < diff:
            i+=1
            long = long.next
        
        while long and short:
            if long == short:
                return long
            long = long.next
            short = short.next
        

        return long 