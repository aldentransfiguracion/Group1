# Kimberly Hunter, Alden Transfiguracion, Baylor Jeppsen, Allison Korth, Levi, Pablo Pineda
# Description: Write hamburger program that tracks how many hamburgers each customer eats

# import library
import random

# Create Order Class that contains a random number of burgers
class Order() :
    def __init__(self) :
        self.burger_count = self.randomBurgers()
    def randomBurgers(self) :
        # number between 1 and 20 : randomint is inclusive
        return random.randint(1, 20)
    
# Create a person class that assigns one of the 9 names in list randomly as customer
class Person() :
    def __init__(self) :
        self.customer_name = self.randomName()
    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", 
        "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)
    
# Create Customer Class that inherits from person class
class Customer(Person) :
    def __init__(self) :
        super().__init__()
        self.order = Order()

# Create variable for Queue and assign items of type "Customer"
# Represents customers in line
queueCustomers = []

# Create variable for Dictionary keys=string value=type int
dictCustInfo = {}
asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", 
"Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
for iCount in range(0, len(asCustomers)) :
    customer_name = asCustomers[0]
    total_burgers = 0
    dictCustInfo[customer_name] = total_burgers
    asCustomers.pop(0)

# Put 100 customers in the queue
iCustomers = 100
for iCount in range(1, iCustomers+1) :
    oCust = Customer()
    queueCustomers.append(oCust)  # [ Customer object ]
    if oCust.customer_name in dictCustInfo :
        dictCustInfo[oCust.customer_name] += oCust.order.burger_count
    queueCustomers.pop(0)

# Sort Customer List Totals in dictionary most ordered first
listSortedCustomers = sorted(dictCustInfo.items(), key=lambda x: x[1], reverse=True)

# Print Names(key) and Totals(value) in dict
for iCount in range(0, len(listSortedCustomers)) :
    customer = listSortedCustomers[0]
    print("\n", customer[0].ljust(19), "\t", customer[1])
    listSortedCustomers.pop(0)