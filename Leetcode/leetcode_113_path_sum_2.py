from binary_tree import create_btree_with_list
from binarytree import Node

"""
Given a binary tree and a sum, 
find all root-to-leaf paths where each path's sum equals the given sum.

This problem is a extension of 112_path_sum_1
Idea:
Backtracking
"""

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
        	return(result)
        # when root is empty, cannot call root.value
        else:
        	result = []
        	self.dfs(root, sum, result, [root.value]) 
        	return(result)


    """
    Tracking Problem: 
    how could I duplicate a path whenever I split on right and left nodes?

    Solution:
    don't use path as a Global variable, at every recursion, fill in the
    old path + [node.value], so that it automatically take care of the duplication.

    Set result as Global variable, so that whenever a path meet the leaf, 
    evaluate the sum of the path, if fits, add the path to result.

    In Python:
    path = [1]
    path + [2] => [1,2]

    """
    def dfs(self, root, target, result, path):
    	if not root:
    		return(result)
    	if sum(path) == target and not root.left and not root.right:
    		result.append(path)
    		return(result)
    	if root.left:
    		# don't use path.append(value), it will change the `path` list
    		self.dfs(root.left, target, result, path + [root.left.value])
    	if root.right:
    		self.dfs(root.right, target, result, path + [root.right.value])


"""
Test Case
"""
tree = create_btree_with_list([5,4,8,11,None,13,4,7,2,None, None,5,1])
print(tree)

s = Solution()
print(s.pathSum(tree, sum = 22))
