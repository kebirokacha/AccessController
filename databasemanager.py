import shutil
import sqlite3
import json
import os

class DataBaseManager:
	def __init__(self ,databasePath:str = "security_system.db" ,personImagePath:str = "person_pictures"):
		if not os.path.isfile(databasePath):
			open(databasePath, "w").close()
		if not os.path.exists(personImagePath):
			os.mkdir(personImagePath)
		self.personImagePath = personImagePath
		# connect to the database file
		self.connection = sqlite3.connect(databasePath)
		self.initializeDatabase()

	def initializeDatabase(self)  -> None:
		with self.connection:
			self.connection.execute("""
					CREATE TABLE IF NOT EXISTS person (
						id INTEGER PRIMARY KEY AUTOINCREMENT,
						name TEXT NOT NULL UNIQUE,
						birthday TEXT NOT NULL,
						phone TEXT NOT NULL,
						email TEXT NOT NULL,
						address TEXT NOT NULL
					);
				"""
			)
			self.connection.execute("""
				CREATE TABLE IF NOT EXISTS faceEmbedding (
						id INTEGER PRIMARY KEY AUTOINCREMENT,
						embedding TEXT NOT NULL,
						personID INTEGER NOT NULL,
						FOREIGN KEY(personID) REFERENCES person(id)
					);
				"""
			)
			self.connection.commit()

	def addPerson(self, name:str ,birthday:str ,phone:str ,email:str ,address:str ,embeddingsList:list[list] ,picturesPaths:list) -> None:
		destinationPath = os.path.join(self.personImagePath ,name)
		if not os.path.exists(destinationPath):
			os.mkdir(destinationPath)
		for imageIndex ,picturePath in enumerate(picturesPaths):
			pictureDestination = os.path.join(destinationPath,f"{imageIndex}.jpg")
			shutil.copy2(picturePath, pictureDestination)
		with self.connection:
			cursor = self.connection.execute("""
					INSERT INTO person (name, birthday, phone, email, address) VALUES (?, ?, ?, ?, ?);
					""", (name, birthday, phone, email, address)
				)
			self.connection.commit()
			personId = cursor.lastrowid
			for embedding in embeddingsList:
				embeddingJson = json.dumps(embedding)
				self.connection.execute("""
					INSERT INTO faceEmbedding (embedding, personID) VALUES (?, ?);
					""", (embeddingJson, personId)
				)
			self.connection.commit()

			
	def modifyPerson(self, id:int ,newName:str ,oldName:str ,birthday:str ,phone:str ,email:str ,address:str ,embeddingsList:list[list] ,picturesPaths:list) -> None:
		# Delete the folder with it's old name
		oldPath = os.path.join(self.personImagePath ,oldName)
		if os.path.exists(oldPath):
			shutil.rmtree(oldPath)
		destinationPath = os.path.join(self.personImagePath ,newName)
		if not os.path.exists(destinationPath):
			os.mkdir(destinationPath)
		for imageIndex ,picturePath in enumerate(picturesPaths):
			pictureDestination = os.path.join(destinationPath,f"{imageIndex}.jpg")
			shutil.copy2(picturePath, pictureDestination)
		with self.connection:
			self.connection.execute("""
				UPDATE person SET name = ?, birthday = ?, phone = ?, email = ?, address = ? WHERE id = ?;
				""", (newName, birthday, phone, email, address, id)
			)
			self.connection.commit()
			self.connection.execute("""
				DELETE FROM faceEmbedding WHERE personID = ?;
				""", (id,)
			)
			for embedding in embeddingsList:
				embeddingJson = json.dumps(embedding)
				self.connection.execute("""
					INSERT INTO faceEmbedding (embedding, personID) VALUES (?, ?);
					""", (embeddingJson, id)
				)
			self.connection.commit()
			
	def modifyPersonWithoutEmbedding(self ,id:int ,newName:str  ,oldName:str ,birthday:str ,phone:str ,email:str ,address:str) -> None:
		# Modify the file name of the persone
		if oldName != newName:
			oldSourcePath = os.path.join(self.personImagePath, oldName)
			newSourcePath = os.path.join(self.personImagePath, newName)
			os.rename(oldSourcePath, newSourcePath)
		# Update the person info without changing it's embedding
		with self.connection:
			self.connection.execute("""
				UPDATE person SET name = ?, birthday = ?, phone = ?, email = ?, address = ? WHERE id = ?;
				""", (newName, birthday, phone, email, address, id)
			)
			self.connection.commit()

	def deletePerson(self, personId:int ,name:str) -> None:
		destinationPath = os.path.join(self.personImagePath ,name)
		if os.path.exists(destinationPath):
			shutil.rmtree(destinationPath)
		with self.connection:
			self.connection.execute("""
				DELETE FROM person WHERE id = ?;
				""",(personId ,)
			)
			self.connection.commit()
			self.connection.execute("""
				DELETE FROM faceEmbedding WHERE personID = ?
				""",(personId ,)
			)
			self.connection.commit()


	def getPersonByName(self, name:str):
		with self.connection:
			cursor = self.connection.execute("""
				SELECT * FROM person WHERE name = ?;
				""", (name,)
			)
			row = cursor.fetchone()
			if row:
				return {'id': row[0], 'name': row[1], 'birthday': row[2], 'phone': row[3], 'email': row[4], 'address': row[5]}
			else:
				return None
	
	def getPersonByPhone(self, phone:str):
		with self.connection:
			cursor = self.connection.execute("""
				SELECT * FROM person WHERE phone = ?;
				""", (phone,)
			)
			row = cursor.fetchone()
			if row:
				return {'id': row[0], 'name': row[1], 'birthday': row[2], 'phone': row[3], 'email': row[4], 'address': row[5]}
			else:
				return None

	def getPersonByEmail(self, email:str):
		with self.connection:
			cursor = self.connection.execute("""
				SELECT * FROM person WHERE email = ?;
				""", (email,)
			)
			row = cursor.fetchone()
			if row:
				return {'id': row[0], 'name': row[1], 'birthday': row[2], 'phone': row[3], 'email': row[4], 'address': row[5]}
			else:
				return None

	def getEncodingArray(self) -> dict:
		with self.connection:
			cursor = self.connection.execute("""
				SELECT personID, embedding FROM faceEmbedding;
				"""
			)
		embeddingsByPersonId = {}
		# Iterate through the rows and populate the dictionary
		for row in cursor:
			personId, embedding = row
			if personId not in embeddingsByPersonId:
				embeddingsByPersonId[personId] = []
			embeddingsByPersonId[personId].append(embedding)
		return embeddingsByPersonId

	def getAllPersonsInfo(self) -> list:
		with self.connection:
			cursor = self.connection.execute("""
				SELECT * FROM person;
				"""
			)
			personsInfo = []
			for row in cursor:
				personDict = {
					'id': row[0],
					'name': row[1],
					'birthday': row[2],
					'phone': row[3],
					'email': row[4],
					'address': row[5],
				}
				personsInfo.append(personDict)
			return personsInfo