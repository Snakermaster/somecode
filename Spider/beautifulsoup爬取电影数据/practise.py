class Stack(object):
	"""docstring for Stack"""
	def __init__(self, max_size):
		self.max_size = max_size
		self.arr = []
	
	def counts(self):
		pass

	def push(self,item):
		pass

	def pop(self):
		pass

	def empty(self):
		pass		

	def full(self):
		pass

	def index(self,item):
		pass

	class Node(object):
		"""docstring for Node"""
		def __init__(self, item):
			self.item = item
			self.next_node = Node

	node1 = Node('first')
	node2 = Node('second')
	node3 = Node('Third')

	head = node1
	node1.next_node = node2
	node2.next_node = node3


class LinkedList(object):
	"""docstring for LinkedList"""
	
	def __init__(self):
		self.head = None
		pass
	
	def append(self,item)
		pass
	
	def insert(self,index)
		pass
		
	def remove(self,item)
		pass

	def remove_by_index(self,index)
		pass

	def counts(self)
		pass

	def index_of(self,item)
		pass

l = LinkedList()
l.append('four')
l.append('five')
l.remove('none')
for i in l:
	print(i)

			







