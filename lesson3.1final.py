result = 1 + 3
print(result)

def add(n1, n2):
    result = (n1 + n2)
    return result
    
add(1,3)

myfuncresult = lambda n1, n2: n1 + n2
print(myfuncresult(1,3))

myfunc2result = map(lambda x: x*2, [1,4,20])
print(list(myfunc2result))

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

def calculateFee(miles):
    result = miles * .5 + 2.50
    return result

print(calculateFee(10))

def calculateFee(miles, initialRate = 2.50):
    result = miles * .5 + initialRate
    return result
    
print(calculateFee(10, 3))

def caculateMultiCustomerRate(*miles):
    rates = []
    for m in miles:
        rates.append(m * 2.50)
    return rates
    
rates = caculateMultiCustomerRate(10,20,30)
i = 1
for r in rates:
    print("customer %d = $%d" % (i, r))
    i = i + 1
    
    