customer1 = "John Doe"
pickupLocation1 = "350 5th Ave"
package1 = customer1 + pickupLocation1

customer2 = "Jane Doe"
pickupLocation2 = "100 7th Ave"
package2 = customer2 + pickupLocation2

customer3 = "Joe Danields"
pickupLocation3 = "11 1st Ave"
package3 = customer3 + pickupLocation3

packages = [package1, package2, package3]
packages2 = {customer1:pickupLocation1,customer2:pickupLocation2,customer3:pickupLocation3}

#2.5

#list
for p in packages:
    print(p)

#dictionary
for k,v in packages2.items():
    print(k + " address=" + v)
    
for k in packages2.keys():
    print(k)
    
for v in packages2.values():
    print(v)