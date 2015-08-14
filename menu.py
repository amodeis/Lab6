#LAB6 Python starter code
#imports go here
#import MySQLdb
import _mysql

#code goes here

buffer = "true"



def oneQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="knockers",db="VideoGameLibrary")
	db.query("""SELECT * FROM Game;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def twoQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="knockers",db="VideoGameLibrary")
	db.query("""SELECT * FROM Developer;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def threeQuery():
        db = _mysql.connect(host="localhost",user="root",passwd="knockers",db="VideoGameLibrary")
	db.query("""SELECT * FROM Platform;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def fourQuery():
        db = _mysql.connect(host="localhost",user="root",passwd="knockers",db="VideoGameLibrary")
	db.query("""SELECT * FROM Manufacturer;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def fiveQuery():
        db = _mysql.connect(host="localhost",user="root",passwd="knockers",db="VideoGameLibrary")
	db.query("""SELECT A.gameName, B.platformName
                FROM Game AS A, Platform AS B, GamePlatform AS C
                WHERE C.gameID = A.gameID AND C.platformID = B.platformID;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def sixQuery():
        db = _mysql.connect(host="localhost",user="root",passwd="knockers",db="VideoGameLibrary")
	db.query("""SELECT A.manufacturerName, B.platformName
                FROM Manufacturer AS A, Platform AS B, ManufacturerPlatform AS C
                WHERE C.manufacturerID = A.manufacturerID AND C.platformID = B.platformID;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def sevenQuery():
        db = _mysql.connect(host="localhost",user="root",passwd="knockers",db="VideoGameLibrary")
	db.query("""INSERT INTO Manufacturer (manufacturerID, manufacturerName, manufacturerHQ)
               VALUES ('6', 'Microsoft', 'Redmond Washington');""")

	
while buffer:
	print("""
        0. Exit
	1. See games.
	2. See developers.
	3. See platforms.
	4. See manufacturers.
	5. See the platforms and games relationships.
        6. See the manufacturers and platforms relationships.
        7. Insert into the Manufacturer table.
	""")
	buffer=input("what would you like to do? ")
	if buffer == 1:
		oneQuery()
	if buffer == 2:
		twoQuery()
	if buffer == 3:
		threeQuery()
        if buffer == 4:
                fourQuery()
        if buffer == 5:
                fiveQuery()
        if buffer == 6:
                sixQuery()
        if buffer == 7:
                sevenQuery()
