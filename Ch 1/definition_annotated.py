# Python Object Oriented Programming by Joe Marini course example


# This file demonstrates basic class definitions


# create a basic class
class Toy():
    # the parenthesis is optional, needed if there's any inheritance going on

    # this is a legit function with only a pass keyword, just not doing anything 
    pass

class Book():
    def __init__(self, title):
        """This is the initializer function that will be called first ipon the creation of an object of this class
        
        @param: self: the first argument of a classss function, is a tradition (can use other words) name, and it refers to the object itself
        @param title: an attribute of the object that should be initialized  """

        self.title = title


# create instances of the class
b1 = Book("Harry Potter")


# print the class and property
print(b1)
print(b1.title)