Name = (input("Enter Name : "))

SID = int(input("Enter SID : "))

Gender = (input("Enter Gender: "))

Course_Name = (input("Enter Course_Name : "))

CGPA = int(input("Enter CGPA : "))



SortedMarks = [SID, Name, Gender, Course_Name, CGPA]

SortedMarks.sort()

print(SortedMarks)
