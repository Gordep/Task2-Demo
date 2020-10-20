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
        Person.__init__(self, fname, lname)


class Team:
    def __init__(self, name):
        self.name = name
        self.members = []
        
    def add_member(self, student):
        self.members.append(student)


a = Student("Alex", "Ortega")
b = Student("Abram", "Nguyen")
c = Student("Luis", "Medina")
d = Student("Julian", "Gonzalez")
e = Student("Brian", "Perez")

t = Team("Team 4")
t.add_member(a)
t.add_member(b)
t.add_member(c)
t.add_member(d)
t.add_member(e)