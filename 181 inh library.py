#1-Create a LibraryItem class with the following properties:

# title (e.g., "The Great Gatsby")
# author (e.g., "F. Scott Fitzgerald")
# year_published (e.g., 1925)
# Add an _init_ method to initialize these properties.


#2-Add a display_info method to the LibraryItem class
# that prints the item’s details in this format:

#Title: The Great Gatsby, Author: F. Scott Fitzgerald, Year Published: 1925



#3-Create a Book class that inherits from LibraryItem and has:

#An additional property called genre (e.g., "Fiction").
#Modify the _init_ method in the Book class
# to accept a genre argument in addition
# to the inherited properties (title, author, and year_published).



#4-Add a display_info method to the Book class that overrides
# the LibraryItem class’s method.
# It should display the book’s details, including genre, in this format:

#Book Info: The Great Gatsby, Author: F. Scott Fitzgerald,
# Year Published: 1925, Genre: Fiction



#5-Create a DVD class that also inherits from LibraryItem and has:

#An additional property called duration (in minutes, e.g., 142).
#Modify the _init_ method in the DVD class to accept
# a duration argument in addition to the
# inherited properties (title, author, and year_published).



#6-Add a display_info method to the DVD class that overrides
# the LibraryItem class’s method. It should display
# the DVD’s details, including duration, in this format:

#DVD Info: Inception, Director: Christopher Nolan,
# Year Published: 2010, Duration: 142 minutes



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

#Call display_info for both objects.

#Call borrow_item for each object twice to verify
# that the availability check works correctly.



#Expected Output:
# Book Info: The Great Gatsby, Author: F. Scott Fitzgerald,
# Year Published: 1925, Genre: Fiction

# DVD Info: Inception, Director: Christopher Nolan,
# Year Published: 2010, Duration: 142 minutes

# Item borrowed successfully.

# Item is already borrowed.

# Item borrowed successfully.

# Item is already borrowed.