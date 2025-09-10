

class library:
    def __init__(self):
        self.book=[]
        self.issued_book={}

    def add_book(self,title):
        self.book.append(title)
        print(f"{title} has been added to the library")

    def display_books(self):
        if self.book:
            print("library contains the following books:")
            for x in self.book:
                print('->',x) 
        else:
            print("library is empty")
    def lend_book(self,title,user):
        if title in self.book:
            self.book.remove(title)
            self.issued_book[title]=user
            print(f"{title}has been issued to {user}")
        else:
            print(f"{title} is not avaliable in library")
    

    def return_book(self,title):
        if title in self.issued_book.keys():
            self.book.append(title)
            self.issued_book.pop(title)
            print(f"{title}has been returned to library")
        else:
            print(f"{title} is not issued from library")

lib=library()
lib.add_book("python")
lib.add_book("Data Science")
lib.add_book("sql")
lib.display_books()
lib.lend_book("python","nani")
lib.return_book("python")
lib.display_books()
