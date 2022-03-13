# class that has all methods needed by the library
class Library:

    # initialization
    def __init__(self, name, city, number, books = {}, readers = {}, numberOfBooks = 0, numberOfReaders = 0) -> None:
        self.name = name        # name of library
        self.city = city        # name of city 
        self.number = number    # index number of library
        self.books = books      # dictonary of books, key word is the index of book
        self.readers = readers      # dictonary of readers, key word is the index of reader
        self.numberOfBooks = numberOfBooks      # number of book registered in the library
        self.numberOfReaders = numberOfReaders      # number of readers registered in the library


    # info about library
    def printInfo(self):
        print(f"{self.name} nr. {self.number} in {self.city}") 
        print(f"Number of books: {len(self.books)}, Number of readers: {len(self.readers)}")

    # print all registered books
    def printAllBooks(self):
        for book in self.books:
            self.books[book].printInfo()
    
    # print all registered readers
    def printAllReaders(self):
        for reader in self.readers:
            self.readers[reader].printInfo()

    # adds book to dictonary, without argument
    def addBook(self):
        title = input("Title: ")
        author = input("Author: ")
        date = input("Date: ")
        category = input("Category: ")

        f = open("books.txt", "a")
        f.write(f"\n{title}, {author}, {date}, {category}")
        f.close()

        self.numberOfBooks += 1
        number = self.numberOfBooks - 1
        self.books[number] = self.Book(title, author, date, category, number)

    # adds book to dictonary, with argument
    def addBook2(self, list):
        title = list[0]
        author = list[1]
        date = list[2]
        category = list[3]

        f = open("books.txt", "a")
        f.write(f"\n{title}, {author}, {date}, {category}")
        f.close()

        self.numberOfBooks += 1
        number = self.numberOfBooks - 1
        self.books[number] = self.Book(title, author, date, category, number)

    # adds book to dictonary, with argument, without appending file
    def addBook3(self, list):
        title = list[0]
        author = list[1]
        date = list[2]
        category = list[3]
        self.numberOfBooks += 1
        number = self.numberOfBooks - 1
        self.books[number] = self.Book(title, author, date, category, number)

    # adds many books to dictonary, from a file
    def addManyBooks(self, file):
        try:
            f = open(file)

            for line in f:
                line = line.replace("\n", "")
                newBook = line.split(", ")
                self.addBook2(newBook)

            f.close()
        except:
            print("File error")
            return

    # load book database
    def loadBooks(self, file):
        try:
            f = open(file)

            for line in f:
                line = line.replace("\n", "")
                newBook = line.split(", ")
                self.addBook3(newBook)

            f.close()
        except:
            print("File error")
            return
          
    # adds reader to dictonary, without argument
    def addReader(self):
        name = input("Name: ")
        surname = input("Surname: ")
        age = input("Age: ")
        books = []

        f = open("readers.txt", "a")
        f.write(f"\n{name}, {surname}, {age}")
        f.close()

        self.numberOfReaders += 1
        number = self.numberOfReaders - 1
        self.readers[number] = self.Reader(name, surname, age, number, books)

    # adds reader to dictonary, wtih argument
    def addReader2(self, list):
        name = list[0]
        surname = list[1]
        age = list[2]
        books = []

        f = open("readers.txt", "a")
        f.write(f"\n{name}, {surname}, {age}")
        f.close()

        self.numberOfReaders += 1
        number = self.numberOfReaders - 1
        self.readers[number] = self.Reader(name, surname, age, number, books)

    # adds reader to dictonary, wtih argument, without appending file
    def addReader3(self, list):
        name = list[0]
        surname = list[1]
        age = list[2]
        books = []

        self.numberOfReaders += 1
        number = self.numberOfReaders - 1
        self.readers[number] = self.Reader(name, surname, age, number, books)
   
    # adds many readers, from file
    def addManyReaders(self, file):
        try:
            f = open(file)

            for line in f:
                line = line.replace("\n", "")
                newReader = line.split(", ")
                self.addReader2(newReader)

            f.close()
        except:
            print("File error")
            return

    # loads reader database
    def loadReaders(self, file):
        try:
            f = open(file)

            for line in f:
                line = line.replace("\n", "")
                newReader = line.split(", ")
                self.addReader3(newReader)

            f.close()
        except:
            print("File error")
            return

    # search for a book by title
    def searchBookTitle(self, title):
        for i in self.books:
            if self.books[i].getTitle() == title:
                return i
        return -1

    #search for a book by number
    def searchBookNumber(self, number):
        for i in self.books:
            if self.books[i].getNumber() == int(number):
                return i
        return -1
    
    # search for a reader by surname
    def searchReaderSurname(self, surname):
        for i in self.readers:
            if self.readers[i].getSurname() == surname:
                return i
        return -1

    # search for a reader by number
    def searchReaderNumber(self, number):
        for i in self.readers:
            if self.readers[i].getNumber() == int(number):
                return i
        return -1

    # lets reader borrow book
    def borrowBook(self):
        who = input("Surname: ")
        indexReader = self.searchReaderSurname(who)
        if indexReader == -1:
            print("Reader does not exist")
            return

        whichBook = input("Title: ")
        indexBook = self.searchBookTitle(whichBook)
        if indexBook == -1:
            print("Book does not exist")
            return

        if self.books[indexBook].getBorrowed() == True:
            print("This book is unavaiable")
            return

        if len(self.readers[indexReader].books) == 2:
            print("You can only have 2 books")
            return

        self.books[indexBook].borrow()
        self.readers[indexReader].borrow(indexBook)

    # lets reader borrow book by index numbers
    def borrowBookNumber(self):
        who = input("Reader number: ")
        indexReader = self.searchReaderNumber(who)
        if indexReader == -1:
            print("Reader does not exist")
            return

        whichBook = input("Book number: ")
        indexBook = self.searchBookNumber(whichBook)
        if indexBook == -1:
            print("Book does not exist")
            return

        if self.books[indexBook].getBorrowed() == True:
            print("This book is unavaiable")
            return

        if len(self.readers[indexReader].books) == 2:
            print("You can only have 2 books")
            return

        self.books[indexBook].borrow()
        self.readers[indexReader].borrow(indexBook)

    # allows to give back book
    def giveBackBook(self):
        who = input("Surname: ")
        indexReader = self.searchReaderSurname(who)
        if indexReader == -1:
            print("Reader does not exist")
            return
        
        whichBook = input("Title: ")
        indexBook = self.searchBookTitle(whichBook)
        if indexBook == -1:
            print("Book does not exist")
            return
        
        if self.readers[indexReader].giveBack(indexBook) != -1:
            self.books[indexBook].giveBack()

    # allows to give back book by index number
    def giveBackBookNumber(self):
        who = input("Reader number: ")
        indexReader = self.searchReaderNumber(who)
        if indexReader == -1:
            print("Reader does not exist")
            return
        
        whichBook = input("Book number: ")
        indexBook = self.searchBookNumber(whichBook)
        if indexBook == -1:
            print("Book does not exist")
            return
        
        if self.readers[indexReader].giveBack(indexBook) != -1:
            self.books[indexBook].giveBack()

    # information about one book
    def bookInfo(self):
        whichBook = input("Title: ")
        indexBook = self.searchBookTitle(whichBook)
        if indexBook == -1:
            print("Book does not exist")
            return
            
        self.books[indexBook].printInfo()

    # information about one book by number
    def bookInfoNumber(self):
        whichBook = input("Number: ")
        indexBook = self.searchBookNumber(whichBook)
        if indexBook == -1:
            print("Book does not exist")
            return
            
        self.books[indexBook].printInfo()

    # information about one reader by number
    def readerInfo(self):
        who = input("Surname: ")
        indexReader = self.searchReaderSurname(who)
        if indexReader == -1:
            print("Reader does not exist")
            return

        toRead = self.readers[indexReader].printInfo()
        print(f"Borrowed books:")
        for books in toRead:
            print(f"{self.books[books].getTitle()}") 

    # information about one reader by number
    def readerInfoNumber(self):
        who = input("Number: ")
        indexReader = self.searchReaderNumber(who)
        if indexReader == -1:
            print("Reader does not exist")
            return

        toRead = self.readers[indexReader].printInfo()
        print(f"Borrowed books:")
        for books in toRead:
            print(f"{self.books[books].getTitle()}") 
        
    # information about all books in category
    def allBooksInCategory(self):
        category = input("Enter category: ")
        for i in self.books:
            if self.books[i].getCategory() == category:
                self.books[i].printInfo()

    class Book:

        # initialization
        def __init__(self, title = None, author = None, date = None, category = None, number = 0, isBorrowed = False):
            self.title = title
            self.author = author
            self.date = date
            self.number = number
            self.category = category
            self.isBorrowed = isBorrowed
        
        # print info about book
        def printInfo(self):
            if self.isBorrowed:
                print(f"{self.number}. {self.title} by {self.author} published in {self.date}. Is borrowed")
            else:
                print(f"{self.number}. {self.title} by {self.author} published in {self.date}. Is not borrowed")
        
        # sets book as borrowed
        def borrow(self):
            self.isBorrowed = True
        
        # sets book as not borrowed
        def giveBack(self):
            self.isBorrowed = False

        # gets title
        def getTitle(self):
            return self.title

        # gets number
        def getNumber(self):
            return self.number

        # gets is borrowed
        def getBorrowed(self):
            return self.isBorrowed
        
        # gets is borrowed
        def getCategory(self):
            return self.category


    class Reader:

        # initialization
        def __init__(self, name = None, surname = None, age = None, number = 0, books = None):
            self.name = name
            self.surname = surname
            self.age = age
            self.number = number
            self.books = books     

        # print info about reader
        def printInfo(self):
            print(f"{self.number}. {self.name} {self.surname}, age: {self.age}")
            return self.books

        # user has borrowed this book
        def borrow(self, number):
            self.books.append(number)

        # user is giving back this bok
        def giveBack(self, number):
            try:
                index = self.books.index(number)
                self.books.pop(index)
            except:
                print("Reader does not have this book")
                return -1

        # gets surname
        def getSurname(self):
            return self.surname

        # gets number
        def getNumber(self):
            return self.number


# options for menu
def menuOption(option, branch):
    if option == '0':
        print("Exiting...")
        quit()
    elif option == '1':
        branch.borrowBook()
    elif option == '2':
        branch.giveBackBook()
    elif option == '3':
        branch.addBook()
    elif option == '4':
        branch.addReader()
    elif option == '5':
        file = input("Enter file name: ")
        branch.addManyBooks(file)
    elif option == '6':
        file = input("Enter file name: ")
        branch.addManyReaders(file)
    elif option == '7':
        branch.printAllBooks()
    elif option == '8':
        branch.printAllReaders()
    elif option == '9':
        branch.bookInfo()
    elif option == '10':
        branch.readerInfo()
    elif option == '11':
        branch.borrowBookNumber()
    elif option == '12':
        branch.giveBackBookNumber()
    elif option == '13':
        branch.bookInfoNumber()
    elif option == '14':
        branch.readerInfoNumber()
    elif option == '15':
        branch.allBooksInCategory()
    else:
        print("Wrong option...")

#info about menu
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
    print("11. Borrow book by number")
    print("12. Give back book by number")
    print("13. Book info by number")
    print("14. Reader info by number")
    print("15. All books in category")
    print("0. Exit")


# main
print("\n\n")
filia1 = Library('Filia', 'Wrocław', 1)
filia1.loadBooks("books.txt")
filia1.loadReaders("readers.txt")
filia1.printInfo()

while 1:
    print("\n")
    menuInfo()
    userInput = input("\nEnter menu option: ")
    menuOption(userInput, filia1)

