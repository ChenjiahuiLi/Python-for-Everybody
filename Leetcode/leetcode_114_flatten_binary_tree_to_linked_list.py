from binary_tree import create_btree_with_list


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        result = []
        self.dfs_tree_to_array(root, result)
        return(result)

    def dfs_tree_to_array(self, root, result):
        # result as global variable
        if not root:
            return(result)
        result.append(root.value)
        if root.left:
            result = self.dfs(root.left, result)
        if root.right:
            result = self.dfs(root.right, result)
        return(result)

    def dfs_tree_to_linked_list(self, root):

        


data = [1,2,5,3,4,7,6]
tree = create_btree_with_list(data)
print(tree)
s = Solution()
print(s.flatten(tree))

        