
class person:
    
    def __init__(self, name, address, city, state, zipcode, age):

        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.age = age

class student(person):
    def __init__(self, name, address, city, state, zipcode, age, studentid, gpa):

        #super class is the primary class
        super().__init__(name, address, city, state, zipcode, age)

        self.studentid = studentid
        self.gpa = gpa
    
class teacher(person):
    def __init__(self, name, age, teacherid, classteaching):
        #super().__init__(name, age)
        self.name = name
        self.age = age
        self.teacherid = teacherid
        self.classteaching = classteaching

student = student("Jane Doe","123 St",'Santa Ana','California',12345,21,123,4.0)
print("Student Name: ",student.name)
print("Student Address: ",student.address)
print("Student City: ",student.city)
print("Student State: ",student.state)
print("Student Zipcode: ",student.zipcode)
print("Student Age: ",student.age)
print("Student ID: ",student.studentid)
print("Student gpa: ",student.gpa)
print()

teacher = teacher("teacher Bob",43,456,"programming")
print("Teacher Name: ",teacher.name)
print("Teacher Age: ",teacher.age)
print("Teacher ID: ",teacher.teacherid)
print("Class Name: ",teacher.classteaching)