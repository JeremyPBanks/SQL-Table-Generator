#Jeremy Banks ~ SQL Table Generator
#Started: February 19, 2018
#Finished: ?

class TableEntry:
	def __init__(self,name,fieldType,fieldSize,isNull,isUnique):
		self.name = name
		self.type = fieldType.upper()
		self.size = fieldSize
		self.null = isNull
		self.unique = isUnique
		self.entries = []

	def toString(self):
		if self.type != "INT":
			return ''.join([self.name," ",self.type, "(",self.size,") ", self.null])
		else:
			return ''.join([self.name," ",self.type," ",self.null])

	def parse(self,fileName):
		newFilePtr = (fileName,"r")


#**********
#*  Main  *
#**********

entryDict = {}
primaryKey = ""
tableName = raw_input("Enter the name of your table: ")
fieldNumber = input("Enter the number of fields you wish your table to have: ")
print ""

for i in range(0,fieldNumber):
	name = raw_input("Name of field?: ")
	fieldType = raw_input("Field type?: ")
	fieldSize = raw_input("Field size?: ")
	isNull = raw_input("Can it be null?[yes/no]: ")
	if isNull == "yes":
		isNull = "NOT NULL"
	isPrimary = raw_input("Is this the primary key?: ")
	if isPrimary == "yes":
		primaryKey = name
	fieldObj = TableEntry(name,fieldType,fieldSize,isNull,isPrimary)
	myFile = raw_input("Enter the file you want to parse: ")
	entryDict[i] = fieldObj

outputFile = "NewTable-" + tableName + ".sql"
filePtr = open(outputFile,"w+")
string = ''.join(["CREATE TABLE ",tableName,"("])
filePtr.write(string)
for j in range(0,fieldNumber):
	if j > 0:
		filePtr.write(",")
	thisObj = entryDict[j]
	string = thisObj.toString()
	filePtr.write(string)
if primaryKey != "":
	tempStr = ''.join([",PRIMARY KEY(",primaryKey,")"])
	filePtr.write(tempStr)
filePtr.write(");\n")

#fieldNumber = input("How many tuples would you like?: ")

filePtr.close()
