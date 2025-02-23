class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

car1 = Car("Ford", "Mustang", 2023)
car2 = Car("Chevrolet", "Camaro", 2021)

print("Car 1:")
car1.display_info()
print("Car 2:")
car2.display_info()
