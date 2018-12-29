from binarytree import Node, tree, bst, heap
from random import seed

# Build a tree with binarytree.tree
seed(3)
my_tree = tree(height = 3, is_perfect = False)
#print("Generate with built-in tree method")
#print(type(my_tree)) # <class 'binarytree.Node'>
#print(my_tree)


# Build with Node
root = Node(1)
root.left = Node(2)
root.right = Node(3)
#print("Generate with built-in Node method")
#print(root)
#print(root.value)

# Build tree using a list
from collections import deque

data1 = [10,5,-3,3,2,None,11,3,-2,None,1]
data2 = [3,5,2,1,4,6,7,8,9,10,11,12,13,14]
"""
Iterators in Python:
- call iter() on list, will create a `list_iterator object` of the list
- every time you call __next__ on the `list_iterator object`, it will return
  the next object in the list. Notice that the 1st time you call __next__ on 
  the `list_iterator object` will return the 1st element of the list.
"""


"""
deque: double-ended queue
"""

def create_btree_with_list(data):

	tree = Node(data.pop(0))
	fringe = deque([tree])

	while len(data) > 1:
	# take out the first item in the queue as the parent node
		head = fringe.popleft()


	# take out the left-most item in the list
	# since we write the tree from left to right, 
	# create left child first
		left_value = data.pop(0)
		if left_value:
		# if the that item is NOT None, then create the child node
			head.left = Node(left_value)
		# add add the new left node into the deque for next level
			fringe.append(head.left)

		right_value = data.pop(0)
		if right_value:
			head.right = Node(right_value)
			fringe.append(head.right)

	return(tree)

def create_btree_with_list_iterator(data):
	n = iter(data)
	tree = Node(n.__next__())
	queue = deque([tree])
	while True:
		head = queue.popleft()
		try:
			head.left = Node(n.__next__())
			queue.append(head.left)
			head.right = Node(n.__next__())
			queue.append(head.right)
		except StopIteration:
			break
	return(tree)




print(create_btree_with_list(data1))
print(create_btree_with_list_iterator(data2))








