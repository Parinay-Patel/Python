                                                     #LIBRARY MANAGEMENT SYSTEM (LMS)

class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books Present in this library are : ")
        for book in self.books:
            print(f"\t\t -> {book}")

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You Have an issued {bookName} . \nPlease keet it safe and return it within 7 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry!!! This Book isn't available right now.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this Book.")

    def donateBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for Donate this Book.")
class Student:
    def requestBook(self):
        self.book  = input("Enter the name of the Book you want to borrow : ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of book you want to return : ")
        days = int(input("Enter how many days  this book late:"))
        if days>0:
            print(f"Fine : {days*5}")
        return self.book

    def donateBook(self):
        self.book = input("Enter the name of book you want to donate : ")
        return self.book

if __name__=="__main__":
    centralLibrary  = Library(['R.D. Sharma Class 9th', 'R.D. Sharma Class 10th', 'R.D. Sharma Class 11th', 'R.D. Sharma Class 12th', 
                              'Hindi 9th', 'English 9th', 'Physics 9th', 'History 9th', 'Geography 9th', 'Economics 9th', 'Biology 9th', 'Chemistry 9th', 
                              'Hindi 10th', 'English 10th', 'Physics 10th', 'History 10th', 'Geography 10th', 'Economics 10th', 'Biology 10th', 'Chemistry 10th',
                              'Hindi 11th', 'English 11th', 'Physics 11th', 'History 11th', 'Geography 11th', 'Economics 11th', 'Biology 11th', 'Chemistry 11th',
                              'Hindi 12th', 'English 12th', 'Physics 12th', 'History 12th', 'Geography 12th', 'Economics 12th', 'Biology 12th', 'Chemistry 12th'])
    student = Student()

    while(True):
        print("----------------------------------------------------------------------------")
        print("------------------  Welcome to Parinay's Library  -------------------------")
        print("----------------------------------------------------------------------------")
        print("1. Display Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Donate a Book")
        print("5. Exit")
        print("---------------------------------------------------------------------------")
        a = int(input("Enter a Choice : "))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            centralLibrary.donateBook(student.donateBook())
        elif a==5:
            print("Thanks for using Parinay's Library.......")
            exit()  
