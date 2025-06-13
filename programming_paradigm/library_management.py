# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self._is_checked_out = False
    
#     def __str__(self):
#         return f"{self.title} by {self.author}"
    
#     def is_available(self):
#         return not self._is_checked_out
    
#     def check_out(self):
#         self._is_checked_out = True
    
#     def return_book(self):
#         self._is_checked_out = False
    
# class  Library:
#     def __init__(self):
#         self.__books = []
    
#     def add_book(self, book):
#         self.__books.append(book)


#     def check_out_book(self, title):
#         for book in self._books:
#             if book.title == title and book.is_available():
#                 book.check_out()
#                 print(f"Checked out: {book.title}")
#                 return
#         print(f"Book '{title}' is not available for checkout.")
    
    
#     def return_book(self, title):
#         for book in self._books:
#             if book.title == title and not book.is_available():
#                 book.return_book()
#                 print(f"Returned: {book.title}")
#                 return
#         print(f"Book '{title}' was not checked out or does not exist.")


#     def list_available_books(self):
#         print("Available books:")
#         available_found = False
#         for book in self._books:
#             if not book._is_checked_out:
#                 print(f"  - {book}")
#                 available_found = True
        
#         if not available_found:
#             print("  No books available")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False 
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def is_available(self):
        return not self._is_checked_out
    
    def check_out(self):
        self._is_checked_out = True
    
    def return_book(self):
        self._is_checked_out = False


class Library:
    def __init__(self):
        self._books = []  
    
    def add_book(self, book):
        self._books.append(book)
    
    
    def check_out_book(self, title):
       for book in self._books:
            if book.title.lower() == title.lower():

                if book._is_checked_out:
                    print(f"Error: '{title}' is already checked out")
                else:
                    book.check_out()  
                return 
        
    
    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():  # Case-insensitive search
                if not book._is_checked_out:
                    print(f"Error: '{title}' wasn't checked out")
                else:
                    book.return_book()  # Return the book
                return  
    
    def list_available_books(self):
        print("Available books:")
        available_found = False
        for book in self._books:
            if not book._is_checked_out:
                print(f"  - {book}")
                available_found = True
        
        if not available_found:
            print("  No books available")