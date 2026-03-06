# Creating Class Named Library

Class Library:
    def __init__(self, name=="", author=""):
       self.name = name
       self.author = author
       self.available = True

    def show_details(self):
        print("\n--- Book Details ---") 
        print("Name        :",self.name if self.name else "Not given")
        print("Author      :",self.author if self.author else "Not given")
        print("Availability   :," "Yes" if self.available else "No")

    def checkout(self):
       if self.available:
           self.available = False
           print("\nYour book has been checked out successfully")
       else:
           print("\nSorry, The mentioned book is not available!!")


# Printing the availability of book
print("1.Enter Book Name")
print("2.Enter Author Name")

choice = input("Choose option (1 or 2): ")

if choice =="1":
    name = input("Enter Name of the book:")
    book = Library(name=name)
elif choice =="2":
    author = input("Enter Name of the author:")
    book = Library(author=author)
else:
    print("Your choice is incorrect")
    exit()

# Creating an object to display output

book.show_details()
book.checkout()
book.show_details()

