"""
Question 3: Employee Salary Calculation
Write a Python program to accept an employee's name and monthly salary. Calculate and display:
- Annual salary
- 10% bonus amount
- Total annual salary including bonus
"""
emp_name=input("Enter Employee name: ")
emp_salary=float(input("Enter Employee Monthly salary: "))

annual_salary= 12 * emp_salary
bonus_ammount= annual_salary * 0.10
total_salary= annual_salary + bonus_ammount

print("Annual Salary: ",annual_salary)
print("10% Bonus Amount: ",bonus_ammount)
print("Total annual salary including bonus: ",total_salary)