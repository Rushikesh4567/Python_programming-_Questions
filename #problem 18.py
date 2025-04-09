#problem 18
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def display(self):
        print("\nDisplay details of a book")
        print(self.title)
        print(self.author)


title=input("Enter the title of book: ")
author = input("Enter book's author name: ")
s=Book(title,author)
s.display()