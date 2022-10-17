from book import Book


class Library():
    def __init__(self):
        """Initialize the empty book list"""
        self.books = []

    def add_title(self, title, author):
        """Add a Book object with the given title and author to the book list"""
        book = {}
        book['title'] = title
        book['author'] = author
        book = Book (title, author)
        self.books.append(book)
        
        
    def count_books(self):
        """Return the number of books currently in the booklist"""
        return len(self.books)
            

    def remove_title(self, title):
        for i in self.books:
            if i.title == title:
                self.books.remove(i)
        return self.books
        # if title == self.books:
        #     return self.books.remove(title)
            
    def display_books(self):
        for i in self.books:
            print(f"{i.title} - {i.author}")          
      

    def is_empty(self):
        """Return True if the book list is empty, False if not"""
        return self.books == []
