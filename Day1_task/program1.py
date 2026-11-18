# Write a Python program to accept a student's name, age, height, and marks from the user. Display all the details along with their respective data types using type().

name=input("Enter Student name :")
age=int(input("Enter Student age :"))
height=float(input("Enter Student Height :"))
marks=float(input("Enter student marks :"))

print("........Student Details.........")
print(f"Student Name: {name} Datatpye : {type(name)}")
print("Student Age:  {0} Datatpye : {1}".format(age,type(age)) )
print("Student Height:", height, "Datatype :",type(height))
print("Student Marks: {0} Datatpye : {1}".format(marks, type(marks)))