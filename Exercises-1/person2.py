class Person2:
    def __init__(self, fname, lname, stNumber):
        self.fname = fname
        self.lname = lname
        self.stNumber = stNumber

    def personInfo(self):
        print("The name of this person is" + self.fname + " " + self.lname)