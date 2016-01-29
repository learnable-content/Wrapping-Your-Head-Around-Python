customer1 = "John Doe"
pickupLocation1 = "350 5th Ave"
package1 = customer1 + pickupLocation1

customer2 = "Jane Doe"
pickupLocation2 = "100 7th Ave"
package2 = customer2 + pickupLocation2

customer3 = "Joe Danields"
pickupLocation3 = "11 1st Ave"
package3 = customer3 + pickupLocation3

#2.4

packages = [package1, package2, package3]

index = 0
while (index < len(packages)):
    print(packages[index])
    index = index + 1
else:
    print("no customers to print. index=" + str(index))