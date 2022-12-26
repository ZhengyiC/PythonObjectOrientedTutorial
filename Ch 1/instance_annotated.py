# Python Object Oriented Programming by Joe Marini course example

# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):

        # all of the below variables are called instance attributes because they are specific to each instance created
        # add properties
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price 
        self.__secret = "this is a secret"

    # create instance methods

    def getPrice(self):

        #test if there's discount set 
        if hasattr(self, "_discount"):
            return self.price - self.price*self._discount
        else:
            return self.price

    

    def setDiscount(self, amount):
        #the underscore at the start of the attribute name indicates that this should be an variable only accessed within class, should not be called else where, but this is not an enforcement 
        self._discount = amount

    def getSecret(self):
        print(self.__secret)


# create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 29.95)
#b2 = Book("The Catcher in the Rye")

# print the price of book1
print(f"before set discount, price: {b1.getPrice()}")
b1.setDiscount(0.2)
print(f"after set 20% discount, price: {b1.getPrice()}")



# properties with double underscores are hidden by the interpreter

# double underscore variables can be called within a class function 
b1.getSecret()

# they cannot be called outside a class function, the below line will result in an no-attribute err
#print(b1.__secret)

print(b1.price) #this can work because price is not with double underscore 

# this is because python automatically concatenate a class name before the variable name 
print(b1._Book__secret)
