#Define a Student class with attributes like name and age. 
# Include a method to display student information.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def student_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
student1 = Student("allan", 43)
print(f"{student1.student_info()}")
    
    