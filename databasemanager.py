import sqlite3
import os

class DataBaseManager:
	def __init__(self, database_path="peoples.db"):
		# check if the database file exists
		if not os.path.isfile(database_path):
			# if not, create a new file
			open(database_path, "w").close()
		# connect to the database file
		self.connection = sqlite3.connect(database_path)
		self.createTable()

	def createTable(self):
		with self.connection:
			self.connection.execute("""
				CREATE TABLE IF NOT EXISTS persons (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    birthday TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT NOT NULL,
                    address TEXT NOT NULL,
                    encoding TEXT NOT NULL
                );
			""")
			self.connection.commit()

	def addPerson(self, name, birthday, phone, email, address, encoding):
		with self.connection:
			# Save the encoding as a string directly
			encodingStr = ",".join(map(str, encoding))
			self.connection.execute("""
				INSERT INTO persons (name, birthday, phone, email, address, encoding) VALUES (?, ?, ?, ?, ?, ?);
			""", (name, birthday, phone, email, address, encodingStr))
			self.connection.commit()
			
	def modifyPerson(self, id, name, birthday, phone, email, address, encoding):
		with self.connection:
			# Save the encoding as a string directly
			encodingStr = ",".join(map(str, encoding))
			self.connection.execute("""
				UPDATE persons SET name = ?, birthday = ?, phone = ?, email = ?, address = ?, encoding = ? WHERE id = ?;
			""", (name, birthday, phone, email, address, encodingStr, id))
			self.connection.commit()
			
	def modifyPersonWithoutEncoding(self, id, name, birthday, phone, email, address):
		with self.connection:
			self.connection.execute("""
				UPDATE persons SET name = ?, birthday = ?, phone = ?, email = ?, address = ? WHERE id = ?;
			""", (name, birthday, phone, email, address, id))
			self.connection.commit()

	def deletePerson(self, personId):
		with self.connection:
			self.connection.execute("""
				DELETE FROM persons WHERE id = ?;
			""", (personId,))
			self.connection.commit()

	def getPersonByName(self, name):
		with self.connection:
			cursor = self.connection.execute("""
				SELECT * FROM persons WHERE name = ?;
			""", (name,))
			row = cursor.fetchone()
			if row:
				return {'id': row[0], 'name': row[1], 'birthday': row[2], 'phone': row[3], 'email': row[4], 'address': row[5], 'encoding': row[6]}
			else:
				return None
	
	def getPersonByPhone(self, phone):
		with self.connection:
			cursor = self.connection.execute("""
				SELECT * FROM persons WHERE phone = ?;
			""", (phone,))
			row = cursor.fetchone()
			if row:
				return {'id': row[0], 'name': row[1], 'birthday': row[2], 'phone': row[3], 'email': row[4], 'address': row[5], 'encoding': row[6]}
			else:
				return None

	def getPersonByEmail(self, email):
		with self.connection:
			cursor = self.connection.execute("""
				SELECT * FROM persons WHERE email = ?;
			""", (email,))
			row = cursor.fetchone()
			if row:
				return {'id': row[0], 'name': row[1], 'birthday': row[2], 'phone': row[3], 'email': row[4], 'address': row[5], 'encoding': row[6]}
			else:
				return None

	def getEncodingList(self, name):
		with self.connection:
			cursor = self.connection.execute("""
				SELECT encoding FROM persons WHERE name = ?;
			""", (name,))
			row = cursor.fetchone()
			if row:
				encodingStr = row[0]
				# Convert the encoding string into a list of floats
				encodingList = list(map(float, encodingStr.split(",")))
				return encodingList
			else:
				return None

	def getEncodingArray(self):
		with self.connection:
			cursor = self.connection.execute("""
				SELECT encoding FROM persons;
			""")
			encodingList = []
			for row in cursor:
				encodingStr = row[0]
				# Remove square brackets and then split the encoding string using any whitespace as a separator
				encodingList.append(list(map(float, encodingStr.strip('[]').split())))
			return encodingList

	def getPersonNames(self):
		with self.connection:
			cursor = self.connection.execute("""
				SELECT name FROM persons;
			""")
			namesList = [row[0] for row in cursor]
			return namesList

	def getAllPersonsInfo(self):
		with self.connection:
			cursor = self.connection.execute("""
				SELECT * FROM persons;
			""")
			personsInfo = []
			for row in cursor:
				personDict = {
					'id': row[0],
					'name': row[1],
					'birthday': row[2],
					'phone': row[3],
					'email': row[4],
					'address': row[5],
					'encoding': row[6]
				}
				personsInfo.append(personDict)
			return personsInfo