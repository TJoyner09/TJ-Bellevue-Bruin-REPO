import os

filePath = input('Enter file path: ')
fileName = input('Enter file name: ')
if not os.path.exists(filePath):
  os.makedirs(filePath)
completeName = os.path.join(filePath, fileName + ".csv")         

fileObj = open(completeName, "w")
name = input('Enter name: ')
address = input('Enter address: ')
phone = input('Enter phone number: ')
fileObj.write(name+','+address+','+phone+'\n')
fileObj.close()

fileObj = open(completeName, "r")
print(fileObj.read())