class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am studying {self.course}.")

student1 = Student("Nikka Jane Senado", 21, "DIP-Information Technology")
student2 = Student("Jane Senado", 22, "DIP-Culinary")
student3 = Student("Niks Senado", 20, "DIP-Hotel Management")

print("Student 1:")
student1.introduce()
print("Student 2:")
student2.introduce()
print("Student 3:")
student3.introduce()
