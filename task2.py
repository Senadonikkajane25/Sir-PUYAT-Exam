# task2.py

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am studying {self.course}.")

# Create three student objects
student1 = Student("Nikka Jane Senado", 20, "DIP-Information Technology 2")
student2 = Student("Charmaine Villanueva", 22, "DIP-Information Technology 2")
student3 = Student("Jhen Senado", 21, "DIP-Information Technology 2")

# Call the introduce() method for each student
student1.introduce()
student2.introduce()
student3.introduce()
