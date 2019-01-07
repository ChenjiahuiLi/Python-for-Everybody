class Solution:

# A recursive way of solving this problem (DFS)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return(True)
        
        return(self.sub_tree_sym(root.left, root.right))
                
                
    def sub_tree_sym(self, L, R):
        if L and R:
            if L.val != R.val:
                return(False)
            else:
                return(self.sub_tree_sym(L.right, R.left) and self.sub_tree_sym(L.left, R.right))
        else:
            if not L and not R:
                return(True)
            else:
                return(False)
        
"""
Garbage COLLECTION
1. objects are stored in VM
2. in Python and Java, don't need to manually delete objects(garbage)
3. clean garbage will need to scan the whole garbage TreeNode
4. when executing garbage collection, VM will stop all 
   the other process (to freeze the gargage tree)        
"""        
