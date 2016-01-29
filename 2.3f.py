customer1 = "John Doe"
pickupLocation1 = "350 5th Ave"
package1 = customer1 + pickupLocation1

customer2 = "Jane Doe"
pickupLocation2 = "100 7th Ave"
package2 = customer2 + pickupLocation2

customer3 = "Joe Daniels"
pickupLocation3 = "11 1st Ave"
package4 = customer3 + pickupLocation3

#2.3f

#create a list of customers

customerList = [customer1, customer2, customer3]
print(customerList[1])

customer4 = "Jason, Bourne"
pickupLocation4 = "333 Lexington Ave"
package4 = customer4 + pickupLocation4

customerList.append(customer4)
print(len(customerList))
customerList.remove(customer4)
print(len(customerList))
customerList[0] = "John Doe II"
print(customerList[0])
print(customer1)

addressList = {customer1:pickupLocation1, customer2:pickupLocation2, customer3:pickupLocation3}
print(len(addressList))
print(addressList[customer2])