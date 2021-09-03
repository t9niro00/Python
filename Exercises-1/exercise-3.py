from person import Person
from person import Student


objectPerson1 = Person()

objectStudent = Student()

objectPerson1.setFname("Lisa")

objectPerson1.setLname("Smith")

objectStudent.setFname("Ressu")

objectStudent.setLname("Redford")


print(objectPerson1.getFname())

print(objectPerson1.getLname())

print(objectStudent.getFname())

print(objectStudent.getLname())