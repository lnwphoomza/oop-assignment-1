books = []
members = []
borrowed_books = []

class Book:
    def __init__(self, id, title, author, total_copies, available_copies):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = available_copies

class Member:
    def __init__(self, member_id, book_id, name, email, borrowed_books_list):
        self.member_id = member_id
        self.book_id = book_id
        self.name = name
        self.email = email
        self.borrowed_books_list = borrowed_books_list

    def borrow_book(self, member_id, book_id):
        """Process a book borrowing transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not member:
            print("Error: Member not found!")
            return False
        
        if not book:
            print("Error: Book not found!")
            return False
        
        if book['available_copies'] <= 0:
            print("Error: No copies available!")
            return False
        
        if len(member['borrowed_books']) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False
        
        # Process the borrowing
        book['available_copies'] -= 1
        member['borrowed_books'].append(book_id)
        
        transaction = {
            'member_id': member_id,
            'book_id': book_id,
            'member_name': member['name'],
            'book_title': book['title']
        }

        borrowed_books.append(transaction)
        
        print(f"{member['name']} borrowed '{book['title']}'")
        return True