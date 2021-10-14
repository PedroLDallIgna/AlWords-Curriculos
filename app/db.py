import json

class DB():

    def __init__(self, file):
        self.filename = file
        self.data = []
    
    def get_db(self):
        with open(self.filename, 'r') as read_file:
            return json.load(read_file)

    def update_db(self, to_update):
        users_updated = self.get_db()
        users_updated.append(to_update)
        with open(self.filename, 'w') as write_file:
            json.dump(users_updated, write_file, indent=4)
        return 'ok'

    def get_users(self):
        return [user['_id'] for user in self.get_db()]

    # def remove_data(self):  
