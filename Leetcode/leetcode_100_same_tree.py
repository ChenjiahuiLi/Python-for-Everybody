"""
Problem:

Given 2 binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if 
they are structured identically
and
the nodes have the same value
"""
from binary_tree import create_btree_with_list
import pytest

class Solution():
	def isSameTree(self, p, q):
		"""
		Don't need a global variable to store whether it's True or False
		The idea was:

		- for each node, return True if and only if:
			- the nodes VALUE on both tree are the same
			- the sub-trees of both nodes are the same

		- whenever a node value or a sub-tree does not match, return False

		- Consider leaf as `not p and not q` 
		  rather than put them inside `if p and q`

		"""
		if p and q:
			if p.value == q.value:
				return(self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
			else:
				return(False)
		else:
			# when it comes to a leaf
			if not p and not q:
				return(True)
			else:
				return(False)


# 3 Test Cases
data  = [[1,2,3], [1,2,3], [1,None,2], [1,2,None],[1,1,2],[1,2,1]]
ttree1 = create_btree_with_list(data[0])
ttree2 = create_btree_with_list(data[1])
ttree3 = create_btree_with_list(data[2])
ttree4 = create_btree_with_list(data[3])
ttree5 = create_btree_with_list(data[4])
ttree6 = create_btree_with_list(data[5])

s = Solution()
assert s.isSameTree(ttree1, ttree2) is True, "Test Case 1 Fail"
assert s.isSameTree(ttree3, ttree4) is False, "Test Case 2 Fail"
assert s.isSameTree(ttree5, ttree6) is False, "Test Case 3 Fail"






