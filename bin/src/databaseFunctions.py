import pyodbc
server = 'surfinder.database.windows.net'
database = 'SURFinder'
username = 'SLVadmin'
password = 'SLVapathy!'
driver= '{ODBC Driver 13 for SQL Server}'

# Phone number: char(12)
# Name: varchar(25)
# Keywords 1, 2, 3: varchar(25)
#

# Connects to the SQL database
def connectToDatabase():
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	return cnxn

########################################################################

# Person Table Accessors 

# Gets all the phone numbers listed in the database.
def getAllPhones():
	cnxn = connectToDatabase()
	crsr = cnxn.cursor()

	numbers = []

	sqlCmd = """SELECT phoneNumber FROM people;"""
	crsr = crsr.execute(sqlCmd)
	row = crsr.fetchone()
	while (row):
		numbers.append(row.phoneNumber)
		row = crsr.fetchone()
	
	cnxn.close()

	return numbers
	

# Gets the name associated with a phone number.
def getName(phone):
	cnxn = connectToDatabase()
	crsr = cnxn.cursor()
	

	sqlCmd = """SELECT name FROM people WHERE phoneNumber=?;"""
	crsr.execute(sqlCmd, phone)
	name = crsr.fetchone().name
	
	cnxn.close()

	return name

def getAllKeywords(phone):
	cnxn = connectToDatabase()
	crsr = cnxn.cursor()
	

	keywords = []
	keywords.append(getKeyword1(phone))
	keywords.append(getKeyword2(phone))
	keywords.append(getKeyword3(phone))

	return keywords

# Gets the first keyword associated with a phone number.
def getKeyword1(phone):
	cnxn = connectToDatabase()
	crsr = cnxn.cursor()

	sqlCmd = """SELECT keyword1 FROM people WHERE phoneNumber=?;"""
	crsr.execute(sqlCmd, phone)
	kw = crsr.fetchone().keyword1

	cnxn.close()

	return kw

# Gets the second keyword associated with a phone number.
def getKeyword2(phone):
	cnxn = connectToDatabase()
	crsr = cnxn.cursor()

	sqlCmd = """SELECT keyword2 FROM people WHERE phoneNumber=?;"""
	crsr.execute(sqlCmd, phone)
	kw = crsr.fetchone().keyword2
	
	cnxn.close()

	return kw

# Gets the third keyword associated with a phone number.
def getKeyword3(phone):
	cnxn = connectToDatabase()
	crsr = cnxn.cursor()

	sqlCmd = """SELECT keyword3 FROM people WHERE phoneNumber=?;"""
	crsr.execute(sqlCmd, phone)
	kw = crsr.fetchone().keyword3
	
	cnxn.close()

	return kw

# Checks whether a given person (identified by phone number) has new 
# opportunities listed. Returns a boolean.
def isNewInfo(phone):
	cnxn = connectToDatabase()
	crsr = cnxn.cursor()

	sqlCmd = """SELECT newOpps FROM people WHERE phoneNumber=?;"""
	crsr.execute(sqlCmd, phone)
	isNew = crsr.fetchone().newOpps

	cnxn.close()

	return (isNew == "t")


# Person Table Modifiers

# Adds a person to the table.
def newPerson(phoneNum, pname, kw1, kw2, kw3):
	cnxn = connectToDatabase()
	crsr = cnxn.cursor()
	
	#if (getName(phoneNum) =)
	sqlCommand = """INSERT INTO people(phoneNumber, name, keyword1, 
	keyword2, keyword3, newOpps)
	VALUES(?, ?, ?, ?, ?, ?);"""

	crsr.execute(sqlCommand, (phoneNum, pname, kw1, kw2, kw3, "f"))

	cnxn.commit()
	cnxn.close()

# Deletes someone from the table.
def deletePerson(phoneNum):
	cnxn = connectToDatabase()
	crsr = cnxn.cursor()

	sqlCommand = """DELETE FROM people WHERE phoneNumber=?;"""
	crsr.execute(sqlCommand, phoneNum)


	cnxn.commit()
	cnxn.close()

def hasUnread(phoneNum, crsr):
	sqlCmd = """UPDATE people SET newOpps="t" WHERE phoneNumber=?);"""
	crsr.execute(sqlCmd, phoneNum)
	return crsr


######################################################################

# Opportunity Table Accessors

# Gets new opportunities for a certain phone number. Returns array of title 
# strings, sets opportunites to read.
def getNewOpportunites(phone):
	cnxn = connectToDatabase()
	crsr = cnxn.cursor()

	ids = []

	sqlCmd = """SELECT oppID FROM opportunities WHERE phone=?, isRead="f";"""
	crsr = crsr.execute(sqlCmd, oppID)
	row = crsr.fetchone()
	while (row):
		titles.append(row.oppID)
		row = crsr.fetchone()
	sqlCmd = """UPDATE opportunities SET isRead="t" WHERE phone=?;"""
	crsr.execute(sqlCmd, oppID)

	cnxn.close()

	return ids

# Gets the URL of a specific opportunity.
def getOppURL(oppID):
	cnxn = connectToDatabase()
	crsr = cnxn.cursor()
	

	sqlCmd = """SELECT oppURL FROM opportunities WHERE oppID=?;"""
	crsr.execute(sqlCmd, oppID)
	oURL = crsr.fetchone().oppURL
	
	cnxn.close()

	return oURL

# Gets the professor's name for a specific opportunity.
def getOppProfName(oppID):
	cnxn = connectToDatabase()
	crsr = cnxn.cursor()
	

	sqlCmd = """SELECT profName FROM opportunities WHERE oppID=?;"""
	crsr.execute(sqlCmd, oppID)
	name = crsr.fetchone().profName
	
	cnxn.close()

	return name

# Gets the professor's email for a specific opportunity.
def getOppProfEmail(oppID):
	cnxn = connectToDatabase()
	crsr = cnxn.cursor()

	sqlCmd = """SELECT profEmail FROM opportunities WHERE oppID=?;"""
	crsr.execute(sqlCmd, oppID)
	email = crsr.fetchone().profEmail
	
	cnxn.close()

	return email

# Gets the person's phone number for a specific opportunity.
def getOppPhone(oppID):
	cnxn = connectToDatabase()
	crsr = cnxn.cursor()
	
	sqlCmd = """SELECT phoneNumber FROM opportunities WHERE oppID=?;"""
	crsr.execute(sqlCmd, oppID)
	number = crsr.fetchone().phoneNumber
	
	cnxn.close()

	return number

# Gets the trigger keyword for a specific opportunity.
def getOppKeyword(oppID):
	cnxn = connectToDatabase()
	crsr = cnxn.cursor()
	
	sqlCmd = """SELECT triggerKeyword FROM opportunities WHERE oppID=?;"""
	crsr.execute(sqlCmd, oppID)
	keyword = crsr.fetchone().triggerKeyword
	
	cnxn.close()

	return keyword



# Opportunity Table Modifiers

# Takes values and makes a new entry in the table of operations.
def newOpp(oppTitle, oppURL, phoneNumber, profName, profEmail,
	triggerKeyword):
	cnxn = connectToDatabase()
	crsr = cnxn.cursor()
	
	sqlCommand = """INSERT INTO opportunities(oppTitle, oppURL, phoneNumber,
	profName, profEmail, triggerKeyword, isRead)
	VALUES(?, ?, ?, ?, ?, ?, ?);"""

	crsr.execute(sqlCommand, (oppTitle, oppURL, phoneNumber, profName,
		profEmail, triggerKeyword, "f"))
	crsr = hasUnread(phoneNumber, crsr)

	cnxn.commit()
	cnxn.close()

def deleteOpp(oppID):
	cnxn = connectToDatabase()
	crsr = cnxn.cursor()

	sqlCommand = """DELETE FROM opportunities WHERE oppID=?"""
	crsr.execute(sqlCommand, oppID)


	cnxn.commit()
	cnxn.close()