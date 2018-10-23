#--------------------------------------This is main.py -------------------------------------
import sys
import os
import traceback
import linkedlist
import MajorsList
import StudentRecord

def main():
	majorslist = MajorsList.MajorsList()
	alphalist = linkedlist.LinkedList()
	
	while True:
		try:
			line = input(">> ")
			if line == "quit":
				break

			elif line[0] == "#":
				print(line)
	
			elif line == "list majors":
				majorslist.print_majors()
	
			elif line.startswith("new major "):
				the_new_major = line[10:]
				if majorslist.find_major(the_new_major):
					#doesnt work
					print("That major is already in the system!")
				else:
					majorslist.insert_sorted(the_new_major)
	
			elif line.startswith("show major "):
				the_major = line[10:]
				stulisthead = majorslist.find_major(the_major)
				if stulisthead is None:
					print("No such major in the system!")
				else:
					majorslist.show_major(the_major)
	
			elif line.startswith("declare major "):
				sturecptr = StudentRecord.StudentRecord(line[14:])
				if not majorslist.find_major(sturecptr.major):
					majorslist.insert_sorted(sturecptr.major)
				alphalist.insert_sorted(sturecptr)
				majorslist.insert_student(sturecptr)
	
			elif line == "list students":
				alphalist.printList()
	
			elif line.startswith("find "):
				student_name = line[5:]
				snode = alphalist.find(student_name)
				if snode is None:
					print("That student does not exist")
				else:
					snode.printAll()
	
			#elif line == "dump":
				#dump is abrogated
				#majorslist.dump()
	
			elif line == "help":
				print("list majors -- print the name of each major")
				print("new major MAJORNAME -- add a new major to the system")
				print("show major MAJORNAME -- list the students who have this major")
				print("declare major NEWSTUDENT -- add a student to the system")
				print("       the student info is:   name,idnum,major,street,city,gpa")
				print("       e.g.    declare major Mark,1501,CSC,Main St.,Buffalo,3.614")
				print("list students -- list all the students in alphabetical order regardless of major")
				print("find NAME -- find a student with the NAME in the system and print their major")
				#print("dump -- write commands that would recreate the system")
				print("help")
				print("quit")
	
			elif line.startswith("$"):
				print(eval(line[1:]))
	
			elif line.startswith("!"):
				os.system(line[1:])
			else:
				print("Unknown command!")
	
		except Exception as e:
			tb = traceback.format_exc()
			print("Caught a run-time error and recovered from it.")
			print(e.__class__.__name__, end=", ")
			print(e)
			print(tb)

main()
