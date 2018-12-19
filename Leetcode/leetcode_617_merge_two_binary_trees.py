import binarytree
# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: Node
        :type t2: Node
        :rtype: Node
        """
        if not t1 or not t2:
            return(t1 if not t2 else t2)
        if t1 and t2:
            t1.val = t1.val + t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        return(t1)

tree1 = Node()
tree2 = Node()
s = Solution()
            
        