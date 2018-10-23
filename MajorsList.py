from StudentRecord import *
from linkedlist import *

class MajorsList:
	'''This class has two classes within it.
It is a linked list of majors,
and within each major there is a linked list of students'''
	class MajorNode:
		'''This class is a linked list of majors.'''
		def __init__(self, payload):
			'''The variables are
			headptr is the pointer to the first node
			next advances to the next node
			and poayload is the data in the node'''
			self.headptr = None
			self.next = None
			self.payload = payload
			
	class stuptrNode:
		'''This class linked lists of student record objects'''
		def __init__(self, payload):
			'''payload is the student record object's data
				next advances to the next node'''
			self.payload = payload
			self.next = None

	def __init__(self):
		'''head is the pointer to the first node in the list of majors'''
		self.head = None

	def find_major(self, maj):
		'''this looks through the lkost of majors.
		it returns true if it finds maj in the list
		it returns false if it doesn't find maj in the list'''
		
		runner = self.head
		while runner != None:
			if runner.payload == maj:
				return True
			runner = runner.next
		return False

	def print_majors(self):
		'''this runs through the list of majors.
		if the list is empty, it returns None.
		it loops through the list of students for each major and adds 1 to the count for each student.
		it prints the name of the major and how many students are in each major.
		then it resets count to 0 before moving on to the next major'''
		runner = self.head
		count = 0
		if self.head == None:
			return None
		while runner != None:
			runner2 = runner.headptr
			while runner2 != None:
				runner2 = runner2.next
				count += 1
			print(runner.payload, count, "students")
			count = 0
			runner = runner.next
		print()

	def show_major(self,maj):
		'''this is similar to print_majors
		but it prints a specific major and how many students are in it
		instead of all the majors'''
		count = 0
		runner = self.head
		if self.head == None:
			return None
		while runner != None:
			runner2 = runner.headptr
			while runner2 != None:
				runner2 = runner2.next
				count += 1
			runner = runner.next
		print(maj,count,"students")
		count = 0
			
		

	def insert_sorted(self, some_new_major):
		'''this inserts majors alphabetically into the list of majors.
		if the list is empty, the newnode is placed in the beginning
		if the payload of the runner is greater than the new major
		the next node is assigned self.head and self.head is assigned the new node
		then it loops through the list
		if the new major is less than the current payload
		it breaks
		or it advances the runner
		outside of the loops it advances runner'''
		count = 0
		newnode = MajorsList.MajorNode(some_new_major)
		runner = self.head
		prev = runner

		if self.head == None:
			self.head = newnode
			return
		elif runner.payload > some_new_major:
			newnode.next = self.head
			self.head = newnode
			return
		runner = self.head
		prev = runner
		while runner != None:
			if some_new_major < runner.payload:
				break
			prev = runner
			runner = runner.next
		prev.next = newnode
		newnode.next = runner

	def insert_student(self, sturec_pointer):
		'''this inserts students unalphabetically in the loist of students within each major
		while looping through the list of majors
		if loops through the list of students
		if theres no student there it assigns the new student to the beginning
		igf the is a student there already it inserts the student in the beginning'''
		runner = self.head
		newnode = MajorsList.stuptrNode(sturec_pointer)
		while runner != None:
			if runner.payload == sturec_pointer.major and runner.headptr == None:
				runner.headptr = newnode
				return
			elif runner.payload == sturec_pointer.major and runner.headptr != None:
				newnode.next = runner.headptr
				runner.headptr = newnode
				return
			
			runner = runner.next
	 

	#def dump(self):
		#abrogated
		#runner = self.head
		#while runner != None:
			#print(runner.payload+":")
			#runner2 = runner.headptr
			#while runner2 != None:
				#print(runner2.payload.name)
				#runner2 = runner2.next
			#runner = runner.next



if __name__ == "__main__":
	majorslist = MajorsList()
	s1 = StudentRecord("John Doe", 1234, "CSC", "1245 Richmond Ave.", "Buffalo", 3.7)
	s2 = StudentRecord("Mary Sue", 5678, "DMA", "2001 Main St.", "Rochester", 4.0)
	s3 = StudentRecord("Zen Smith", 9999, "ABEC", "12354 Five St.", "NYC", 2.9)
	s4 = StudentRecord("Abby Robin", 1111, "English", "12 Done St.", "Paris", 1.2)
	s5 = StudentRecord("Fake Name", 6767, "DMA", "222 No St.", "Berlin", 0.0)
	majorslist.insert_sorted("DMA")
	majorslist.insert_sorted("ABEC")
	majorslist.insert_sorted("CSC")
	majorslist.insert_sorted("English")
	majorslist.insert_student(s1)
	majorslist.insert_student(s2)
	majorslist.insert_student(s3)
	majorslist.insert_student(s4)
	majorslist.insert_student(s5)
	#majorslist.dump()
	majorslist.print_majors()
	
	
	

			
