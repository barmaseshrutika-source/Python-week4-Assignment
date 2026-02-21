class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book} added successfully!")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} removed successfully!")
        else:
            print("Book not found!")

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} issued successfully!")
        else:
            print("Book not available!")

    def return_book(self, book):
        self.books.append(book)
        print(f"{book} returned successfully!")

    def display_books(self):
        print("Available Books:", self.books)

