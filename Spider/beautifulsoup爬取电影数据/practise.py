class Stack(object):
	"""docstring for Stack"""
	def __init__(self, max_size):
		self.max_size = max_size
		self.arr = []
	
	def counts(self):
		return len(self.arr)

	def push(self,item):
		self.arr.append(item)
		return "添加成功"

	def pop(self):
		self.arr.pop()
		return '删除成功'

	def empty(self):
		if len(self.arr):
			return '非空'
		return '为空'		

	def full(self):
		if len(self.arr) == self.max_size:
			return '已满'
		return '未满'

	def index(self,item):
		for i in len(self.arr):
			if arr[i] == item:
				return i
			return '找不到该元素'

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
		self.end = None
	
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

			


LOAD DATA LOCAL INFILE 'C:\\Users\\Administrator\\Desktop\\datasets\\movielens\\ratings.dat' INTO TABLE tag FILEDS TERMINATED BY '::' LINES TERMINATED BY '\n' (userid,movieid,rating,timestamp)



LOAD DATA INFILE 'C:\\Users\\Administrator\\Desktop\\datasets\\movielens\\movies.dat' INTO TABLE movies FIELDS TERMINATED BY '::'  ENCLOSED BY '"' LINES TERMINATED BY '\n';

secure-file-priv

show variables like '%secure%';