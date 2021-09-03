from person2 import Person2


class Person:
    def __init__(self):
        self.fname = ""
        self.lname = ""

    def setFname(self, value):
        self.fname = value


    def getFname(self):
        return self.fname


    def setLname(self, value):
        self.lname = value



    def getLname(self):
        return self.lname


class Student(Person):
    pass


class Student2(Person2):
    def __init__(self, fname, lname, stNumber):
        super().__init__(fname, lname, stNumber)

    def studentInfo(self):
        print("The name of this person is" + self.fname + " " + self.lname + " " + self.stNumber)