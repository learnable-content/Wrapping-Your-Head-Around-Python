customer1 = "John Doe"
pickupLocation1 = "350 5th Ave"
package1 = customer1 + pickupLocation1

customer2 = "Jane Doe"
pickupLocation2 = "100 7th Ave"
package2 = customer2 + pickupLocation2

customer3 = "Joe Daniels"
pickupLocation3 = "11 1st Ave"
package4 = customer3 + pickupLocation3

customerList = [customer1, customer2, customer3]

#start 3.3f

#class Customer:
#    name = ""
#    pickupLocation = ""
#    
#    def getPackage(self):
#        return self.name + ", " + self.pickupLocation
    
#cus1 = Customer()
#cus1.name = "Joe Blow"
#print(cus1.name)
#print(cus1.getPackage())

        
class Person:
    firstName = ""
    lastName = ""
    streetAddress = ""
    city = ""
    state = ""
    zipcode = ""
    
    def __init__(self, fname, lname, streetAddress, city, state, zipcode):
        self.firstName = fname 
        self.lastName = lname
        self.streetAddress = streetAddress 
        self.city = city 
        self.state = state 
        self.zipcode = zipcode
    
    def printName(self):
        print("First name is %s" % (self.firstName))
        
p1 = Person("Jim", "Jones", "100 1st street", "Newport Beach", "CA", "92661")
p1.printName()

#this is switch to go after Person. But Customer class is defined first in course.
class Customer (Person):
    name = ""
    pickupLocation = ""
    
    def __init__(self, name, pickupLocation, custId):
        self.name = name
        self.pickupLocation = pickupLocation
        self.__customerId = custId
        return
        
    #def getPackage(self):
     #   return self.name + ", " + self.pickupLocation
        
    def getPackage(self, delimeter):
        return "%s %s %s. Customer ID = %d" % (self.name, delimeter,self.pickupLocation, self.__customerId)
    
    #overrides
    #def printName(self):
     #   print("Name is %s" % (self.name))
     
    #hide data member
    __customerId = 0
        
cus1 = Customer("Joe Blow", "350 5th Ave", 20)
#init required
#cus1 = Customer()
cus1.name = "Joe Blow"
cus1.pickupLocation = "350 5th Ave"
#print(cus1.getPackage())
print(cus1.getPackage(":"))

#overriding
cus1.printName()



        