# for person in db
# find opps
# add opps to db
# for person
# if new
# text
# new == false
conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=test;'
    r'DATABASE=test;'
    r'UID=user;'
    r'PWD=password'
    )