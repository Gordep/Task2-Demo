class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

    def countToTen(self):
        for x in range (1, 11):
            print("number:", x)

class Student(Person):
    def __init__(self, fname, lname):
        print("Student class was called:")
        Person.__init__(self, fname, lname)
        print("printname() was inherited from Person:")
        self.printname() 

    def changeName(self):
        print("Xela Agetro")

student = Student("Alex", "Ortega")
print("countToTen() was inherited from Person:")
student.countToTen()
print("changeName() is from Student:")
student.changeName()