from binarytree import Node, tree, bst, heap
from random import seed

# Build a tree with binarytree.tree
seed(3)
my_tree = tree(height = 3, is_perfect = False)
print("Generate with built-in tree method")
print(type(my_tree)) # <class 'binarytree.Node'>
print(my_tree)


# Build with Node
root = Node(1)
root.left = Node(2)
root.right = Node(3)
print("Generate with built-in Node method")
print(root)
print(root.value)



