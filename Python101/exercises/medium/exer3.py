class Library:
    def __init__(self, collection = None):
        if collection is None:
            collection = []
        self.collection = collection

    def add_book(self,book):
        self.collection.append(book)

    def list_books(self):
        return self.collection

    def find_book(self,title):
        for book in self.collection:
            if book.title.lower() == title.lower():
                checkout_status = "Checked out" if book.is_checked_out else "Available"
                return f"{book.title} by {book.author} ({book.year}) - {checkout_status}"
        else:
            print(f"{title} is not found in the library")
    
    def available_books(self):
        return [book for book in self.collection if not book.is_checked_out]

class Book:
    def __init__(self, title, author, year, is_checked_out=False):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = is_checked_out

    def checkout(self):
        self.is_checked_out = True
    
    def return_book(self):
        self.is_checked_out = False

    def __str__ (self):
        return f"{self.title} by {self.author}, published in {self.year}"
    

b1 = Book("1984", "George Orwell", 1949)
b2 = Book("The Alchemist", "Paulo Coelho", 1988)
b3 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1995, True)

# Add books to the library
lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

print("All Books:")
for book in lib.list_books():
    print(book)

print("\nAvailable Books in the Library not checked out:")
for book in lib.available_books():
    print(book)

print("\nFinding '1984':")
found = lib.find_book("1984")
if found:
    print(found)


    