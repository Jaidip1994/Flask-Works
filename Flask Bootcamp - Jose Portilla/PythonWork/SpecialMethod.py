class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __repr__(self) -> str:
        return f'Title: {self.title}, Author: {self.author}'
    
    def __len__(self):
        return self.pages

myBook = Book('Python Rocks!', 'Jose', 250)
print(myBook)
print(len(myBook))

# __repr__ method is the way to define on printing class instance whats to show
# __len__ and __repr__ are the special methods