"""
Question 4: String Manipulation
Write a Python program to accept a full name from the user and perform the following operations:
- Display the name in uppercase and lowercase.
- Count the total number of characters.
- Display the first and last characters.
- Reverse the name.
- Replace spaces with underscores.
"""

full_name=input("Enter your Full Name: ")

print("Full name:" , full_name)
print("Upper case: ",full_name.upper())
print("lower case: ",full_name.lower())
print("Including space: ",len(full_name))
print("excluding space", len(full_name.replace(" ","")))
print("First and last Char :",full_name[0]," ",full_name[-1])
print("Revers name: ", full_name[::-1])
print("Replace Space with _ :", full_name.replace(" ","_"))