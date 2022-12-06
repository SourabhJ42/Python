class Employee:
    deartment_name = "Human Resource"

    @classmethod
    def get_department_name(cls):
        return cls.deartment_name

    def __init__(self, e_id, sal, m_id):
        self.emp_id = e_id
        self.__salary = sal
        self.mgr_id = m_id

    def set_salary(self):
        self.__salary = self.__salary

    def get_salary(self):
        return self.__salary

    @staticmethod
    def field_expertise():
        print("Finance")


employee1 = Employee(100, 1000, 1)

print(employee1.emp_id)
print(employee1._Employee__salary)
print(employee1.mgr_id)

print(Employee.get_department_name())

employee1.field_expertise()

del employee1.mgr_id
del employee1

