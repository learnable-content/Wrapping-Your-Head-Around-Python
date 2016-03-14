fileOutput = open('/users/brettromero/test/file_io.txt', 'wt')
fileOutput.write('John Doe;\n350 5th Ave\n|\nJane Doe;\n100 7th Ave\n|\nJoe Daniels;\n11 1st Ave\n')
fileOutput.close()

fileInput = open('/users/brettromero/test/file_io.txt', 'rt')
fileInput.read()
file.close()
