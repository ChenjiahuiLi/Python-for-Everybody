from binary_tree import create_btree_with_list
from collections import deque


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        result = []
        self.dfs_tree_to_array_II(root, result)
        return(result)

        #result_stack = deque()
        #self.dfs_tree_to_stack(root, result_stack)
        #result_stack.popleft()
        #self.stack_2_tree(root, result_stack)
        #return(root)


        
    """
    dfs_tree_to_array function takes a tree's root,
    and export an array recording the node's value 
    from top to leaf, left to right
    """
    def dfs_tree_to_array(self, root, result):
        # result as global variable
        if not root:
            return(result)
        result.append(root.value)
        if root.left:
            result = self.dfs_tree_to_array(root.left, result)         
        if root.right:
            result = self.dfs_tree_to_array(root.right, result)       
        return(result)
        """
        The biggest problem of this solution is that, it skip
        the empty nodes in the tree, meaning that with the output 
        list, cannot re-create the tree.
        """

    def dfs_tree_to_array_II(self, root, result):
        # How to not skip a empty child node but does not
        # influence when both child nodes are empty(leaf)
        if not root:
            return(result)
        result.append(root.value)
        if root.left and root.right:
            result = self.dfs_tree_to_array_II(root.left, result)
            result = self.dfs_tree_to_array_II(root.right, result)
        else:
            if not root.left and not root.right:
                return(result)
            elif root.left:
                result = self.dfs_tree_to_array_II(root.left, result)
                result.append(None)
            else:
                result.append(None)
                result = self.dfs_tree_to_array_II(root.right, result)
                



        return(result)



    def dfs_tree_to_stack(self, root, result_stack):
        if not root:
            return(result_stack)
        result_stack.append(root)
        if root.left:
            result_stack = self.dfs_tree_to_stack(root.left, result_stack)
        else:
            result_stack.append(None)

        if root.right:
            result_stack = self.dfs_tree_to_stack(root.right, result_stack)
        else:
            result_stack.append(None)
        return(result_stack)

    def stack_2_tree(self, root, result_stack):
        if result_stack:
            root.right = result_stack.popleft()
            root.left = None
            self.stack_2_tree(root.right, result_stack)
        else:
            return(root)


        


data = [1,2,5,3,4,None,6]
tree = create_btree_with_list(data)
print(tree)
s = Solution()
print(s.flatten(tree))

        