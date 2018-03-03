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
def connectToDatabase(server, database, username, password, driver):
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	return cnxn

########################################################################

# Person Table Accessors 

# Gets all the phone numbers listed in the database.
def getAllPhones():
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()
	
	numbers = []


	cnxn.commit()
	cnxn.close()

	return numbers
	

# Gets the name associated with a phone number.
def getName(phone):
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()
	
	numbers = []

	cnxn.commit()
	cnxn.close()

	return name

def getAllKeywords(phone):
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()
	
	keywords = []

	cnxn.commit()
	cnxn.close()

	return keywords

# Gets the first keyword associated with a phone number.
def getKeyword1(phone):
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()

	cnxn.commit()
	cnxn.close()

	return kw

# Gets the second keyword associated with a phone number.
def getKeyword2(phone):
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()

	cnxn.commit()
	cnxn.close()

	return kw

# Gets the third keyword associated with a phone number.
def getKeyword3(phone):
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()

	cnxn.commit()
	cnxn.close()

	return kw

# Checks whether a given person (identified by phone number) has new 
# opportunities listed. Returns a boolean.
def isNewInfo(phone):
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()
	
	

	cnxn.commit()
	cnxn.close()

	return newOpps


# Person Table Modifiers

# Adds a person to the table.
def newPerson(phoneNum, pname, kw1, kw2, kw3):
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()
	
	sqlCommand = """INSERT INTO people 
	(phoneNumber, name, keyword1, keyword2, keyword3, newOpps)
	VALUES(?, ?, ?, ?, ?, "f");"""

	crsr.execute(sqlCommand, phoneNum, pname, kw1, kw2, kw3)

	cnxn.commit()
	cnxn.close()


######################################################################

# Opportunity Table Accessors

# Gets new opportunities for a certain phone number. Returns array of title 
# strings, sets opportunites to read.
def getNewOpportunites(phone):
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()

	titles = []

	cnxn.commit()
	cnxn.close()

	return titles

# Gets the URL of a specific opportunity.
def getOppURL(oppTitle):
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()
	

	cnxn.commit()
	cnxn.close()

	return URL

# Gets the professor's name for a specific opportunity.
def getOppProfName(oppTitle):
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()
	

	cnxn.commit()
	cnxn.close()

	return name

# Gets the professor's email for a specific opportunity.
def getOppProfEmail(oppTitle):
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()

	cnxn.commit()
	cnxn.close()

	return email

# Gets the person's phone number for a specific opportunity.
def getOppPhone(oppTitle):
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()
	
	numbers = []

	cnxn.commit()
	cnxn.close()

	return phoneNum

# Gets the trigger keyword for a specific opportunity.
def getOppKeyword(oppTitle):
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()
	

	cnxn.commit()
	cnxn.close()

	return keyword


# Opportunity Table Modifiers

# Takes a csv file and adds the data to the database, updating the person's
# new info flag in the process. Returns success/failure boolean.
def csvToDatabase(file):
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()
	
	numbers = []

	cnxn.commit()
	cnxn.close()

# Takes values and makes a new entry in the table of operations.
def newOpp(oppTitle, oppURL, phoneNumber, profName, profEmail,
	triggerKeyword):
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()
	
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+
	';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
	crsr = cnxn.cursor()
	
	sqlCommand = """INSERT INTO opportunities 
	(oppTitle, oppURL, phoneNumber, profName, profEmail, triggerKeyword, \
	isRead)
	VALUES("{title}", "{url}", "{num}", "{pname}", "{pemail}", "{kw}",
	"f");"""

	sqlCommand = sqlCommand.format(title = oppTitle, url=oppURL, 
		num=phoneNumber, pname=profName, pemail=profEmail, kw=triggerKeyword)

	crsr.execute(sqlCommand)

	cnxn.commit()
	cnxn.close()

	cnxn.commit()
	cnxn.close()

