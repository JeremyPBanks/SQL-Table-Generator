#Jeremy Banks ~ SQL Table Generator
#Started: February 19, 2018
#Finished: ?

class TableEntry:
	def __init__(self,name,fieldType,fieldSize,isNull,isUnique,isPrimary):
		self.name = name
		self.type = fieldType.upper()
		self.size = fieldSize
		self.null = isNull
		self.unique = isUnique
		self.isPrimary = isPrimary
		self.entries = []

	def toString(self):
		if self.type != "INT":
			return ''.join([self.name," ",self.type, "(",str(self.size),") ", self.null])
		else:
			return ''.join([self.name," ",self.type," ",self.null])

	def parse(self,fileName):
		with open(fileName) as newFilePtr:
    			self.entries = newFilePtr.readlines()
		self.entries = [x.strip() for x in self.entries]
		newFilePtr.close()
		

def generate(currObject,index,thisList):
	if currObject.type == "INT":
		myLen = currObject.size
	else:
		myLen = len(currObject.entries)

	for i in range(0,myLen):
		if currObject.type == "INT":
			thisList.append(i)
		else:
			thisList.append(currObject.entries[i])
		
		if (index+1) < fieldNumber:
			
			generate(entryDict[index+1],index+1,thisList)
			intoTheVoid = thisList.pop()
		else:
			if len(thisList) == fieldNumber:
				newList = list(thisList)
				myTuples.append(newList);
			intoTheVoid = thisList.pop()
	return


#**********
#*  Main  *
#**********

entryDict = {}
myTuples = []
primaryKeys = []
tableName = raw_input("Enter the name of your table: ")
fieldNumber = input("Enter the number of fields you wish your table to have: ")
print ""

for i in range(0,fieldNumber):
	name = raw_input("Name of field?: ")
	fieldType = raw_input("Field type?: ")
	if fieldType.upper() != "INT":
		fieldSize = input("Field size?: ")
	else:
		fieldSize = input("Input Max?: ")
	isNull = raw_input("Can it be null?[yes/no]: ")
	if isNull == "no":
		isNull = "NOT NULL"
	else:
		isNull = ""
	if isNull == "NOT NULL":
		isPrimary = raw_input("Is this the primary key?: ")
		if isPrimary != "yes":
			isPrimary = ""
		else:
			primaryKeys.append(name)
	else:
		isPrimary = ""

	fieldObj = TableEntry(name,fieldType,fieldSize,isNull,isPrimary,isPrimary)
	if fieldObj.type != "INT":
		fileName = raw_input("Enter the file you'd like to parse for this: ")
		fieldObj.parse(fileName)
	entryDict[i] = fieldObj
	print "---"

outputFile = "NewTable-" + tableName + ".sql"
filePtr = open(outputFile,"w+")
string = ''.join(["CREATE TABLE ",tableName,"("])
filePtr.write(string)
for j in range(0,fieldNumber):
	if j > 0:
		filePtr.write(", ")
	thisObj = entryDict[j]
	string = thisObj.toString()
	filePtr.write(string)

if primaryKeys is not None:
	keys = ','.join(map(str,primaryKeys))
	tempStr = ''.join([",PRIMARY KEY(",keys,")"])
	filePtr.write(tempStr)
filePtr.write(");\n")

colString = ""

for l in range(0,fieldNumber):
	colString += entryDict[l].name
	if l != (fieldNumber-1):
		colString += ","
	generate(entryDict[l],l,[])

newString = ''.join(["INSERT INTO ", tableName," (",colString,") VALUES "]);
filePtr.write(newString)
myTupleLen = len(myTuples) 
g = 0;
for x in myTuples:
	filePtr.write("(")
	newTuple = ','.join(map(str,x))
	filePtr.write(newTuple)
	g += 1
	if g < myTupleLen:
		filePtr.write("),")
	else:
		filePtr.write(");\n")

filePtr.close()
