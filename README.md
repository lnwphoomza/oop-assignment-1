This Library Management System is a Python-based console application that demonstrates how to manage books, members,
and borrowing/returning transactions in a procedural programming style — while still using classes for structure.

This assignment want you to create the classes and build methods in each 3 classes (such as Book, Member, Library) by using the functions below that have in the original code.

There are so many functions and many variable, I put almost every functions to be the methods in every classes, I put it in each classes by specific the role of each functions.

Some function might be in many classes such as __init__ and borrow_book. 

Class Book represents a book record and there are lots of attributes in this class such as id, title, author, total_copies, available_copies.

Class Member represents a LIBRARY member. and there are 5 attributes in this class such as member_id, book_id, name, emal, borrowed_books_list and a method name borrow_book this method
used for allows a member to borrow a book.

and in class Library there are so many methods that shows below this text
                    |
                    |
                    |
                    |
                    V
  add_book(book_id, title, author, available_copies)
  add_member(member_id, name, email)
  borrow_book(member_id, book_id)
  return_book(member_id, book_id)
  display_available_books()
  display_member_books(member_id)
  find_book(book_id)
  find_member(member_id)

And finally I ran this code with this command.
  if __name__ == "__main__":
    test_library_system()

Thank you for reading!!!
  Tanisorn Pisittanaphat 6810545671
  
