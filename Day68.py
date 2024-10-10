class library:
    def __init__(self):
        self.nobooks = 0 
        self.books= []

    def addbooks(self , books):
        self.books.append(books)
        self.nobooks = len(self.books)

    def showinfo(self):
        print(f"the total number of books in library is : {self.nobooks} books . the boooks are ")
        for books in self.books:
            print(books)

l1 =library()

l1.addbooks("book1")
l1.addbooks("book2")
l1.addbooks("book3")
l1.addbooks("book4")
l1.addbooks("book5")

l1.showinfo()