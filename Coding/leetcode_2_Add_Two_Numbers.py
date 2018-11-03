# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def to_int(node):
            if node:
                return node.val + 10*to_int(node.next)
            else:
                return 0
            
        def to_linked_list(num):
            newll = ListNode(num % 10)
            if num > 9:
                newll.next = to_linked_list(num / 10)
            else:
                return(newll)
                            
        return [to_int(l1) , to_int(l2)]
            
            
        
    
        
                
                
            
        
        