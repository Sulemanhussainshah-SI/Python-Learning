name_stud=input("Enter Student Name: ")

math_marks=int(input("enter math marks:"))
science_marks=int(input("enter science marks:"))
english_marks=int(input("enter english marks:"))

total_marks=math_marks+science_marks+english_marks
average_marks=total_marks/3

print("Student Name:",name_stud)
print("Total Marks:",total_marks)
print("Average of marks:",average_marks)