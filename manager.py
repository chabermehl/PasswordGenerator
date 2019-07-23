import json


class manager():

    def __init__(self):

        self.path = '.\\vault.json'
        self.entries = {}

    def load_vault(self):
        self.loose_entries = self.entries
        try:
            with open(self.path, 'r') as file:
                self.entries = json.load(file)
                print(self.entries)
        except ImportError:
            print('File does not exist...')

    def save_vault(self, merge=True):
        if merge is True:
            self.entries.update(self.loose_entries)
            self.loose_entries.clear()

        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(self.entries, file, ensure_ascii=False, indent=4)

    def close_vault(self, save=True):
        if save is True:
            self.save_vault()

        self.entries.clear()

    def create_entry(self, title, username, password=""):
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

    def get_entry(self, title):
        if title in self.loose_entries:
            return self.loose_entries[title]
        elif title in self.entries:
            return self.entries[title]
        else:
            return None

    def set_path(self, path):
        self.path = path
