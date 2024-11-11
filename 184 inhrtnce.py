#3-Simple Python program with INHERITANCE?
from symtable import Class


class Classs:
    def __init__(self,departmentname,numberofstudents):
        self.department = departmentname
        self.numberofstudent = numberofstudents

    def get_department(self):
        return f"Department Name:{self.department}"

    def get_students_number(self):
        return f"Number of students:{self.numberofstudent}"

class ComputerScience(Classs):
    def __init__(self, departmentname, numberofstudents):
        super().__init__(departmentname, numberofstudents)

class Mathematics(Classs):
    def __init__(self, departmentname, numberofstudents):
        super().__init__(departmentname, numberofstudents)

c1 = ComputerScience("Computer Science",1000)
m1 = Mathematics("Mathematics",2000)
print(c1.get_department()+"\n"+c1.get_students_number())
print(m1.get_department()+"\n"+m1.get_students_number())



