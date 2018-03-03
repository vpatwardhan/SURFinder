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
	return cnxn;

########################################################################

# Person Table Accessors 

# Gets all the phone numbers listed in the database.
def getAllPhones(cnxn):

# Gets the name associated with a phone number.
def getName(cnxn, phone):

# Gets the first keyword associated with a phone number.
def getKeyword1(cnxn, phone):

# Gets the second keyword associated with a phone number.
def getKeyword2(cnxn, phone):

# Gets the third keyword associated with a phone number.
def getKeyword3(cnxn, phone):

# Checks whether a given person (identified by phone number) has new 
# opportunities listed. Returns a boolean.
def isNewInfo(cnxn, phone):


######################################################################

# Opportunity Table Accessors

# Gets new opportunities for a certain phone number. Returns array of ID 
# strings, sets opportunites to read.
def getNewOpportunites(cnxn, phone):

# Gets the URL of a specific opportunity.
def getOppURL(cnxn, oppID):

# Gets the professor's name for a specific opportunity.
def getOppProfName(cnxn, oppID):

# Gets the professor's email for a specific opportunity.
def getOppProfEmail(cnxn, oppID):

# Gets the person's phone number for a specific opportunity.
def getOppPhone(cnxn, oppID):

# Gets the trigger keyword for a specific opportunity.
def getOppKeyword(cnxn, oppID):

# Takes a csv file and adds the data to the database, updating the person's
# new info flag in the process. Returns success/failure boolean.
def csvToDatabase(cnxn, oppID):



