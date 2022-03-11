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

    def printAllBooks(self):
        for book in self.books:
            self.books[book].printInfo()
    
    def printAllReaders(self):
        for reader in self.readers:
            self.readers[reader].printInfo()


    def addBook(self):
        book = self.Book()
        book.title = input("Title: ")
        book.author = input("Author: ")
        book.date = input("Date: ")
        book.category = input("Category: ")
        self.numberOfBooks += 1
        book.number = self.numberOfBooks - 1
        self.books[book.number] = book

    def addBook2(self, list):
        book = self.Book()
        book.title = list[0]
        book.author = list[1]
        book.date = list[2]
        book.category = list[3]
        self.numberOfBooks += 1
        book.number = self.numberOfBooks - 1
        self.books[book.number] = book

    def addManyBooks(self, file):
        f = open(file)

        for line in f:
            line = line.replace("\n", "")
            newBook = line.split(", ")
            self.addBook2(newBook)

        f.close()
            

    def addReader(self):
        reader = self.Reader()
        reader.name = input("Name: ")
        reader.surname = input("Surname: ")
        reader.age = input("Age: ")

        self.numberOfReaders += 1
        reader.number = self.numberOfReaders - 1
        self.readers[reader.number] = reader

    def addReader2(self, list):
        reader = self.Reader()
        reader.name = list[0]
        reader.surname = list[1]
        reader.age = list[2]

        self.numberOfReaders += 1
        reader.number = self.numberOfReaders - 1
        self.readers[reader.number] = reader

    def addManyReaders(self, file):
        f = open(file)

        for line in f:
            line = line.replace("\n", "")
            newReader = line.split(", ")
            self.addReader2(newReader)

        f.close()

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

    def giveBackBook(self):
        who = input("Surname: ")
        indexReader = self.searchReaderSurname(who)

        whichBook = input("Title: ")
        indexBook = self.searchBookTitle(whichBook)
        self.books[indexBook].giveBack()

        self.readers[indexReader].giveBack(indexBook)

    def bookInfo(self):
        whichBook = input("Title: ")
        indexBook = self.searchBookTitle(whichBook)
        self.books[indexBook].printInfo()

    def readerInfo(self):
        who = input("Surname: ")
        indexReader = self.searchReaderSurname(who)
        toRead = self.readers[indexReader].printInfo()
        print(f"Borrowed books:")
        for books in toRead:
            print(f"{self.books[books].title}") 
        



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
            return self.books

        def borrow(self, number):
            self.books.append(number)

        def giveBack(self, number):
            index = self.books.index(number)
            self.books.pop(index)


def menuOption(option, branch):
    if option == 0:
        print("Exiting...")
        quit()
    elif option == 1:
        branch.borrowBook()
    elif option == 2:
        branch.giveBackBook()
    elif option == 3:
        branch.addBook()
    elif option == 4:
        branch.addReader()
    elif option == 5:
        file = input("Enter file name: ")
        branch.addManyBooks(file)
    elif option == 6:
        file = input("Enter file name: ")
        branch.addManyReaders(file)
    elif option == 7:
        branch.printAllBooks()
    elif option == 8:
        branch.printAllReaders()
    elif option == 9:
        branch.bookInfo()
    elif option == 10:
        branch.readerInfo()
    else:
        print("Wrong option...")


def menuInfo():
    print("1. Borrow book")
    print("2. Give back book")
    print("3. Add book")
    print("4. Add reader")
    print("5. Add many books")
    print("6. Add many readers")
    print("7. Print all books")
    print("8. Print all readers")
    print("9. Book info")
    print("10. Reader info")
    print("0. Exit")

print("\n\n")
filia1 = Library('Filia', 'Wrocław', 1)
filia1.addManyBooks("books.txt")
filia1.addManyReaders("readers.txt")
filia1.printInfo()

while 1:
    print("\n")
    menuInfo()
    userInput = int(input("\nEnter menu option: "))
    menuOption(userInput, filia1)

