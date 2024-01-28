class College:
    def __init__(self,name,dept):
        self.name = name
        self.dept = dept
    
    def printname(self):
        print(f"He is {self.name} and he is from {self.dept} {self.section}")

class Student(College):
    def __init__(self, name, dept, section):
        super().__init__(name, dept)
        self.section = section
    
p1 = Student("Goutham", "CSBS","A")

p1.printname()