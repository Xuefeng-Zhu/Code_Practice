class Node():
	def __init__(self, v=None):
		self.value = v
		self.left = None
		self.mid = None
		self.right = None

class trinaryTree():
	def __init__(self):
		self.root = None
		self.size = 0

	# insert a new node into the tree and increase the size of the tree
	def insertNode(self, v):
		if self.root is None:
			self.root = Node(v)
		else:
			self.insert(self.root, v) 
		self.size += 1 

	# helper function for insertNode
	def insert(self, node, v):
		if node is None:
			node = Node(v)
		elif node.value > v:
			node.left = self.insert(node.left, v)
		elif node.value == v:
			node.mid = self.insert(node.mid, v)
		else:
			node.right = self.insert(node.right, v) 
		return node

	# delete a node from the tree and decrease the size of the tree  		
	def deleteNode(self, v):
		if self.root is None:
			raise Exception, 'The tree is empty!'
		elif self.root.value == v:
			if self.root.mid is not None:
				self.root.mid.left = self.root.left
				self.root.mid.right = self.root.right
				self.root = self.root.mid
			elif self.root.left and self.root.right:
				temp = self.deletedTwo(node)
				self.root = temp
			elif self.root.left:
				self.root = self.root.left
			elif self.root.right:
				self.root = self.root.right
			else:
				self.root = None  
		else:
			self.delete(None, self.root, v)
		self.size -= 1

	#helper function for deleteNode
	def delete(self, parent, node, v):
		if node is None:
			raise Exception, 'The node you are trying to delete does not exist'
		elif node.value == v:
			#find the node to be deleted 
			if node.mid is not None:
				if node.mid is not None:
					node.mid.left = node.left
					node.mid.right = node.right
					parent = node.mid
				elif node.left and node.right:
					temp = self.deleteTwo(node)
					self.replaceChild(parent, temp)
				elif node.left:
					self.replaceChild(parent, node.left)
				elif node.right:
					self.replaceChild(parent, node.right)
				else:
					self.deleteNone(parent, node)
		elif node.value > v:
			self.delete(node, node.left, v)
		else:
			self.delete(node, node.right, v)

	# delete node with no child 
	def deleteNone(self, parent, node):
		if node.value < parent.value:
			parent.left = None
		else:
			parent.right = None

	# delete  node with one child by replace itself with its child
	def replaceChild(self, parent, node):
		if node.value < parent.value:
			parent.left = node
		else:
			parent.right = node

	# delete node with two children 
	def deleteTwo(self, node):
		successor = self.findSuccessor(node.left)
		if node.left is not successor:
			successor.left = node.left
		else:
			successor.left = None 
		successor.right = node.right 
		return successor

	# find node with largest value in left subtree
	def findSuccessor(node):
		cur = node
		parent = None
		while cur.right:
			parent = cur
			cur = cur.right
		if parent:
			parent.right = None
		return cur


if __name__ == '__main__':
	tree = trinaryTree()
	tree.insertNode(5)
	tree.insertNode(4)
	tree.insertNode(9)
	tree.insertNode(5)
	tree.insertNode(7)
	tree.insertNode(2)
	tree.insertNode(2)
	assert tree.size == 7, 'Error'

	tree.deleteNode(5)
	assert tree.size == 6, 'Error'
	tree.insertNode(5)
	tree.deleteNode(2)
	assert tree.size == 6, 'Error'
	tree.insertNode(2)
	tree.deleteNode(4)
	assert tree.size == 6, 'Error'
	tree.insertNode(4)
	tree.deleteNode(7)
	assert tree.size == 6, 'Error'
	tree.insertNode(7)
	tree.insertNode(11)
	tree.deleteNode(9)
	assert tree.size == 7, 'Error'

	print "Pass test"
