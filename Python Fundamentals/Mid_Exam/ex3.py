shelf_of_books = input().split("&")

input_line = input()
while input_line != "Done":
    command = input_line.split(" | ")

    if "Add Book" in command:
        book_name = command[1]
        if book_name not in shelf_of_books:
            shelf_of_books.insert(0, book_name)

    elif "Take Book" in command:
        book_name = command[1]
        if book_name in shelf_of_books:
            shelf_of_books.remove(book_name)

    elif "Swap Books" in command:
        book1 = command[1]
        book2 = command[2]
        if book1 in shelf_of_books and book2 in shelf_of_books:
            book1_index = shelf_of_books.index(book1)
            book2_index = shelf_of_books.index(book2)
            shelf_of_books[book1_index], shelf_of_books[book2_index] = \
                shelf_of_books[book2_index], shelf_of_books[book1_index]

    elif "Insert Book" in command:
        book_name = command[1]
        if book_name not in shelf_of_books:
            shelf_of_books.insert(len(shelf_of_books), book_name)

    elif "Check Book" in command:
        book_index = int(command[1])
        if 0 <= book_index < len(shelf_of_books):
            print(shelf_of_books[book_index])

    input_line = input()

print(", ".join(shelf_of_books))