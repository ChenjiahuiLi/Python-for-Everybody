import random
import binarytree


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        # if all node's value are non-negative
        if sum < 0:
        	return(False)

        if root is not None:
        	# if encounter a leaf
        	if root.left is None and root.right is None:
        		if root.value == sum:
        			return(True)
        		else:
        			return(False)
        	else:
        		left_result = self.hasPathSum(root.left, sum - root.value)
        		right_result = self.hasPathSum(root.right, sum - root.value)
        		return(left_result or right_result)
        # if the root is None, 
        # OR try to evaluate left and right nodes of a leaf
        else:
        	return(False)


random.seed(5)
tree1 = binarytree.tree(height = 3, is_perfect = False)
print(tree1)


test = Solution()
print(test.hasPathSum(tree1, 12))
print(test.hasPathSum(tree1, 36))
print(test.hasPathSum(tree1, 50))
print(test.hasPathSum(None, 50))
print(test.hasPathSum(tree1, -3))

        