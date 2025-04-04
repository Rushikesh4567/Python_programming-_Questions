#problem 11
def remove_duplicates(book_list):
    unique_books = list(set(book_list)) 
    return unique_books


books = [
    "Wngs of fire", "Atomic habits", "1984", 
    "wings of fire", "The secret", "1984", "Can't hurt me"
]

unique_books = remove_duplicates(books)
print("Unique Book Titles:")
for book in unique_books:
    print(book)
