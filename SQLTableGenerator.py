#Jeremy Banks ~ SQL Table Generator
#Started: February 19, 2018
#Finished: ?

#**********
#*  Main  *
#**********

entryDict = {}
tableName = raw_input("Enter the name of your table: ")
fieldNumber = input("Enter the number of fields you wish your table to have: ")
print ""

for i in range(0,fieldNumber):
	catList = [None]*4
	name = raw_input("Name of field?: ")
	catList[0] = name
	fieldType = raw_input("Field type?: ")
	catList[1] = fieldType
	fieldSize = raw_input("Field size?: ")
	catList[2] = fieldSize
	isNull = raw_input("Can it be null?: ")
	catList[3] = isNull	
	entryDict[i] = catList

outputFile = "NewTable-" + tableName + ".sql"
filePtr = open(outputFile,"w+")
string = ''.join(["CREATE TABLE ",tableName,"("])
filePtr.write(string)
for j in range(0,fieldNumber):
	if j > 0:
		filePtr.write(",")
	arr = entryDict[j]
	string = ''.join([arr[0]," ", arr[1], "(", arr[2],") ", arr[3]])
	filePtr.write(string)
filePtr.write(");")
filePtr.close()
