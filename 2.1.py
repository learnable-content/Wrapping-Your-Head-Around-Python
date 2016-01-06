>>> customer = "John Doe"
>>> pickupLocation = "350 5th Ave"
>>> package = customer + pickupLocation
>>> print(package)
John Doe350 5th Ave
>>> 
package = customer + "@" + pickupLocation
>>> print(package)
John Doe@350 5th Ave
>>> fare = 15
>>> tip = 2
>>> totalFare = fare + tip
>>> print(totalFare)
17
>>> print(package + " with total of " + totalFare)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(package + " with total of " + totalFare)
TypeError: Can't convert 'int' object to str implicitly
>>> 
>>> print(package + " with total of " + str(totalFare))
John Doe@350 5th Ave with total of 17
>>> fare + "2"
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    fare + "2"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> fare + int("2")
17
>>> 
