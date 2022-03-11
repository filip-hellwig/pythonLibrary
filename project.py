
class Library:
    def __init__(self, name, city, number, books = {}, readers = {}, numberOfBooks = 0, numberOfReaders = 0) -> None:
        self.name = name
        self.city = city
        self.number = number
        self.books = books
        self.readers = readers
        self.numberOfBooks = numberOfBooks
        self.numberOfReaders = numberOfReaders

    def printInfo(self):
        print(f"{self.name} nr. {self.number} in {self.city}") 
        print(f"Number of books: {len(self.books)}, Number of readers: {len(self.readers)}")

    def addBook(self):
        book = self.Book()
        book.title = input("Title: ")
        book.author = input("Author: ")
        book.date = input("Date: ")
        book.category = input("Category: ")
        self.numberOfBooks += 1
        book.number = self.numberOfBooks - 1
        self.books[book.number] = book

    def addManyBooks(self):
        f = open("books.txt")

        for line in f:
            newBook = line.split(", ")
            print(line)

    def addReader(self):
        reader = self.Reader()
        reader.name = input("Name: ")
        reader.surname = input("Surname: ")
        reader.age = input("Age: ")

        self.numberOfReaders += 1
        reader.number = self.numberOfReaders - 1
        self.readers[reader.number] = reader

    def searchBookTitle(self, title):
        for i in self.books:
            if self.books[i].title == title:
                return i
    
    def searchReaderSurname(self, surname):
        for i in self.readers:
            if self.readers[i].surname == surname:
                return i

    def borrowBook(self):
        who = input("Surname: ")
        indexReader = self.searchReaderSurname(who)

        whichBook = input("Title: ")
        indexBook = self.searchBookTitle(whichBook)
        self.books[indexBook].borrow()

        self.readers[indexReader].borrow(indexBook)




    class Book:
        def __init__(self, title = None, author = None, date = None, category = None, isBorrowed = False, number = 0):
            self.title = title
            self.author = author
            self.date = date
            self.number = number
            self.category = category
            self.isBorrowed = isBorrowed
        
        def printInfo(self):
            if self.isBorrowed:
                print(f"{self.number}. {self.title} by {self.author} published in {self.date}. Is borrowed")
            else:
                print(f"{self.number}. {self.title} by {self.author} published in {self.date}. Is not borrowed")
        
        def borrow(self):
            self.isBorrowed = True
        
        def giveBack(self):
            self.isBorrowed = False

    class Reader:
        def __init__(self, name = None, surname = None, age = None, number = 0, books = []):
            self.name = name
            self.surname = surname
            self.age = age
            self.number = number
            self.books = books     

        def printInfo(self):
            print(f"{self.name} {self.surname}, age: {self.age}")
            print(f"Borrowed books {self.books[0]}") 
        
        def borrow(self, number):
            self.books.append(number)

filia1 = Library('Filia', 'Wrocław', 1)
filia1.printInfo()
filia1.addManyBooks()
filia1.addBook()
filia1.addReader()

filia1.borrowBook()

filia1.books[0].printInfo()
filia1.readers[0].printInfo()
