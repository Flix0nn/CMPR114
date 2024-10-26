class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        self.name = input("enter your name: ")
        while True:
            try:
                self.age = int(input('enter the age: '))
                break
            except ValueError:
                print('enter a valid age')

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

#SAC Student class inheriting the person class
class SACStudent(Person):
    def __init__(self,name='', age=0):
        super().__init__(name, age)

if __name__ == "__main__":

    student = SACStudent()
    student.get_info()
    print(student.display_info())


