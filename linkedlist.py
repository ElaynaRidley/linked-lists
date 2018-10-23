from StudentRecord import*

class LinkedList:
	class Node:
		def __init__(self, payload):
			#assert type(payload) is str
			self.payload = payload
			self.next = None

	def __init__(self):
		self.head = None

	def addNode(self, newpayload, where="end"):
		if where == "beginning":
			node = LinkedList.Node(newpayload)
			node.next = self.head
			self.head = node
		else:
			self.appendAtEnd(newpayload)

	def appendAtEnd(self, newpayload):
		if self.head == None:
			self.head = LinkedList.Node(newpayload)
			return
		node = LinkedList.Node(newpayload)
		runner = self.head
		while runner.next != None:
			runner = runner.next
		runner.next = node

	def print(self):
		runner = self.head
		while runner != None:
			print(runner.payload.name, ": ", runner.payload.major, ", ", sep = "", end = "")
			runner = runner.next
		print()

	def defFront(self):
		if self.head != None:
			self.head = self.head.next
		else:
			return

	def __len__(self):
		count = 0
		runner = self.head
		while runner != None:
			count += 1
			runner = runner.next
		return count

	def clear(self):
		self.head = None
		

	def delLast(self):
		runner = self.head
		temp = runner
		while runner.next != None:
			temp = runner
			runner = runner.next
		temp.next = None

	def find(self, target):
		runner = self.head
		while runner != None:
			if runner.payload.name == target:
				return runner.payload
			runner = runner.next
		return None           

	def getNth(self, n):
		'''
		return a pointer to the nth node in the list where the first node is 0.
		Return None if the list has fewer than n nodes.
		'''
		assert type(n) is int, "first parameter must be an int"
		count = 0
		runner = self.head
		while runner != None:
			if count == n:
				return runner
			runner = runner.next
			count += 1
		return None

	def insert_sorted(self, some_str):
		'''Inserts a new node in alphabetical order'''
		newnode = LinkedList.Node(some_str)
		runner = self.head
		prev = runner
		
		if self.head == None:
			self.head = newnode
			return
		elif runner.payload.name > some_str.name:
			newnode.next = self.head
			self.head = newnode
			return
			
		runner = self.head
		prev = runner
		
		while runner != None:
			if runner.payload.name > some_str.name:
				newnode.next = runner
				prev.next = newnode
				return

			prev = runner
			runner = runner.next
		prev.next = newnode
			

	def printList(self):
		runner = self.head
		while runner != None:
			
			print("%-10s %s" % ("name:",runner.payload.name))
			print("%-10s %d" % ("id:",runner.payload.id))
			print("%-10s %s" % ("major:",runner.payload.major))
			print("%-10s %s" % ("address:",runner.payload.address))
			print("%-10s %s" % ("city:",runner.payload.city))
			print("%-10s %5.3f" % ("gpa:",runner.payload.gpa))
			print("")
			
			runner = runner.next
				

if __name__ == "__main__":
	j = LinkedList()
	j.insert_sorted(StudentRecord("Mark"))
	j.insert_sorted(StudentRecord("John,1501,CSC,Richmond Ave,Buffalo,4.000"))
	j.insert_sorted(StudentRecord("Mary", 1677, "HIS", "Main St", "Albany", 3.998))
	j.print()
