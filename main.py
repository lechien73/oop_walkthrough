from classes import Employee, Developer

employee = Employee("Nina", "Raju", 25000)

print(employee)
print(employee.first_name)
print(employee.calculate_raise())
employee.apply_raise()
print(employee.salary)

developer = Developer("Sasha", "Kolesnyk", 25000)

print(developer)
print(developer.first_name)
developer.language = "Python"
print(developer.calculate_raise())
developer.apply_raise()
print(developer.salary)
