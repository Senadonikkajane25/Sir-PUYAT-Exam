# task2.py
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am studying {self.course}.")

student1 = Student("Nikka Jane Senado", 21, "DIP-Information Technology")
student2 = Student("Jane Senado", 22, "DIP-Information Technology")
student3 = Student("Niks Senado", 20, "DIP-Information Technology")

student1.introduce()
student2.introduce()
student3.introduce()
