import json

import generator

'''
A vault will be a password file. The reason I'm making this distinction is for
future functionality, such as the ability to save the vault as a portable
file to sync over google drive etc, and also to keep passwords logically
partitioned on disk.
'''

class manager():

	def __init__(self):

		self.entries = {}


	'''
	Load JSON file containing all dict entries
	This will later be encrypted!
	'''
	def load_vault(self, path):

		try:
			with open(path, 'r') as file:
				self.entries = json.load(file)
				print(self.entries)
		except:

			print("File does not exist...\nCreate New?")

	def save_vault(self, path):
		
		with open(path, 'w', encoding='utf-8') as file:
			json.dump(self.entries, file, ensure_ascii=False, indent=4)



	def create_entry(self, title, username, password=""):
		'''TODO: If no password, use generator to create one'''
		self.entries.update({title: [username, password]})

	
	def edit_entry(self, title, username="", password=""):

		if len(username) > 1:
			self.entries[title][0] = username
		
		if len(password) > 1:
			self.entries[title][1] = password


	def delete_entry(self, title):

		self.entries.pop(title, None)


	def get_all_entries(self):

		return self.entries