customer = "John Doe"
pickupLocation = "350 5th Ave"
package1 = customer + pickupLocation

#if "350 5th Ave" in package1:
 #   print("Customer Found")
    
#what if there are several customers
customer2 = "Jane Doe"
pickupLocation2 = "100 7th Ave"
package2 = customer2 + pickupLocation2

customer3 = "Joe Danields"
pickupLocation3 = "11 1st Ave"
package = customer3 + pickupLocation3

if "350 5th Ave" in package:
    print("Customer 1 Found")
elif "100 7th Ave" in package:
    print("Customer 2 Found")
else:
    print("Customer 3 Found")
   
#what if we want to find ranges of street numbers on the same street
#emphasis on ordering for this example.  Will start with 100, 200, 300 first.
streetNumber = 1


if streetNumber >= 0 and streetNumber < 200:
    print("Customer found in 100 to 200 block")
elif streetNumber >= 200 and streetNumber < 300:
    print("Customer found in 200 block")
elif streetNumber >= 300 and streetNumber < 400:
    print("Customer found in 300 block")
else: 
    print("Customer found in 400 and above block")
    