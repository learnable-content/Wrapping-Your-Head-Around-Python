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

#start 3.4f 

#global but used in function
#chargePerMile = .5

def calculateFee(miles):
    result = miles * .5 + 2.50
    return result
    
#result is out of scope here
#print(result)
 
#customerList is global
#print(customerList)
    
print (calculateFee(10))

add = lambda n1, n2: n1 + n2
print(add(1,3))
#lambda variables are out of scope here
#print(n1)

calculateFee2 = lambda miles: miles * .5 + 2.5
print(calculateFee2(10))

def calculateFee3(miles):
    resultTemplate = lambda miles: miles * .5 + 2.5
    return resultTemplate(miles)
    
print(calculateFee3(10))

#global variable affected by function
myint = 10
myint2 = 9
print("myint %d" % (myint))
def changeGlobal():
    #instance variable disappears after function execution
    myint = 20
    #global variable
    global myint2
    myint2 = 15
    print("myint inside func %d" % (myint))
    return

changeGlobal()
print("myint after func call %d" % (myint))
print("myint2 after func call %d" % (myint2))


    