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

#start 3.2f

def calculateFee(miles):
    result = miles * .5 + 2.50
    return result
    
print (calculateFee(10))

add = lambda n1, n2: n1 + n2
print(add(1,3))

calculateFee2 = lambda miles: miles * .5 + 2.5
print(calculateFee2(10))

def calculateFee3(miles):
    resultTemplate = lambda miles: miles * .5 + 2.5
    return resultTemplate(miles)
    
print(calculateFee3(10))