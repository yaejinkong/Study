class Node:
	def __init__(self, key=None):
		self.key = key
		self.prev = self
		self.next = self
	def __str__(self):
		return str(self.key)

class DoublyLinkedList:
	def __init__(self):
		self.head = Node() # create an empty list with only dummy node

	def __iter__(self):
		v = self.head.next
		while v != self.head:
			yield v
			v = v.next
	def __str__(self):
		return " -> ".join(str(v.key) for v in self)

	def printList(self):
		v = self.head.next
		print("h -> ", end="")
		while v != self.head:
			print(str(v.key)+" -> ", end="")
			v = v.next
		print("h")
	def __len__(self):
		size = 0
		for node in self:
			size += 1
		return size

	def splice(self, a, b, x):
			if a == None or b == None or x == None:
				return
			a.prev.next = b.next
			b.next.prev = a.prev
			
			x.next.prev = b
			b.next = x.next
			a.prev = x
			x.next = a
			
	def moveAfter(self, a, x):
		self.splice(a, a, x)
			
	def moveBefore(self, a, x):
		self.splice(a, a, x.prev)
			
	def insertAfter(self, x, key):
		self.moveAfter(Node(key), x)
		
	def insertBefore(self, x, key):
		self.moveBefore(Node(key), x)
		
	def pushFront(self, key):
		self.insertAfter(self.head, key)
		
	def pushBack(self, key):
		self.insertBefore(self.head, key)
			
	def deleteNode(self, x):
		if x == None or x == self.head:
			return
		else: 
			x.prev.next = x.next
			x.next.prev = x.prev
		
	def popFront(self):
		if self.head.next == self.head:
			return None
		key = self.head.next.key
		self.deleteNode(self.head.next)
		return key
		
	def popBack(self):
		if self.head.next == self.head:
			return None
		key = self.head.prev.key
		self.deleteNode(self.head.prev)
		return key
		
	def search(self, key):
		v = self.head.next
		while v != self.head:
			if v.key == key:
				return v
			v = v.next
		return None
		
	def isEmpty(self):
		if len(self) == 0:
			return True
		else:
			return False
			
	def first(self):
		ch = self.head
		return ch.next
		
	def last(self):
		ch = self.head
		return ch.prev
	
	def findMax(self, key):
		if len(self) == 0:
			return None
		max_node = self.head.next
		for node in self:
			if node.key > max_node.key:
				max_node = node
		return max_node.key
	
	def deleteMax(self):
		if len(self) == 0:
			return None
		max_node = self.head.next
		for node in self:
			if node.key > max_node.key:
				max_node = node
		key = max_node.key
		self.deleteNode(max_node)
		return key
		
	def sort(self):
		sorted_list = DoublyLinkedList()
		while len(self) > 0:
			max_key = self.deleteMax()
			sorted_list.pushFront(max_key)
		return sorted_list
L = DoublyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == 'pushF':
		L.pushFront(int(cmd[1]))
		print("+ {0} is pushed at Front".format(cmd[1]))
	elif cmd[0] == 'pushB':
		L.pushBack(int(cmd[1]))
		print("+ {0} is pushed at Back".format(cmd[1]))
	elif cmd[0] == 'popF':
		key = L.popFront()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Front".format(key))
	elif cmd[0] == 'popB':
		key = L.popBack()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Back".format(key))
	elif cmd[0] == 'search':
		v = L.search(int(cmd[1]))
		if v == None: print("* {0} is not found!".format(cmd[1]))
		else: print("* {0} is found!".format(cmd[1]))
	elif cmd[0] == 'insertA':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertAfter(x, int(cmd[2]))
			print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'insertB':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertBefore(x, int(cmd[2]))
			print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'delete':
		x = L.search(int(cmd[1]))
		if x == None:
			print("- {0} is not found, so nothing happens".format(cmd[1]))
		else:
			L.deleteNode(x)
			print("- {0} is deleted".format(cmd[1]))
	elif cmd[0] == "first":
		print("* {0} is the value at the front".format(L.first()))
	elif cmd[0] == "last":
		print("* {0} is the value at the back".format(L.last()))
	elif cmd[0] == "findMax":
		m = L.findMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key is", m)
	elif cmd[0] == "deleteMax":
		m = L.deleteMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key", m, "is deleted.")
	elif cmd[0] == 'sort':
		L = L.sort()
		L.printList()
	elif cmd[0] == 'print':
		L.printList()
	elif cmd[0] == 'exit':
		break
	else:
		print("* not allowed command. enter a proper command!")