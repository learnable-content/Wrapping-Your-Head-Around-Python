fileContent = 'John Doe;\n350 5th Ave\n|\nJane Doe;\n100 7th Ave\n|\nJoe Daniels;\n11 1st Ave\n'

packages = {}

newStr = fileContent.split("|", 3)
print(newStr)
i = 0
for s in newStr:
    (a,b) = newStr[i].replace("\n", "").split(";", 1)
    print(a + " == " + b)
    packages[a] = b
    i = i + 1
    
print(packages)