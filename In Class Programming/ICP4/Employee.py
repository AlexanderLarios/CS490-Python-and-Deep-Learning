class employee:
    count_employee = 0

    def __init__(self, name, salary, family, department):
        #increments the class counter each time an employee or a full time employee (child class) is created
        self.__class__.count_employee += 1
        #stores the general information about the employee
        self.name_employee = name
        self.salary_employee = salary
        self.family_employee = family
        self.department_employee = department

    def averageSalary(self, list = [], *args):
        total_salary = 0
        #retrieves all the salaries and sums them
        for e in list:
            total_salary += e
        #finds the average based off total salary / total employee count
        return total_salary / self.__class__.count_employee

class fullTimeEmployee (employee):
    #if employee is created as a full time employee this attribute will always be true
    full_time = True

    def __int__(self, name_employee, salary, family, department):
        employee.__init__(self, name_employee, salary, family, department)

#creating instances of employee and full time employee class
empD = employee("alex piatt", 150.00, 4, "engineer1")
empA= employee("tony stark", 200.00, 3, "engineer2")
empC = employee("wanda", 450.00, 2, "engineer3")
ftEmp = fullTimeEmployee("natasha romanov", 300.00, 1, "engineer4")
ftEmpA = fullTimeEmployee("peter parker", 400.00, 2, "engineer5")

listemp = [empD.salary_employee, empA.salary_employee, empC.salary_employee, ftEmp.salary_employee, ftEmpA.salary_employee]

#find average of all employee salaries
average = ftEmpA.averageSalary(listemp)

#make it look like a dollar amount
formattedAverage = round(average, 2)
print(str(formattedAverage))
