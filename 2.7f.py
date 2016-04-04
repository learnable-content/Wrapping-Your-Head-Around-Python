fileContent = 'John Doe;\n350 5th Ave\n|\nJane Doe;\n100 7th Ave\n|\nJoe Daniels;\n11 1st Ave\n'

packages = {}

newStr = fileContent.split("|", 3)
print(newStr)

for s in newStr:
    (a,b) = s.replace("\n", "").split(";", 1)
    print(a + " == " + b)
    packages[a] = b
    
print(packages)
print(packages.keys())
print(packages.values())