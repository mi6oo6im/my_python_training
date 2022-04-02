searched_book = input()
books_looked = 0
current_book = input()
book_is_found = False

while current_book != "No More Books":
    if current_book == searched_book:
        book_is_found = True
        break
    books_looked += 1
    current_book = input()

if book_is_found:
    print(f"You checked {books_looked} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_looked} books.")


