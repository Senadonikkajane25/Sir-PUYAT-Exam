# task4.py

class Book:
    def __init__(self, title, author, year_published):
        # Initialize the book object with title, author, and year published
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        # Method to display book details
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        print("-" * 30)

# Create three book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("1984", "George Orwell", 1949)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

# Display the details of each book
book1.describe()
book2.describe()
book3.describe()
