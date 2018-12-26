from binarytree import tree, Node
from random import seed

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: Node
        :type t2: Node
        :rtype: Node
        """
        # Use t1 as the base tree for output
        if not t1 or not t2:
            return(t1 if not t2 else t2)
        else:
            t1.value += t2.value
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        return(t1)



seed(10086)      
tree1 = tree(height = 3, is_perfect = True)
tree2 = tree(height =2, is_perfect = False)
print("Tree1")
print(tree1)
print("Tree2")
print(tree2)
s = Solution()

# When one of the tree argument is empty
stree1 = s.mergeTrees(tree1, None)
print(stree1)

# When both of the tree arguments are empty
stree2 = s.mergeTrees(None, None)
print(stree2)

# When both of the tree arguments are non-empty
stree3 = s.mergeTrees(tree1, tree2)
print(stree3)

            
        