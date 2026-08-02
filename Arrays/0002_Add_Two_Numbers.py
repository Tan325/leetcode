# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = l1
        sum1 = 0
        i = 1
        while current:
            sum1 = sum1 + current.val*i
            current = current.next
            i = i*10
     
       
        current = l2
        sum2 = 0
        j = 1
        while current:
            sum2 = sum2 + current.val*j
            current = current.next
            j = j*10

        sum3 = sum1 + sum2
         
        h3 = ListNode()
    
        current = h3
        while current:
            current.val = sum3%10
            sum3 = sum3//10
            if sum3 == 0:
                break
            current.next = ListNode()
            current = current.next
            

        return h3
        

       
    
    
       