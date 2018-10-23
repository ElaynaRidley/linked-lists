from linkedlist import*

class StudentRecord:
	nextid = 1001

	def __init__(self, *args):
		if len(args) == 1:
			if "," not in args[0]:     #name only, rest are default values
				self.name = args[0]
				self.id = StudentRecord.nextid
				StudentRecord.nextid += 1
				self.major = "UND"
				self.address = "Bosch Hall"
				self.city = "Buffalo"
				self.gpa = 0
			else:
				xargs = args[0].split(",")
				if len(xargs) != 6:
					print("****ERROR**** You need 6 args for the StudentRecord constructor")
				else:
					self.name = xargs[0]
					self.id = int(xargs[1])
					self.major = xargs[2]
					self.address = xargs[3]
					self.city = xargs[4]
					self.gpa = float(xargs[5])
		else:
			if len(args) != 6:
				print("**** ERROR **** You need 6 args for the StudentRecord constructor")
			else:
				self.name = args[0]
				self.id = int(args[1])
				self.major = args[2]
				self.address = args[3]
				self.city = args[4]
				self.gpa = float(args[5])

	def print(self):
		print(self.name, self.major)

	def printAll(self):
		print("%-10s %s" % ("name:",self.name))
		print("%-10s %d" % ("id:",self.id))
		print("%-10s %s" % ("major:", self.major))
		print("%-10s %s" % ("address:", self.address))
		print("%-10s %s" % ("city:", self.city))
		print("%-10s %5.3f" % ("gpa:",self.gpa))
		print("")

	def dump(self):
		return self.name+","+str(self.id)+"," + self.major + "," + self.address + "," + self.city+ "," + str(self.gpa)
	
	# more methods here
	
	def printNameMajor(self):
		'''This prints the student's name and the major'''
		print(self.name+ ":", self.major)
		
	def find(self, student_name):
		'''This searches the alphalist and looks to see if there is a student in it or not'''
		for item in alphalist:
			if item.name == student_name:
				return alphalist.name
			else:
				return None

if __name__ == "__main__":
	s1 = StudentRecord("Mark")
	#print(s1.dump())
	s2 = StudentRecord("John,1501,CSC,Richmond Ave,Buffalo,4.000")
	print(s2.dump())
	s2.printNameMajor()
	s2.printAll()
	s3 = StudentRecord("Mary", 1677, "HIS", "Main St", "Albany", 3.998)
	#s3.dump()      
	#s3.printAll()
	alphalist = LinkedList()
	alphalist.insert_sorted(s1)
	alphalist.insert_sorted(s2)
	alphalist.insert_sorted(s3)
