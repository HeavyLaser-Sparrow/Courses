# Read the names and marks of at least 3 students
# Rank the top three students with highest marks
# Give cash rewards, $500 for first, $300 for second, $100 for third value can't be modified
# Appreciate students who secured 950 marks and above

import operator

def readStudentDetails(): 
	print()
	# {student1: 700, student2: 800, student3:950, student4: 990}
	print("Enter the number of students: ")
	numberOfStudents = int(input())
	studentRecord = {}
	for student in range (0, numberOfStudents):
		print("Enter the name of the student: ")
		name = input()
		print("Enter the marks of students: ")
		marks = int(input())
		studentRecord[name] = marks
	print()
	return studentRecord
	
	
def rankStudents(studentRecord):
	try: 
		print()
		#[('student4', 990), ('student3', 950), ('student2', 800), ('student1', 700)]
		sortedStudentRecord = sorted(studentRecord.items(), key = operator.itemgetter(1), reverse = True)
		print(sortedStudentRecord)
		print("{} has secured first rank, scoring {} marks".format(sortedStudentRecord[0][0], sortedStudentRecord[0][1]))
		print("{} has secured second rank, scoring {} marks".format(sortedStudentRecord[1][0], sortedStudentRecord[1][1]))
		print("{} has secured third rank, scoring {} marks".format(sortedStudentRecord[2][0], sortedStudentRecord[2][1]))
		print()
		return sortedStudentRecord
	except IndexError: 
		print("Enter a minimum of 3 students")
		quit()


def rewardStudents(sortedStudentRecord, reward): 
	print()
	print("{} has received a cash reward of ${}".format(sortedStudentRecord[0][0], reward[0]))
	print("{} has received a cash reward of ${}".format(sortedStudentRecord[1][0], reward[1]))
	print("{} has received a cash reward of ${}".format(sortedStudentRecord[2][0], reward[2]))
	print()


def appreciateStudents(sortedStudentRecord): 
	print()
	for record in sortedStudentRecord:
		if record[1] >= 950: 
			print("Congratulations on scoring {} marks, {}".format(record[1], record[0]))
		else: 
			break
	print()
	
studentRecord = readStudentDetails()
sortedStudentRecord = rankStudents(studentRecord)
reward = (500, 300, 100)
rewardStudents(sortedStudentRecord, reward)
appreciateStudents(sortedStudentRecord)



