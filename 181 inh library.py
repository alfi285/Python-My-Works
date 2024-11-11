#1-Create a LibraryItem class with the following properties:
from time import perf_counter


# title (e.g., "The Great Gatsby")
# author (e.g., "F. Scott Fitzgerald")
# year_published (e.g., 1925)
# Add an _init_ method to initialize these properties.

class LibrarySystem:
    def __init__(self,title,author,year_published):
        self.title = title
        self.author = author
        self.year = year_published


#2-Add a display_info method to the LibraryItem class
# that prints the item’s details in this format:

#Title: The Great Gatsby, Author: F. Scott Fitzgerald, Year Published: 1925

    def display_info(self):
         return f"Title:{self.title},Author:{self.author},Year:{self.year}"

#3-Create a Book class that inherits from LibraryItem and has:

class Book(LibrarySystem):

#An additional property called genre (e.g., "Fiction").
#Modify the _init_ method in the Book class
# to accept a genre argument in addition
# to the inherited properties (title, author, and year_published).

    def __init__(self, title, author, year_published,genre):
        super().__init__(title, author, year_published)
        self.genre = genre

#4-Add a display_info method to the Book class that overrides
# the LibraryItem class’s method.
# It should display the book’s details, including genre, in this format:

    def display_info(self):
        return f"Title:{self.title},Author:{self.author},Year:{self.year},Genre:{self.genre}"


    def borrow_item(self):
        is_available = True
        print("Item borrowed successfully.") if is_available == True else print("Item is already borrowed.")

#Book Info: The Great Gatsby, Author: F. Scott Fitzgerald,
# Year Published: 1925, Genre: Fiction



#5-Create a DVD class that also inherits from LibraryItem and has:

#An additional property called duration (in minutes, e.g., 142).
#Modify the _init_ method in the DVD class to accept
# a duration argument in addition to the
# inherited properties (title, author, and year_published).

class dvd(LibrarySystem):
    def __init__(self,title, author, year_published,minutes):
        super().__init__(title, author, year_published)
        self.minutes = minutes

#6-Add a display_info method to the DVD class that overrides
# the LibraryItem class’s method. It should display
# the DVD’s details, including duration, in this format:
    def display_info(self):
        return f"DVD info:{self.title},Director:{self.author},Year:{self.year},Duration{self.minutes}"
#DVD Info: Inception, Director: Christopher Nolan,
# Year Published: 2010, Duration: 142 minutes

    def borrow_item(self):
        is_available = False
        print("Item borrowed successfully.") if is_available == True else print("Item is already borrowed.")



#7-Add a borrow_item method to both Book and DVD classes that:

#Checks if the item is available
# (assume each item has a boolean property is_available initialized to True).
#If available, sets is_available to False and displays a message
# like "Item borrowed successfully."
#If not available, displays "Item is already borrowed."



#8-Write code to:

#Create an object of the Book class with
# title "The Great Gatsby," author "F. Scott Fitzgerald,
# " year published 1925, and genre "Fiction."

#Create an object of the DVD class with title "Inception,
# " director "Christopher Nolan," year published 2010, and
# duration of 142 minutes.

book1 = Book("The Great Gatsby","F.Scott Fitzger",1925,"Fiction")
print(book1.display_info())

d1 = dvd("Inception","Christopher Nolan",2010,142)
print(d1.display_info())

#Call display_info for both objects.

#Call borrow_item for each object twice to verify
# that the availability check works correctly.
book1.borrow_item()
d1.borrow_item()
book1.borrow_item()
d1.borrow_item()


#Expected Output:
# Book Info: The Great Gatsby, Author: F. Scott Fitzgerald,
# Year Published: 1925, Genre: Fiction

# DVD Info: Inception, Director: Christopher Nolan,
# Year Published: 2010, Duration: 142 minutes

# Item borrowed successfully.

# Item is already borrowed.

# Item borrowed successfully.

# Item is already borrowed.