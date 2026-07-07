class BookIterator:
    def __init__(self,books:list[str]):
        self.books=books
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<len(self.books):
            book=self.books[self.index] 
            self.index+=1
            return book
        raise StopIteration
books=["The Alchemist","Harry Potter","Oliver Twist","The Great Gatsby","1984","Atomic Habits"]
book_iterator=BookIterator(books)
for book in book_iterator:
    print(book)