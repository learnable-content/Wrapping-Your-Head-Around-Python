customer1 = "John Doe"
pickupLocation1 = "350 5th Ave"
package1 = customer1 + ":" +  pickupLocation1

customer2 = "Jane Doe"
pickupLocation2 = "100 7th Ave"
package2 = customer2 + ":" +   pickupLocation2

customer3 = "Joe Danields"
pickupLocation3 = "11 1st Ave"
package = customer3 + ":" +   pickupLocation3

packages2 = {customer1:pickupLocation1,customer2:pickupLocation2,customer3:pickupLocation3}

#2.8f

a,b = package1.split(":", 1)
print(a)
#John Doe
print(b)
#350 5th Ave
tuplePackage = package1.split(":", 1)
print(tuplePackage[0])
#John Doe

#dictionary
for (k,v) in packages2.items():
    print(k + " address=" + v)
#output
#John Doe address=350 5th Ave
#Jane Doe address=100 7th Ave
#Joe Danields address=11 1st Ave
    
numbers = (1,)
print(numbers[0])
# 1
numbers = ("1st street", "2nd street", "3rd street", "4th street")
print(numbers[1:4])

test = (1,2,3,4,5)
print(test[1:3])

#reassignment error
#test[0] = 22
test = (22, 33, 44, 55, 66)
print(test[0])
