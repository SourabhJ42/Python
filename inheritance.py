"""Exercise on Inheritance:
-------------------------
Create a base class named Employee as follows:
Employee (
-- class variables and methods
	organisation_name,
	get_organisation_name(),
	set_organisation_name(org_name)

-- instance variables and methods()
emp_id,
name,
base_location,
deployed_location,
designation,
salary ,
get_employee_details()

Create a subclass of Employee named Manager as follows:
Manager(
-- instance variables and methods()
	managed_employees[],
	perform_appraisal_for_an_employee(emp_id,percent_raise),
	get_manager_details(mgr_id)
)

Write a main method that does the following:
create 3 objects of Employee
create an object of Manager_class and add the above 3 employee objects created as managed employees
display get_manager_details()
for an employee do perform_appraisal_for_an_employee()


"""


class Employee:
    organisation_name = "CDAC"

    @classmethod
    def get_organisation_name(cls):
        return cls.organisation_name

    @classmethod
    def set_organization_name(cls, o_name):
        cls.organisation_name = o_name

    def __init__(self, e_id, e_name, b_loc, d_loc, desig, sal):
        self.emp_id = e_id
        self.name = e_name
        self.base_location = b_loc
        self.deployed_location = d_loc
        self.designation = desig
        self.__salary = sal

    def get_employee_details(self):
        return f"Employee details::\nEmployee ID : {self.emp_id}\nEmployee Name : {self.name}\nBase Location : {self.base_location}\nDeployed Location : {self.deployed_location}\nDesignation : {self.designation}\n"

    def set_salary(self, per):
        self.__salary = self.__salary + ((self.__salary * per) / 100)

    def get_salary(self):
        return self.__salary


class Manager(Employee):
    def __init__(self, e_id, e_name, b_loc, d_loc, desig, sal, managed_emp):
        super().__init__(e_id, e_name, b_loc, d_loc, desig, sal)
        self.managed_employees = []
        self.managed_employees.extend(managed_emp)

    def get_employees_list(self):
        for m in self.managed_employees:
            print(m.get_salary())

    def perform_appraisal_for_an_employee(self, empId, percent_raise):
        for e in self.managed_employees:
            if e.emp_id == empId:
                e.set_salary(percent_raise)
                break


e1 = Employee(1, "saurabh", "Pune", "Dubai", "Researcher", 150000)
print(e1.get_employee_details())

e2 = Employee(2, "Vaibhav", "Pune", "Mumbai", "Developer", 5000)
print(e2.get_employee_details())

e3 = Employee(3, "Abhishek", "Pune", "new york", "Analyst", 15800)
print(e3.get_employee_details())

lists = [e1, e2, e3]
m1 = Manager(101, "Jason", "California", "Vegas", "Sr. Manager", 1500000, lists)

m1.perform_appraisal_for_an_employee(2, 10)
print(e2.get_salary())
