
employee_file = open("employees1.txt", "w")

new_employee = "Toby - Human Resources\n"
employee_file.write(new_employee)


# Always close the file!!!
employee_file.close()
