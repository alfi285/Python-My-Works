# 2-Simple Python program with ENCAPSULATION ?

class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_name(self):
        return f"Name:{self.name}"

    def get_age(self):
        return f"Age:{self.age}"

    def get_salary(self):
        return f"Salary:{self.salary}"

    def set_name(self,newname):
        self.name = newname

    def set_age(self,newage):
        self.age = newage

    def set_salary(self,newsalary):
        self.salary = newsalary

e1 = Employee("Alfiya",31,50000)
print("Employee Details\n",e1.get_name(),"\n",e1.get_age(),"\n"+e1.get_salary())

e1.set_name("Alfiya A")
e1.set_age(25)
e1.set_salary(60000)
print("Employee Details after updation\n",e1.get_name(),"\n",e1.get_age(),"\n"+e1.get_salary())
