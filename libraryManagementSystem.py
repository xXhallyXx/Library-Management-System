class Library:
    __book_list = []
    
    @classmethod
    def entry_book(self, book):
        self.__book_list.append(book)
    
    @classmethod
    def get_all_books(self):
        return self.__book_list
    
    @classmethod
    def find_book_by_id(self, book_id):
        for book in self.__book_list:
            if book._Book__book_id == book_id:
                return book
        return None


class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)
    
    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"Book '{self.__title}' has been borrowed.")
        else:
            print(f"Book '{self.__title}' is already borrowed.")
    
    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"Book '{self.__title}' has been returned.")
        else:
            print(f"Book '{self.__title}' is not borrowed.")
    
    def view_book_info(self):
        if self.__availability:
            status = 'Available'
        else:
            status = 'Not Available'
        print(f"ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {status}")


def menu():
    while True:
        print("\nLibrary Menu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            books = Library.get_all_books()
            if books:
                for book in books:
                    book.view_book_info()
            else:
                print("No books available.")
        
        elif choice == '2':
            book_id = input("Enter the Book ID to borrow: ")
            book = Library.find_book_by_id(book_id)
            if book:
                book.borrow_book()
            else:
                print("Invalid Book ID.")
        
        elif choice == '3':
            book_id = input("Enter the Book ID to return: ")
            book = Library.find_book_by_id(book_id)
            if book:
                book.return_book()
            else:
                print("Invalid Book ID.")
        
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice.")



book1 = Book('1', 'ABC', 'X')
book2 = Book('2', 'DEF', 'Y')
book3 = Book('3', 'GHI', 'Z')


menu()
