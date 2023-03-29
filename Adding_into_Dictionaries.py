#------------Adding into Dictionarys-----------------------------#
#Declaring the Variables
dicRow1 = {'id' : 1, 'name': 'Jane Doe', 'email': 'JaneD@doemail.com'}
dicRow2 = {'id' : 2, 'name': 'Jane Fox', 'email': 'JaneF@foxemail.com'}
dicRow = {}
lstTbl = []
lstTbl.append(dicRow1)
lstTbl.append(dicRow2)

# Process the Data
print('items in the List:')
print('each \'row\':')
for row in lstTbl:
    print(row)
print()
print('assigning directly into the dictionary:')
dicRow['id'] = int(input('Enter an ID:'))
dicRow['name'] = input('Enter the Name: ')
dicRow['email'] = input('Enter the eMail: ')
lstTbl.append(dicRow)

print('assigning to variables first')
strID = input('Enter an ID:')
strName = input('Enter the Name: ')
strMail = input('Enter the eMail:')
intId = int(strID)
dicRow = {'id': intId, 'name': strName, 'email': strMail}
lstTbl.append(dicRow)

#Show the result
print('items in the list now:')
print('each \'row\':')
for row in lstTbl:
    print(row)