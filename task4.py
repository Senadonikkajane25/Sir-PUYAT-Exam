class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        print("-" * 30)

book1 = Book("Brave New World", "Aldous Huxley", 1932)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
book3 = Book("Fahrenheit 451", "Ray Bradbury", 1953)

book1.describe()
book2.describe()
book3.describe()
